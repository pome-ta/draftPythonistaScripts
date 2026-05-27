const title = '編集後に指定した音を出す';

const v = 360;
const frq = 440;
let toneOsc;

function setup() {
  createCanvas(v, v);
  colorMode(HSL, v, 1, 1);
  // sound init
  window._cacheSounds?.forEach((s) => {
    s.stop();
    s.disconnect();
  });

  const mFrq = Math.trunc(
    frq + frq * (0.5 - Math.trunc(random() * 1000) * 0.001)
  );

  toneOsc = new p5.SinOsc(mFrq);
  // toneOsc = new p5.TriOsc(mFrq);
  // toneOsc = new p5.SawOsc(mFrq);
  // toneOsc = new p5.SqrOsc(mFrq);

  const oscTypes = new Map([
    ['sine', 0.5],
    ['triangle', 0.4],
    ['sawtooth', 0.3],
    ['square', 0.2],
  ]);

  //toneOsc.amp(0.1);
  oscTyoe = toneOsc.getType();
  toneOsc.amp(oscTypes.get(oscTypes));

  toneOsc.start();

  window._cacheSounds = [toneOsc];
}

function draw() {
  background(frameCount % v, 1, 0.5);
}
