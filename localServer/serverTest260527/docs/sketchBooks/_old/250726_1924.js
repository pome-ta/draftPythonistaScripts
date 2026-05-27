// リニアでやる

class GridAndLabels {
  #p;
  #labelsLayer;
  #gridLayer;

  constructor(mainInstance) {
    this.#p = mainInstance;
    this.#labelsLayer = null;
    this.#gridLayer = null;
  }

  setup() {
    const ratio = 0.92;
    let w = this.#p.windowWidth;
    let h = this.#p.windowHeight;

    this.#labelsLayer = this.#p.createGraphics(w * ratio, h * ratio);
    let lw = this.#labelsLayer.width;
    let lh = this.#labelsLayer.height;

    let lx = (w - lw) / 2;
    let ly = (h - lh) / 2;

    this.#gridLayer = this.#p.createGraphics(lw * ratio, lh * ratio);
    let gw = this.#gridLayer.width;
    let gh = this.#gridLayer.height;

    let gx = (w - gw) / 2;
    let gy = (h - gh) / 2;

    const nyquist = this.#p.sampleRate() / 2;
    const divStep = 10;

    console.log(nyquist / divStep);
    const xGridSteps = Array.from({ length: 220 }, (_, i) => 10 + i * 10);
    const xStepFirst = xGridSteps[0];
    const xStepLast = xGridSteps.slice(-1)[0];

    function getHighestDigit(n) {
      if (n === 0) {
        return 0;
      }
      const digits = Math.floor(Math.log10(n));
      return Math.floor(n / 10 ** digits);
    }

    this.#labelsLayer.textFont('monospace');
    this.#labelsLayer.textSize(8);
    this.#labelsLayer.fill(255);

    //this.#labelsLayer.textAlign(this.#p.CENTER, this.#p.CENTER);
    //this.#labelsLayer.textAlign(this.#p.RIGHT, this.#p.BOTTOM);
    this.#labelsLayer.textAlign(this.#p.CENTER, this.#p.BOTTOM);

    this.#gridLayer.strokeWeight(0.5);

    xGridSteps.forEach((hz, idx) => {
      // if (hz === xStepFirst || hz === xStepLast) {
      //   return;
      // }
      const x = this.#p.map(
        Math.log10(hz),
        Math.log10(xStepFirst),
        Math.log10(nyquist),
        0,
        gw
      );
      //const x = this.#p.map(hz, xStepFirst, xStepLast, 0, gw);
      if ((idx + 1) % 10 === 0) {
        //console.log(idx);
        this.#gridLayer.strokeWeight(1);
        this.#labelsLayer.text(`${hz}`, x + gx - lx, lh - gy);
      } else {
        this.#gridLayer.strokeWeight(0.5);
      }
      this.#gridLayer.line(x, 0, x, gh);
      // this.#labelsLayer.text(`${hz}`, x + gx - lx, lh - gy);
    });

    this.lPos = [lx, ly];
    this.lSize = [lw, lh];
    this.gPos = [gx, gy];
    this.gSize = [gw, gh];

    this.#p.image(this.#gridLayer, ...this.gPos);
    this.#p.image(this.#labelsLayer, ...this.lPos);
  }

  draw() {
    this.#p.image(this.#gridLayer, ...this.gPos);
    this.#p.image(this.#labelsLayer, ...this.lPos);
  }
}

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let osc;
  const baseFreq = 100;

  let fft;
  let lfo;
  let amp;
  let bgColor;
  let bgDrawColor;

  const pg = new GridAndLabels(p);
  let pgX, pgY, pgW, pgH;

  p.setup = () => {
    // put setup code here
    soundReset();

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);

    bgColor = [0, 0, 0.25];
    bgDrawColor = [...bgColor, 0.05];
    p.background(...bgColor);

    // sound
    const types = ['sine', 'triangle', 'sawtooth', 'square'];
    osc = new p5.Oscillator();
    osc.setType(types[0]);
    const rFrq = baseFreq * p.random();
    // osc.freq(baseFreq + rFrq);
    osc.freq(baseFreq);
    osc.amp(0.4);
    osc.start();

    // lfo = new p5.Oscillator(0.25, types[2]); // 速さ
    // lfo.amp(440); // 幅
    // lfo.start();

    // lfo.disconnect();
    // lfo.connect(osc.freqNode);

    window._cacheSounds = [osc /*lfo,*/];

    fft = new p5.FFT();
    amp = new p5.Amplitude();
    pg.setup();
    [pgX, pgY] = pg.gPos;
    [pgW, pgH] = pg.gSize;
  };

  p.draw = () => {
    // put drawing code here
    //p.blendMode(p.SCREEN);
    p.background(...bgColor);

    //p.blendMode(p.BLEND);

    const spectrum = fft.analyze();
    //console.log(amp.getLevel())
    //p.noFill();
    p.noStroke();
    p.fill(0.5, 0.8, 0.8, 0.3);
    p.beginShape();
    // 今後break したい為
    for (const [index, amplitude] of Object.entries(spectrum)) {
      const x = p.map(
        Math.log10(index),
        0,
        Math.log10(spectrum.length),
        pgX,
        pgW + pgX
      );

      //const db = 20 * Math.log10(amplitude === 0 ? 1e-8 : amplitude / 255);
      const db = amplitude > 0 ? 20 * Math.log10(amplitude / 255) : -60;
      const y = p.map(db, -60, 12, pgH + pgY, pgY);
      p.vertex(x, y);
    }
    p.vertex(pgX, pgH + pgY);
    p.endShape();

    pg.draw();
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
