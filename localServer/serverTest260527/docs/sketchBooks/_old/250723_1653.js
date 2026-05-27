const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let osc;
  const baseFreq = 440;

  let fft;

  p.setup = () => {
    // put setup code here
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

    fft = new p5.FFT();
  };

  p.draw = () => {
    // put drawing code here
    p.background(0, 0, 0.25);

    const spectrum = fft.analyze();
    //p.noFill();
    p.beginShape();
    // 今後break したい為
    for (const [index, amplitude] of Object.entries(spectrum)) {
      const x = p.map(
        Math.log10(index),
        0,
        Math.log10(spectrum.length),
        0,
        w,
        true
      );
      const y = p.map(amplitude, 0, 255, h, 0);
      p.vertex(x, y);
    }
    //p.vertex(0, h);

    p.endShape();
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };

  function soundReset() {
    const actx = p.getAudioContext();
    const gain = p.soundOut.output.gain;
    const defaultValue = gain.defaultValue;
    // todo: クリップノイズ対策
    gain.value = -1;
    window._cacheSounds?.forEach((s) => {
      s.stop();
      s.disconnect();
    });

    gain.value = defaultValue;
    p.userStartAudio();
  }
};

new p5(sketch);
