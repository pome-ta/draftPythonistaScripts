// すぺあな
class GridAndLabels {
  #p;

  #fft;
  #nyquist;
  #bandWidth;

  #labelsLayer;
  #gridLayer;
  #spectrumLayer;

  #labelsSize;
  #labelsPosition;
  #gridSize;
  #gridPosition;

  constructor(mainInstance, isLinear = false) {
    this.#p = mainInstance;
    this.#fft = null;

    this.#labelsLayer = null;
    this.#gridLayer = null;
    this.#spectrumLayer = null;
    this.isLinear = isLinear;

    this.ratio = 0.92;

    this.minDb = -60;
    this.maxDb = +6;
    this.dbStep = 6;
  }

  setup(fft) {
    this.#fft = fft;
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
    this.#spectrumLayer.vertex(0, gh);
    // 今後break するかも?で、`for`
    for (const [index, amplitude] of Object.entries(spectrum)) {
      const bin = index * this.#bandWidth;

      const x = this.#p.map(
        Math.log10(bin ? bin : 1e-8),
        Math.log10(this.#bandWidth),
        Math.log10(this.#nyquist),
        0,
        gw
      );

      const amplitudeRatio = amplitude / 255;
      const logDb = 20 * Math.log10(amplitudeRatio || 1e-10);
      const y = this.#p.map(logDb, this.minDb, this.maxDb, gh, 0);
      //const y = this.#p.map(amplitude, 0, 225, gh, 0);

      this.#spectrumLayer.vertex(x, y);
      //this.#spectrumLayer.curveVertex(x, y);
    }
    this.#spectrumLayer.vertex(gw, gh);
    this.#spectrumLayer.endShape();
    this.#p.image(this.#spectrumLayer, ...this.#gridPosition);
  }

  #setLabelsLayer() {
    this.#labelsLayer.clear();
    const [w, h] = this.#labelsSize;
    const [x, y] = this.#labelsPosition;

    //this.#labelsLayer.fill(0, 255, 255);
    //this.#labelsLayer.rect(0, 0, w, h);
  }

  #setGridLayer() {
    this.#gridLayer.clear();
    const [pgw, pgh] = this.#gridSize;
    const [pgx, pgy] = this.#gridPosition;
    //this.#gridLayer.fill(255, 0, 255);
    //this.#gridLayer.rect(0, 0, pgw, pgh);

    /* 
      log スケールとlinear スケールの切り替え？
    */

    const minFreq = this.#bandWidth;
    const maxFreq = this.#nyquist;

    const minLog = Math.log10(minFreq);
    const maxLog = Math.log10(maxFreq);

    const decades = Array.from(
      { length: Math.floor(maxLog) - Math.floor(minLog) + 1 },
      (_, d) => d + Math.floor(minLog)
    );

    const ticks = [...Array(9)].map((_, i) => i + 1);

    decades.forEach((d) => {
      ticks.forEach((i) => {
        const freq = i * 10 ** d;
        if (freq < minFreq || freq > maxFreq) {
          return;
        }

        const x = this.#p.map(Math.log10(freq), minLog, maxLog, 0, pgw);
        const isMajor = i === 1;
        if (isMajor) {
          console.log(freq);
        }

        this.#gridLayer.stroke(isMajor ? 100 : 50);
        this.#gridLayer.strokeWeight(isMajor ? 1 : 0.5);
        this.#gridLayer.line(x, 0, x, pgh);
      });
    });

    const dbTicks = Array.from(
      { length: Math.floor((this.maxDb - this.minDb) / this.dbStep) + 1 },
      (_, i) => this.minDb + i * this.dbStep
    );

    dbTicks.forEach((db) => {
      const y = this.#p.map(db, this.minDb, this.maxDb, pgh, 0);
      const isMajor = db % 12 === 0;

      this.#gridLayer.stroke(isMajor ? 100 : 50);
      this.#gridLayer.strokeWeight(db === 0 ? 2 : isMajor ? 2 : 0.1);
      this.#gridLayer.line(0, y, pgw, y);
    });
  }

  get #sampleRate() {
    return this.#p.sampleRate();
  }

  #setBaseGraphics() {
    this.#nyquist = this.#sampleRate / 2;
    this.#bandWidth = this.#nyquist / this.#fft.bins;

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
      this.#gridLayer.width,
      this.#gridLayer.height
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
  const baseFreq = 220;

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
    osc.setType(types[3]);
    const rFrq = baseFreq * p.random();
    // osc.freq(baseFreq + rFrq);
    osc.freq(baseFreq);
    osc.amp(0.5);
    osc.start();

    /*
    lfo = new p5.Oscillator(0.1, types[0]); // 速さ
    lfo.amp(440); // 幅
    lfo.start();
    lfo.disconnect();
    lfo.connect(osc.freqNode);
    */

    window._cacheSounds = [osc, lfo];

    gridGraph.setup(fft);
    //p.frameRate(10);
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
