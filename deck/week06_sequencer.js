const W = 1000, H = 600;
const pitches = [261.63, 329.63, 392, 493.88];
let grid = [[1,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0],
            [0,1,0,1,0,1,0,1],[0,0,0,1,0,0,0,1]];
let ctx = null, running = false, starting = false, generation = 0, bpm = 100, step = -1;
let nextTime = 0, timer = null;
function setup() { createCanvas(W,H); textFont('monospace'); }
function draw() {
  background(255); noStroke(); fill(0,11,28); textSize(25);
  text('A written score: click cells to change the rule',40,42);
  textSize(18);
  for(let c=0;c<8;c++) text(c+1,95+c*110,105);
  for(let r=0;r<4;r++) text(['C4','E4','G4','B4'][r],15,160+r*80);
  for(let r=0;r<4;r++) for(let c=0;c<8;c++) {
    fill(grid[r][c] ? '#246E70' : '#EAF2F2');
    rect(60+c*110,120+r*80,96,65,5);
    if(c===step && running) { noFill(); stroke('#ED6D24');
      strokeWeight(4); rect(60+c*110,120+r*80,96,65,5); noStroke(); }
  }
  fill('#000B1C'); rect(60,470,170,55,5);
  fill(255); text(running?'STOP':'PLAY',100,507);
  fill('#000B1C'); text(bpm+' BPM',285,507);
  text('click here: slower     faster',460,507);
  textSize(18); text('Quiet start. Escape stops. No microphone or recording.',60,566);
}
function schedule() {
  if(!running || !ctx) return;
  while(nextTime < ctx.currentTime + 0.12) {
    step=(step+1)%8;
    for(let r=0;r<4;r++) if(grid[r][step]) {
      const o=ctx.createOscillator(),g=ctx.createGain();
      o.type='sine'; o.frequency.value=pitches[r];
      g.gain.setValueAtTime(0,nextTime);
      g.gain.linearRampToValueAtTime(0.035,nextTime+0.01);
      g.gain.exponentialRampToValueAtTime(0.0001,nextTime+0.22);
      o.connect(g);g.connect(ctx.destination);o.start(nextTime);o.stop(nextTime+0.24);
    }
    nextTime+=60/bpm/2;
  }
}
function stopAudio() {
  generation++; running=false; starting=false; clearInterval(timer);timer=null;
  if(ctx) {ctx.close();ctx=null;} step=-1;
}
async function mousePressed() {
  if(mouseY>=120 && mouseY<440 && mouseX>=60 && mouseX<940) {
    const r=floor((mouseY-120)/80),c=floor((mouseX-60)/110);
    if(r<4 && c<8) grid[r][c]=1-grid[r][c];return;
  }
  if(mouseY>=470 && mouseY<=525) {
    if(mouseX>=60 && mouseX<230) {
      if(running || starting) {stopAudio();return;}
      starting=true; const token=++generation;
      try {
        ctx=new (window.AudioContext || window.webkitAudioContext)();
        const local=ctx; await local.resume();
        if(generation!==token || ctx!==local || local.state==='closed') return;
        running=true;nextTime=ctx.currentTime+0.03;
        schedule();timer=setInterval(schedule,25);
      } catch(error) {
        if(generation===token) stopAudio();
        console.error('Audio could not start',error);
      } finally {if(generation===token) starting=false;}
    } else if(mouseX>=460 && mouseX<950) bpm=constrain(bpm+(mouseX<700?-10:10),40,180);
  }
}
function keyPressed() { if(keyCode===27) stopAudio(); }
window.addEventListener('keydown',e=>{
  if(e.key==='Escape') {stopAudio();e.preventDefault();e.stopImmediatePropagation();}
},true);
document.addEventListener('visibilitychange',()=>{if(document.hidden) stopAudio();});
window.addEventListener('pagehide',stopAudio);
window.addEventListener('message',e=>{
  if(e.source===window.parent && e.data==='slide:stop') stopAudio();
});
