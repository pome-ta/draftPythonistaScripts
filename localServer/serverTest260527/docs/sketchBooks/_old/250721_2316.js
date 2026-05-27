const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let osc;

  const baseFreq = 440;

  p.setup = () => {
    // put setup code here
    console.log(`top`);
    soundReset();

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);
    p.background(0, 0, 0.25);

    // sound
    osc = new p5.Oscillator();
    osc.setType('sine');
    const rFrq = baseFreq * p.random();
    osc.freq(baseFreq + rFrq);
    osc.amp(0.4);
    osc.start();

    window._cacheSounds = [osc];
    console.log(`end`);
  };

  p.draw = () => {
    // put drawing code here
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };

  function soundReset() {
    const actx = p.getAudioContext();
    const gain = p.soundOut.output.gain;
    console.log(`0: ${gain.value}`);
    const defaultValue = gain.defaultValue;

    const msBuf = 500;
    //33  // 30fps

    //const setTime = actx.currentTime + (msBuf / 1000);
    const timeWait = (ms) => actx.currentTime + ms / 1000;
    gain.exponentialRampToValueAtTime(-1.0, timeWait(msBuf));

    const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    wait(msBuf)
      .then(() => {
        console.log(`1: ${gain.value}`);
        window._cacheSounds?.forEach((s) => {
          s.stop();
          s.disconnect();
        });
        return wait(msBuf + 1);
      })
      .then(() => {
        console.log(`2: ${gain.value}`);
        gain.exponentialRampToValueAtTime(defaultValue, timeWait(msBuf));
      });

    console.log(`3: ${gain.value}`);

    p.userStartAudio();
  }
};

new p5(sketch);
