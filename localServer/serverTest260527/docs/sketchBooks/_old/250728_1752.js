// すぺあな
class GridAndLabels {
  #p;
  #labelsLayer;
  #gridLayer;
  #spectrumLayer;

  #labelsSize;
  #labelsPosition;
  #gridSize;
  #gridPosition;

  constructor(mainInstance) {
    this.#p = mainInstance;
    this.#labelsLayer = null;
    this.#gridLayer = null;
    this.#spectrumLayer = null;

    this.ratio = 0.92;
  }

  setup(fft) {
    /*
    const bandWidth = this.#sampleRate / 2 / fft.bins;
    //const hzPerBinList = Array.from({ length: fft.bins }, (_, idx) => idx * bandWidth);
    const hzPerBinList = Array.from({ length: fft.bins }, (_, idx) => {
      let a = idx * bandWidth;
      return 1;
    });
    console.log(this.#sampleRate);
    console.log(hzPerBinList);
    */

    const maxHz = this.#sampleRate / 2;
    //const divHz =
    const xSteps = [200, 400, 440, 500, 800, 880];
    //this.xGrids =

    this.#setBaseGraphics();
    this.#useWindowResized();
  }

  drawSpectrum(spectrum) {
    this.#drawBaseGraphics();
    this.#spectrumLayer.clear();

    const [gw, gh] = this.#gridSize;
    const [gx, gy] = this.#gridPosition;

    this.#spectrumLayer.noFill();
    this.#spectrumLayer.beginShape();
    this.#spectrumLayer.vertex(gx, gh);
    // 今後break するかも?で、`for`
    for (const [index, amplitude] of Object.entries(spectrum)) {
      const x = this.#p.map(index, 0, spectrum.length, gx, gw);
      const y = this.#p.map(amplitude, 0, 255, gh, gy);
      this.#spectrumLayer.vertex(x, y);
    }
    this.#spectrumLayer.vertex(gw, gh);
    this.#spectrumLayer.endShape();
    this.#p.image(this.#spectrumLayer, ...this.#gridPosition);
  }

  #setLabelsLayer() {
    this.#labelsLayer.clear();
    const [w, h] = this.#labelsSize;
    const [x, y] = this.#labelsPosition;

    this.#labelsLayer.fill(0, 255, 255);
    this.#labelsLayer.rect(0, 0, w, h);
  }

  #setGridLayer() {
    this.#gridLayer.clear();
    const [pgw, pgh] = this.#gridSize;
    const [pgx, pgy] = this.#gridPosition;
    this.#gridLayer.fill(255, 0, 255);
    this.#gridLayer.rect(0, 0, pgw, pgh);

    /* 440hz に線を引く
      リニアで
    */
    const maxHz = this.#sampleRate / 2;
    const tHzs = [110, 220, 440, 880];
    //const tHz = 880;
    this.#gridLayer.stroke(0, 255, 0);
    this.#gridLayer.strokeWeight(0.5);
    tHzs.forEach((tHz) => {
      const hz = this.#p.map(tHz, 0, maxHz, 0, 255);
      const x = this.#p.map(hz, 0, 255, pgx, pgw);
      this.#gridLayer.line(x, 0, x, pgh);
    });

    //console.log(hz);
    //console.log(x);
  }

  get #sampleRate() {
    return this.#p.sampleRate();
  }

  #setBaseGraphics() {
    this.#setSize();
    this.#setLabelsLayer();
    this.#setGridLayer();
    this.#drawBaseGraphics();
  }

  #drawBaseGraphics() {
    const [lx, ly] = this.#labelsPosition;
    const [gx, gy] = this.#gridPosition;
    this.#p.image(this.#labelsLayer, ...this.#labelsPosition);
    this.#p.image(this.#gridLayer, ...this.#gridPosition);
  }

  #setSize() {
    this.#labelsLayer && this.#labelsLayer.remove();
    this.#gridLayer && this.#gridLayer.remove();
    this.#spectrumLayer && this.#spectrumLayer.remove();

    this.#labelsLayer = this.#p.createGraphics(
      this.#p.windowWidth * this.ratio,
      this.#p.windowHeight * this.ratio
    );

    this.#gridLayer = this.#p.createGraphics(
      this.#labelsLayer.width * this.ratio,
      this.#labelsLayer.height * this.ratio
    );

    this.#spectrumLayer = this.#p.createGraphics(
      this.#labelsLayer.width * this.ratio,
      this.#labelsLayer.height * this.ratio
    );

    this.#labelsSize = [this.#labelsLayer.width, this.#labelsLayer.height];
    this.#labelsPosition = [
      (this.#p.windowWidth - this.#labelsLayer.width) / 2,
      (this.#p.windowHeight - this.#labelsLayer.height) / 2,
    ];

    this.#gridSize = [this.#gridLayer.width, this.#gridLayer.height];
    this.#gridPosition = [
      (this.#p.windowWidth - this.#gridLayer.width) / 2,
      (this.#p.windowHeight - this.#gridLayer.height) / 2,
    ];
  }

  #useWindowResized() {
    const instance = this;
    const originalFunction =
      instance.#p.windowResized === void 0
        ? (e) => {}
        : instance.#p.windowResized;
    instance.#p.windowResized = function (...args) {
      const result = originalFunction.apply(this, args);
      instance.#setBaseGraphics();
      return result;
    };
  }
}

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;
  let bgColor;

  let osc, lfo;
  let fft;
  const baseFreq = 440;

  const gridGraph = new GridAndLabels(p);

  p.setup = () => {
    // put setup code here
    soundReset();

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);

    bgColor = [0, 0, 0.25];
    p.background(...bgColor);

    fft = new p5.FFT();
    // sound
    const types = ['sine', 'triangle', 'sawtooth', 'square'];
    osc = new p5.Oscillator();
    osc.setType(types[0]);
    const rFrq = baseFreq * p.random();
    // osc.freq(baseFreq + rFrq);
    osc.freq(baseFreq);
    osc.amp(0.5);
    osc.start();

    lfo = new p5.Oscillator(0.1, types[0]); // 速さ
    lfo.amp(440); // 幅
    lfo.start();
    lfo.disconnect();
    lfo.connect(osc.freqNode);

    window._cacheSounds = [osc, lfo];

    gridGraph.setup(fft);
  };

  p.draw = () => {
    // put drawing code here
    p.background(...bgColor);
    const spectrum = fft.analyze();
    gridGraph.drawSpectrum(spectrum);
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };

  function soundReset() {
    // const actx = p.getAudioContext();
    const gain = p.soundOut.output.gain;
    const defaultValue = gain.defaultValue;
    // todo: クリップノイズ対策
    gain.value = -1;
    window._cacheSounds?.forEach((s) => {
      s?.stop();
      s?.disconnect();
    });

    gain.value = defaultValue;
    p.userStartAudio();
  }
};

new p5(sketch);
