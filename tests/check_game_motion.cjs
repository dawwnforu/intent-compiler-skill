// Unit-level execution of saved game scripts; this does not emulate browser hit testing.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const root = process.argv[2];


function observe(html, arm, suppressPointer, reduced) {
  let now = 1000, nextFrame, ballY, markers = [], obstacleXs = [];
  const drawing = new Proxy({}, {
    get: (target, key) => key in target ? target[key] : () => {},
  });
  drawing.roundRect = (x, y, w, h) => { if (drawing.fillStyle === '#426451') obstacleXs.push(x); };
  drawing.moveTo = (x, y) => { if (y === 426) markers.push(x); };
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
  const media = { ...element(), matches: reduced };
  media.addListener = fn => media.addEventListener('change', fn);
  const context = vm.createContext({ document, window, devicePixelRatio: 1,
    localStorage: { getItem: () => null, setItem() {} },
    matchMedia: () => media, performance: { now: () => now },
    requestAnimationFrame: fn => { nextFrame = fn; }, Math: math,
  });
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length, 1);
  vm.runInContext(scripts[0][1], context, { timeout: 1000 });
  function frames(count) {
    for (let i = 0; i < count; i++) {
      now += 1000 / 60;
      assert.equal(typeof nextFrame, 'function');
      markers = []; obstacleXs = []; nextFrame(now);
    }
    assert(Number.isFinite(ballY));
    return ballY;
  }
  ids.get(['A', 'G'].includes(arm) ? 'start' : 'action').fire('click');
  // Let V2's automatic starting jump land before comparing the same input.
  const before = frames(54);
  const markersBefore = markers.slice();
  ids.get(arm === 'A' ? 'game' : arm === 'V2' ? 'arena' : 'stage').fire('pointerdown');
  const after = frames(6);
  const markersAfter = markers.slice();
  frames(42); const obstaclesBefore = obstacleXs.slice();
  frames(6); const obstaclesAfter = obstacleXs.slice();
  let ticks = 0;
  while (ids.get('overlay').hidden && ticks++ < 600) frames(1);
  const collisionEnded = ids.get('overlay').hidden === false;
  ids.get('action').fire('click'); frames(1);
  const restarted = ids.get('overlay').hidden === true && Number(ids.get('score').textContent) === 0;
  return { before, after, rise: before - after, markersBefore, markersAfter,
    obstaclesBefore, obstaclesAfter, collisionEnded, restarted };
}


const html = fs.readFileSync(root, 'utf8');
const ordinary = observe(html, 'V2', false, false);
const reduced = observe(html, 'V2', false, true);
const reducedGroundStatic = JSON.stringify(reduced.markersBefore) === JSON.stringify(reduced.markersAfter);
if (process.argv.includes('--expect-fixed')) {
  assert(reducedGroundStatic, 'Reduced decoration must stop scrolling');
  assert.notDeepEqual(ordinary.markersBefore, ordinary.markersAfter);
  for (const result of [ordinary, reduced]) {
    assert.equal(result.markersBefore.length, 16, 'Do not pass because markers vanished');
    assert(result.rise > 20 && result.collisionEnded && result.restarted);
    assert(result.obstaclesBefore.length && result.obstaclesAfter.length);
    assert(result.obstaclesAfter[0] < result.obstaclesBefore[0]);
  }
}
console.log(JSON.stringify({ordinary, reduced, reducedGroundStatic}, null, 2));
