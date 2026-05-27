const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let osc;

  const baseFreq = 440;

  p.setup = () => {
    // put setup code here
    soundReset();

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);
    //p.background(p.frameCount % v, 1, 0.25);
    p.background(0, 0, 0.25);

    // sound
    osc = new p5.Oscillator();
    osc.setType('sine');
    const rFrq = baseFreq * p.random();
    osc.freq(baseFreq + rFrq);
    osc.amp(0.4);
    osc.start();

    window._cacheSounds = [osc];

    //console.log(p.soundOut.output.gain)
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
    let currentTime;
    const buf = 2; // 30fps
    const actx = p.getAudioContext();

    //const output = p.soundOut.output;
    //const defaultValue = output.gain.defaultValue

    const gain = p.soundOut.output.gain;
    const defaultValue = gain.defaultValue;

    const setTime = actx.currentTime + buf;
    gain.exponentialRampToValueAtTime(-1.0, setTime);
    //gain.exponentialRampToValueAtTime(-1.0, actx.currentTime);

    //console.log(gain)
    window._cacheSounds?.forEach((s) => {
      s.stop(buf);
      s.disconnect();
    });

    gain.exponentialRampToValueAtTime(defaultValue, setTime + buf);

    p.userStartAudio();
  }
};

new p5(sketch);
