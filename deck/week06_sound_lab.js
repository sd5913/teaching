// Finite Web Audio examples. The drawn samples are the exact buffer sent to playback.
const W = 1600, H = 600, RATE = 22050, COUNT = 2 * RATE;
let mode = 'tone', ctx = null, source = null;
let running = false, starting = false, generation = 0;

function samplesFor(kind) {
  const samples = new Float32Array(COUNT);
  let seed = 7;
  for (let i = 0; i < COUNT; i++) {
    if (kind === 'tone') {
      samples[i] = 0.08 * Math.sin(2 * Math.PI * 220 * i / RATE);
    } else {
      seed ^= seed << 13;
      seed ^= seed >>> 17;
      seed ^= seed << 5;
      samples[i] = ((seed >>> 0) / 4294967296 * 2 - 1) * 0.08;
    }
    const edge = Math.min(1, i / (RATE * 0.01), (COUNT - 1 - i) / (RATE * 0.01));
    samples[i] *= edge;
  }
  return samples;
}

function setup() { createCanvas(W, H); textFont('monospace'); }
function draw() {
  background(255);
  noStroke(); fill('#000B1C'); textSize(34);
  text('THE SAME CLOCK. TWO RULES FOR THE NUMBERS.', 70, 52);
  textSize(26);
  text(mode === 'tone' ? 'TONE / 220 cycles per second' : 'NOISE / seeded random values', 70, 100);
  text('First 20 ms (including the fade-in)', 820, 100);
  stroke('#CCDADA'); strokeWeight(2);
  line(70, 250, 1530, 250);
  for (let ms = 0; ms <= 20; ms += 5) {
    const x = 70 + ms / 20 * 1460;
    line(x, 130, x, 370);
    noStroke(); fill('#5C6470'); textSize(22); text(ms + ' ms', x - 20, 402);
    stroke('#CCDADA');
  }
  const values = samplesFor(mode);
  stroke('#246E70'); strokeWeight(3); noFill(); beginShape();
  for (let i = 0; i <= RATE * 0.02; i += 2) {
    vertex(70 + i / (RATE * 0.02) * 1460, 250 - values[i] / 0.08 * 95);
  }
  endShape();
  noStroke(); fill('#000B1C'); textSize(28);
  text('22,050 samples/s  |  44,100 samples  |  2 seconds', 70, 455);
  const buttons = [[70, 245, running || starting ? 'STOP' : 'PLAY 2 s'],
    [340, 245, 'TONE'], [610, 245, 'NOISE']];
  for (const [x, width, label] of buttons) {
    fill(label === 'NOISE' && mode === 'noise' || label === 'TONE' && mode === 'tone' ? '#246E70' : '#000B1C');
    rect(x, 480, width, 66, 6); fill(255); textSize(27); text(label, x + 28, 523);
  }
}

function stopAudio() {
  generation++;
  running = false; starting = false;
  if (source) {
    source.onended = null;
    try { source.stop(); } catch (_) { /* Already ended. */ }
    source = null;
  }
  if (ctx) { ctx.close(); ctx = null; }
}

async function playAudio() {
  if (running || starting) return;
  starting = true;
  const token = ++generation;
  try {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    const local = ctx;
    await local.resume();
    if (token !== generation || ctx !== local || local.state === 'closed') return;
    const buffer = local.createBuffer(1, COUNT, RATE);
    buffer.copyToChannel(samplesFor(mode), 0);
    source = local.createBufferSource();
    source.buffer = buffer;
    source.connect(local.destination);
    source.onended = () => {
      if (token === generation && source) stopAudio();
    };
    source.start();
    running = true;
  } catch (error) {
    if (token === generation) stopAudio();
    console.error('Audio could not start', error);
  } finally {
    if (token === generation) starting = false;
  }
}

function mousePressed() {
  if (mouseY < 480 || mouseY > 546) return;
  if (mouseX >= 70 && mouseX < 315) {
    if (running || starting) stopAudio(); else playAudio();
  } else if (mouseX >= 340 && mouseX < 585) {
    stopAudio(); mode = 'tone';
  } else if (mouseX >= 610 && mouseX < 855) {
    stopAudio(); mode = 'noise';
  }
  return false;
}
function keyPressed() { if (keyCode === 27) stopAudio(); }
window.addEventListener('keydown', e => {
  if (e.key === 'Escape') { stopAudio(); e.preventDefault(); e.stopImmediatePropagation(); }
}, true);
document.addEventListener('visibilitychange', () => { if (document.hidden) stopAudio(); });
window.addEventListener('pagehide', stopAudio);
window.addEventListener('message', e => {
  if (e.source === window.parent && e.data === 'slide:stop') stopAudio();
});
