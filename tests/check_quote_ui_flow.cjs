// Executes unchanged R35 UI handlers with an in-memory DOM/storage; not a browser test.
const fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const assert = require('node:assert/strict');
const root = path.resolve(process.argv[2]);
const source = fs.readFileSync(path.join(root, 'quote-ui.js'), 'utf8');
const core = require(path.join(root, 'quote-core.js'));
const storage = new Map();
function boot() {
  const elements = new Map(), downloads = [], blobs = new Map();
  let consent = true;
  const get = id => {
    if (!elements.has(id)) elements.set(id, {value:'', checked:false, hidden:true, innerHTML:'', textContent:'', handlers:{}, addEventListener(k, fn){this.handlers[k]=fn;}});
    return elements.get(id);
  };
  const context = vm.createContext({QuoteCore:core, TextDecoder, Blob, console,
    document:{getElementById:get, createElement:()=>({click(){downloads.push({name:this.download, blob:blobs.get(this.href)});}})},
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},
    URL:{createObjectURL:b=>{const k=String(blobs.size);blobs.set(k,b);return k;},revokeObjectURL:()=>{}},
    confirm:()=>consent, setTimeout:()=>0});
  vm.runInContext(source, context);
  const dispatch = async (id, files) => get(id).handlers.change({target:{files,value:'fixture'}});
  return {get, downloads, dispatch, consent:v=>{consent=v;}};
}
const file = (name, text) => ({name,arrayBuffer:async()=>new TextEncoder().encode(text).buffer});
const input = name => file(name,fs.readFileSync(path.join(root,'inputs',name),'utf8'));
const saved = () => JSON.parse(storage.get('weekly-quotes-v1')).rows;
(async()=>{
  let app=boot();
  await app.dispatch('csvFiles',[input('09-30.csv'),file('broken.csv','bad headers\ninvalid'),input('10-07.csv')]);
  assert.equal(saved().length,9);
  assert.match(app.get('status').textContent,/broken.csv.*未导入/);
  assert.match(app.get('status').textContent,/10-07.csv.*新增/);
  assert.equal(app.get('status').className,'status error');
  assert(!app.get('results').innerHTML.includes('全部历史'));
  app.get('history').checked=true;app.get('history').onchange();
  assert.match(app.get('results').innerHTML,/全部历史/);
  assert.match(app.get('results').innerHTML,/2026-09-30/);
  app.get('backup').onclick();
  const backup=await app.downloads.at(-1).blob.text();
  assert.deepEqual(JSON.parse(backup).rows,saved());
  const original=JSON.stringify(saved());
  app.consent(false);app.get('clear').onclick();assert.equal(JSON.stringify(saved()),original);
  app.consent(true);app.get('clear').onclick();assert.equal(saved().length,0);
  await app.dispatch('restoreFile',[file('backup.json',backup)]);
  assert.equal(JSON.stringify(saved()),original);
  await app.dispatch('restoreFile',[file('backup.json',backup)]);
  assert.equal(saved().length,9);assert.match(app.get('status').textContent,/新增 0 条/);
  await app.dispatch('restoreFile',[file('corrupt.json','{"version":1,"rows":')]);
  assert.equal(JSON.stringify(saved()),original);assert.match(app.get('status').textContent,/备份未恢复/);
  app=boot();assert.match(app.get('stats').textContent,/9 条历史报价/);
  app.get('search').value='A4-80gsm';app.get('search').oninput();
  assert.equal((app.get('results').innerHTML.match(/<article>/g)||[]).length,1);
  app.get('export').onclick();
  const csv=await app.downloads.at(-1).blob.text();
  assert(csv.includes('A4-70gsm')&&csv.includes('Black-0.5mm'));
  assert.match(app.get('status').textContent,/全部物料，不受搜索筛选影响/);
  console.log(JSON.stringify({passed:true,checks:['mixed valid-invalid-valid import retains both valid files','history toggle renders old quotes','backup actual Blob equals stored rows','cancelled clear preserves rows','confirmed clear and restore recovers all rows','duplicate restore adds zero','corrupt restore preserves rows','fresh UI context reloads stored rows','search narrows rendered groups','export contains all specifications with explicit notice'],scope:'Original UI event handlers and core executed with mocked DOM, storage and download dispatch; no browser file picker, actual downloaded file, layout or native GUI assertion'},null,2));
})().catch(e=>{console.error(e);process.exitCode=1;});
