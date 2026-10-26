'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const dir = path.join(root, 'pilot/demo');
const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
const script = fs.readFileSync(path.join(dir, 'demo.js'), 'utf8');
const dataScript = fs.readFileSync(path.join(dir, 'data.js'), 'utf8');

function element(dataset = {}) {
  return {dataset, textContent: '', value: '', attrs: {}, handlers: {},
    setAttribute(k, v) { this.attrs[k] = v; },
    addEventListener(k, fn) { this.handlers[k] = fn; },
    focus() { this.focused = true; }, select() { this.selected = true; },
    set innerHTML(_) { throw Error('Untrusted HTML insertion'); }};
}
function load(clipboard) {
  const nodes = Object.fromEntries(['artifact', 'artifact-label', 'artifact-summary', 'download', 'language', 'starter', 'copy-status', 'copy', 'request', 'change'].map(id => ['#' + id, element()]));
  const views = ['initial', 'final'].map(view => element({view}));
  const translated = [...html.matchAll(/data-zh="([^"]*)" data-en="([^"]*)"/g)].map(match => element({zh: match[1], en: match[2]}));
  const doc = {documentElement: {}, querySelector: selector => nodes[selector],
    querySelectorAll: selector => selector === '[data-view]' ? views : translated};
  const context = {window: {}, document: doc, navigator: {clipboard}};
  vm.runInNewContext(dataScript, context);
  vm.runInNewContext(script, context);
  return {nodes, views, translated, context};
}
async function main() {
  let copied = null;
  const page = load({writeText: async value => { copied = value; }});
  const {nodes, views, context} = page;
  const data = context.window.pilotDemoData;
  for (const key of ['requestExcerpt', 'changeExcerpt', 'initial', 'final']) assert.equal(typeof data[key], 'string');
  assert.doesNotMatch(dataScript, /PSPath|PSParentPath|C:\\\\Users/);
  assert.equal(data.final, fs.readFileSync(path.join(root, 'tests/results/intent-handoff-r99/C-brief.md'), 'utf8'));
  assert.equal(data.initial, fs.readFileSync(path.join(dir, 'initial-handoff.md'), 'utf8'));
  assert.equal(data.final, fs.readFileSync(path.join(dir, 'final-brief.md'), 'utf8'));
  assert.ok(fs.readFileSync(path.join(dir, 'history.md'), 'utf8').includes(data.requestExcerpt));
  assert.ok(fs.readFileSync(path.join(dir, 'change-request.txt'), 'utf8').includes(data.changeExcerpt));
  assert.equal(data.source.runtimeSource, 'cefba82343fef6512a31f96013fc20793f878dd5');
  assert.equal(nodes['#artifact'].textContent, data.final);
  assert.equal(nodes['#download'].href, 'final-brief.md');
  views[0].handlers.click();
  assert.equal(nodes['#artifact'].textContent, data.initial);
  assert.equal(views[0].attrs['aria-pressed'], 'true');
  assert.equal(nodes['#download'].href, 'initial-handoff.md');
  nodes['#language'].handlers.click();
  assert.equal(context.document.documentElement.lang, 'en');
  assert.equal(nodes['#artifact'].textContent, data.initial);
  assert.ok(nodes['#starter'].value.startsWith('Load Intent Compiler'));
  assert.match(nodes['#artifact-summary'].textContent, /Tiaotiao/);
  assert.match(nodes['#artifact-summary'].textContent, /not a separate English model output/);
  await nodes['#copy'].handlers.click();
  assert.equal(copied, nodes['#starter'].value);
  assert.match(nodes['#copy-status'].textContent, /Copy requested/);
  assert.equal(nodes['#starter'].selected, true);
  nodes['#language'].handlers.click();
  assert.equal(context.document.documentElement.lang, 'zh-CN');
  assert.ok(page.translated.some(node => node.textContent.includes('\n')));
  const denied = load({writeText: async () => { throw Error('Denied'); }});
  await denied.nodes['#copy'].handlers.click();
  assert.equal(denied.nodes['#starter'].selected, true);
  assert.match(denied.nodes['#copy-status'].textContent, /手动复制/);
  const missing = load(undefined);
  await missing.nodes['#copy'].handlers.click();
  assert.equal(missing.nodes['#starter'].selected, true);
  data.final = '<img src=x onerror=alert(1)> & original text';
  views[1].handlers.click();
  assert.equal(nodes['#artifact'].textContent, data.final);
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    if (match[1].startsWith('#')) continue;
    if (/^https:/.test(match[1])) continue;
    assert.ok(fs.existsSync(path.resolve(dir, match[1])), 'Missing linked resource: ' + match[1]);
  }
  assert.doesNotMatch(script, /\b(fetch|XMLHttpRequest|localStorage|sessionStorage|sendBeacon)\b/);
  assert.match(html, /四组均通过/);
  assert.match(html, /开发助手构造/);
  assert.match(html, /新包渠道完整业务仍未验证/);
  const log = fs.readFileSync(path.join(root, 'pilot/pilot-log.csv'), 'utf8').trim().split(/\r?\n/);
  assert.equal(log.length, 1, 'Participant records must remain private, not synthetic rows');
  assert.ok(log[0].endsWith(',market,entry_channel,public_post_ref'));
  console.log('PASS: frozen-artifact fidelity; original UI handlers; language/state; copy success/denied/missing; literal text; local resources; no telemetry; empty participant log');
  console.log('DOM adapter checks only; not browser, clipboard permission, download, user acceptance or model-effect evidence.');
}
main().catch(error => { console.error(error); process.exitCode = 1; });
