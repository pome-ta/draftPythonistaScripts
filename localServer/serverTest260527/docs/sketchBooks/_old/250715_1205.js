const title = '編集後に指定した音を出す';

const sketch = (p) => {
  let w, h;
  let setupWidth, setupHeight, setupRatio;

  let bgColor;

  const frq = 440;
  let toneOsc;
  let oscTyoe;
  let fft;

  p.setup = () => {
    // sound init
    window._cacheSounds?.forEach((s) => {
      s.stop();
      s.disconnect();
    });
    p.userStartAudio();

    // put setup code here

    windowFlexSize(true);
    p.colorMode(p.HSB, 1.0, 1.0, 1.0, 1.0);
    bgColor = p.color(0, 0, 64 / 255);
    p.background(bgColor);

    const mFrq = Math.trunc(
      frq + frq * (0.5 - Math.trunc(p.random() * 1000) * 0.001)
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

    fft = new p5.FFT();
    p.textAlign(p.CENTER, p.CENTER);
    p.textSize(32);

    window._cacheSounds = [toneOsc];
  };

  p.draw = () => {
    // put drawing code here
    p.background(bgColor);

    let spectrum = fft.analyze();
    p.noStroke();
    p.fill(0.2, 0.5, 0.8);
    for (let i = 0; i < spectrum.length; i++) {
      let x = p.map(i * 32, 0, spectrum.length, 0, p.width);
      let h = -p.height + p.map(spectrum[i], 0, 255, p.height, 0);
      p.rect(x, p.height, p.width / spectrum.length, h);
    }

    let waveform = fft.waveform();
    p.noFill();
    p.beginShape();
    p.stroke(0.8, 0.5, 0.8);
    for (let i = 0; i < waveform.length; i++) {
      let x = p.map(i, 0, waveform.length, 0, p.width);
      let y = p.map(waveform[i], -1, 1, 0, p.height);
      p.vertex(x, y);
    }
    p.endShape();

    p.noStroke();
    p.fill(0.0, 0.0, 0.8);

    p.text(`${oscTyoe}\n${toneOsc.f}`, p.width / 2, p.height / 2);
  };

  p.windowResized = (event) => {
    windowFlexSize(true);
  };

  function windowFlexSize(isFullSize = false) {
    const isInitialize =
      typeof setupWidth === 'undefined' || typeof setupHeight === 'undefined';

    [setupWidth, setupHeight] = isInitialize
      ? [p.width, p.height]
      : [setupWidth, setupHeight];

    const sizeRatio = 1;
    const windowWidth = p.windowWidth * sizeRatio;
    const windowHeight = p.windowHeight * sizeRatio;

    if (isFullSize) {
      w = windowWidth;
      h = windowHeight;
    } else {
      const widthRatio =
        windowWidth < setupWidth ? windowWidth / setupWidth : 1;
      const heightRatio =
        windowHeight < setupHeight ? windowHeight / setupHeight : 1;

      setupRatio = Math.min(widthRatio, heightRatio);
      w = setupWidth * setupRatio;
      h = setupHeight * setupRatio;
    }
    p.resizeCanvas(w, h);
  }
};

new p5(sketch);
//window._p5Instance = new p5(sketch);
