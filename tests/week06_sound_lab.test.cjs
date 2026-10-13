const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

// Browser-free contract test; physical speakers and volume still need preflight.
(async () => {
  const events = {}, docEvents = {}, contexts = [];
  class AudioContext {
    constructor() {
      this.state = 'suspended'; this.destination = {};
      this.starts = 0; this.buffers = []; contexts.push(this);
    }
    resume() { this.state = 'running'; return Promise.resolve(); }
    close() { this.state = 'closed'; return Promise.resolve(); }
    createBuffer(channels, count, rate) {
      const buffer = { channels, count, rate,
        copyToChannel(data) { this.samples = data; } };
      this.buffers.push(buffer);
      return buffer;
    }
    createBufferSource() {
      return { connect() {}, stop() {}, start: () => this.starts++, onended: null };
    }
  }
  const window = { parent: {}, AudioContext,
    addEventListener: (name, f) => (events[name] ??= []).push(f) };
  const document = { hidden: false,
    addEventListener: (name, f) => (docEvents[name] ??= []).push(f) };
  const c = vm.createContext({ window, document, console, Float32Array, Math });
  vm.runInContext(fs.readFileSync('deck/week06_sound_lab.js', 'utf8'), c);
  assert.equal(contexts.length, 0, 'the slide must load silent');

  await vm.runInContext('playAudio()', c);
  const tone = contexts.at(-1).buffers[0];
  assert.deepEqual([tone.channels, tone.count, tone.rate], [1, 44100, 22050]);
  assert.equal(contexts.at(-1).starts, 1);
  assert(tone.samples[0] === 0);
  assert(tone.samples.at(-1) === 0);
  assert(Math.max(...tone.samples) <= 0.08);
  assert.equal(vm.runInContext('running', c), true);

  events.message.forEach(f => f({ source: {}, data: 'slide:stop' }));
  assert.equal(vm.runInContext('running', c), true);
  events.message.forEach(f => f({ source: window.parent, data: 'slide:stop' }));
  assert.equal(vm.runInContext('running', c), false);
  assert.equal(contexts.at(-1).state, 'closed');

  vm.runInContext("mode = 'noise'", c);
  await vm.runInContext('playAudio()', c);
  const noise = contexts.at(-1).buffers[0].samples;
  assert.notEqual(noise[101], tone.samples[101]);
  assert.equal(noise[101], vm.runInContext("samplesFor('noise')[101]", c));
  document.hidden = true;
  docEvents.visibilitychange.forEach(f => f());
  assert.equal(contexts.at(-1).state, 'closed');

  const promise = vm.runInContext('playAudio()', c);
  vm.runInContext('stopAudio()', c);
  await promise;
  assert.equal(contexts.at(-1).starts, 0, 'stop during resume prevents playback');
  console.log('week06_sound_lab: finite tone/noise buffers, silent load, slide-stop, visibility-stop and startup race pass.');
})().catch(error => { console.error(error); process.exit(1); });
