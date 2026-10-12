const vm = require('vm');
const fs = require('fs');
const assert = require('assert');

// Offline logic test. This does not test a browser, speakers, or audible output.
(async () => {
  for (const file of ['deck/week06_analysis.js', 'deck/week06_sequencer.js']) {
    const events = {}, docEvents = {}, contexts = [];
    function parameter() {
      return { value: 0, setValueAtTime() {}, linearRampToValueAtTime() {},
        exponentialRampToValueAtTime() {}, setTargetAtTime() {} };
    }
    class AudioContext {
      constructor() {
        this.state = 'suspended'; this.currentTime = 0; this.sampleRate = 48000;
        this.destination = {}; this.starts = 0; contexts.push(this);
      }
      resume() { this.state = 'running'; return Promise.resolve(); }
      close() { this.state = 'closed'; return Promise.resolve(); }
      createOscillator() {
        return { frequency: parameter(), connect() {},
          start: () => this.starts++, stop() {} };
      }
      createGain() { return { gain: parameter(), connect() {} }; }
      createAnalyser() { return { fftSize: 2048, frequencyBinCount: 1024, connect() {} }; }
    }
    const window = { parent: {}, AudioContext,
      addEventListener: (name, f) => (events[name] ??= []).push(f) };
    const document = { hidden: false,
      addEventListener: (name, f) => (docEvents[name] ??= []).push(f) };
    const c = vm.createContext({ window, document, console, Float32Array, Math, Array,
      mouseX: 100, mouseY: 490, setInterval: () => 1, clearInterval() {},
      floor: Math.floor, constrain: (x, l, h) => Math.max(l, Math.min(h, x)) });
    vm.runInContext(fs.readFileSync(file, 'utf8'), c);
    assert.equal(contexts.length, 0, 'must start silent');
    const start = () => vm.runInContext(file.includes('analysis') ? 'playAudio()' : 'mousePressed()', c);
    await start();
    assert.equal(vm.runInContext('running', c), true);
    assert(contexts.at(-1).starts > 0);
    events.message.forEach(f => f({ source: {}, data: 'slide:stop' }));
    assert.equal(vm.runInContext('running', c), true, 'foreign sender cannot stop');
    events.message.forEach(f => f({ source: window.parent, data: 'slide:stop' }));
    assert.equal(vm.runInContext('running', c), false);
    assert.equal(contexts.at(-1).state, 'closed');
    await start();
    document.hidden = true;
    docEvents.visibilitychange.forEach(f => f());
    assert.equal(vm.runInContext('running', c), false);
    assert.equal(contexts.at(-1).state, 'closed');
    const promise = start();
    vm.runInContext('stopAudio()', c);
    await promise;
    assert.equal(vm.runInContext('running', c), false);
    assert.equal(contexts.at(-1).starts, 0, 'stop during resume prevents start');
    console.log(file + ': silent load, start, authorized slide stop, visibility stop, and start/stop race pass (mock audio).');
  }
})().catch(error => { console.error(error); process.exit(1); });
