// Unit-level execution of saved game scripts; this does not emulate browser hit testing.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const root = process.argv[2];
const saved = root ? null : JSON.parse(fs.readFileSync(
  path.join(__dirname, 'results/v2-game-jump.json'), 'utf8').replace(/^\uFEFF/, ''));

function observe(html, arm, suppressPointer) {
  let now = 1000, nextFrame, ballY;
  const drawing = new Proxy({}, {
    get: (target, key) => key in target ? target[key] : () => {},
  });
  drawing.translate = (x, y) => { ballY = y; };
  function element() {
    const listeners = new Map();
    return {
      width: 390, height: 600, clientWidth: 390, clientHeight: 600,
      classList: { add() {}, remove() {} },
      getBoundingClientRect: () => ({ width: 390, height: 600 }),
      getContext: () => drawing, closest: () => null,
      addEventListener(type, fn) {
        if (!listeners.has(type)) listeners.set(type, new Set());
        listeners.get(type).add(fn);
      },
      removeEventListener(type, fn) { listeners.get(type)?.delete(fn); },
      fire(type) {
        if (type === 'pointerdown' && suppressPointer) return;
        for (const fn of listeners.get(type) || []) fn({ target: this, preventDefault() {} });
      },
    };
  }
  const ids = new Map([...html.matchAll(/id="([^"]+)"/g)].map(m => [m[1], element()]));
  const document = { ...element(), hidden: false, getElementById(id) {
    assert(ids.has(id), `Missing fixture element ${id}`);
    return ids.get(id);
  } };
  const window = { ...element(), devicePixelRatio: 1 };
  const math = Object.create(Math); math.random = () => 0.5;
  const context = vm.createContext({ document, window, devicePixelRatio: 1,
    localStorage: { getItem: () => null, setItem() {} },
    matchMedia: () => ({ matches: false }), performance: { now: () => now },
    requestAnimationFrame: fn => { nextFrame = fn; }, Math: math,
  });
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length, 1);
  vm.runInContext(scripts[0][1], context, { timeout: 1000 });
  function frames(count) {
    for (let i = 0; i < count; i++) {
      now += 1000 / 60;
      assert.equal(typeof nextFrame, 'function');
      nextFrame(now);
    }
    assert(Number.isFinite(ballY));
    return ballY;
  }
  ids.get(['A', 'G'].includes(arm) ? 'start' : 'action').fire('click');
  // Let V2's automatic starting jump land before comparing the same input.
  const before = frames(54);
  ids.get(arm === 'A' ? 'game' : arm === 'V2' ? 'arena' : 'stage').fire('pointerdown');
  const after = frames(6);
  return { before, after, rise: before - after };
}

const results = [];
for (const arm of ['A', 'G', 'V1', 'V2']) {
  const html = root ? fs.readFileSync(path.join(root, arm, 'workspace/index.html'), 'utf8')
    : saved.results.find(result => result.arm === arm).html;
  const active = observe(html, arm, false);
  const suppressed = observe(html, arm, true);
  assert(active.rise > 20, `${arm}: pointer handler must cause a jump`);
  assert(Math.abs(suppressed.rise) < 2, `${arm}: no-input control must remain grounded`);
  results.push({ arm, active, suppressed, passed: true, html });
}
console.log(JSON.stringify({
  scope: 'Historical unchanged scripts; deterministic 60 Hz mocked DOM/canvas unit check',
  limits: 'No browser event dispatch, touch hit testing, reduced-motion or current-Skill comparison',
  results,
}, null, 2));
