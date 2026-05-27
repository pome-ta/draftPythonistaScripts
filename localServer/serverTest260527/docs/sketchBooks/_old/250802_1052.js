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

    // todo: マージン設定方法要検討
    this.ratio = 0.96;

    // todo: どこで定義するか要検討
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

    const [pgw, pgh] = this.#gridSize;
    const [pgx, pgy] = this.#gridPosition;

    this.#spectrumLayer.noFill();
    this.#spectrumLayer.beginShape();
    this.#spectrumLayer.vertex(0, pgh);
    // 今後break するかも?で、`for`
    for (const [index, amplitude] of Object.entries(spectrum)) {
      const bin = index * this.#bandWidth;

      const x = this.#p.map(
        Math.log10(bin ? bin : 1e-8),
        Math.log10(this.#bandWidth),
        Math.log10(this.#nyquist),
        0,
        pgw
      );

      const amplitudeRatio = amplitude / 255;
      const logDb = 20 * Math.log10(amplitudeRatio || 1e-10);
      const y = this.#p.map(logDb, this.minDb, this.maxDb, pgh, 0);
      //const y = this.#p.map(amplitude, 0, 225, gh, 0);

      this.#spectrumLayer.vertex(x, y);
    }
    this.#spectrumLayer.vertex(pgw, pgh);
    this.#spectrumLayer.endShape();
    this.#p.image(this.#spectrumLayer, ...this.#gridPosition);
  }

  get #sampleRate() {
    return this.#p.sampleRate();
  }

  #createBase() {
    this.#labelsLayer.clear();
    this.#gridLayer.clear();

    const [lw, lh] = this.#labelsSize;
    const [lx, ly] = this.#labelsPosition;
    const [gw, gh] = this.#gridSize;
    const [gx, gy] = this.#gridPosition;

    /*
    this.#labelsLayer.fill(255, 0, 255);
    this.#labelsLayer.rect(0, 0, lw, lh);
    
    this.#gridLayer.fill(0, 255, 255);
    this.#gridLayer.rect(0, 0, gw, gh);
    */

    const xDistance = (lw - gw) / 2;
    const yDistance = (lh - gh) / 2;

    this.#labelsLayer.textFont('monospace');
    this.#labelsLayer.textSize(8);
    this.#labelsLayer.fill(255);

    // xxx: ここの変数は、別で`this.` として取り回せるはず
    const minFreq = this.#bandWidth;
    const maxFreq = this.#nyquist;

    const minLog = Math.log10(minFreq);
    const maxLog = Math.log10(maxFreq);

    // x: hz
    const decades = Array.from(
      { length: Math.floor(maxLog) - Math.floor(minLog) + 1 },
      (_, d) => d + Math.floor(minLog)
    );

    const ticks = [...Array(9)].map((_, i) => i + 1);

    const digits = Math.floor(Math.log10(minFreq));
    // 20hz 用
    const minimumFreq = Math.floor(minFreq / 10 ** digits) * 10 ** digits;

    decades.forEach((d, idx) => {
      ticks.forEach((i) => {
        const freq = i * 10 ** d;

        if (freq < minimumFreq || freq >= maxFreq) {
          return;
        }

        const x = this.#p.map(Math.log10(freq), minLog, maxLog, 0, gw);
        const isMajor = i === 1;

        //BOTTOM
        if (i % 2 === 0 || isMajor) {
          this.#gridLayer.stroke(isMajor ? 100 : 50);
          this.#gridLayer.strokeWeight(isMajor ? 1 : 0.8);

          isMajor
            ? this.#labelsLayer.textAlign(this.#p.CENTER, this.#p.TOP)
            : this.#labelsLayer.textAlign(this.#p.CENTER, this.#p.BOTTOM);
          const ty = isMajor ? lh - yDistance : lh;
          this.#labelsLayer.text(
            freq >= 1000 ? `${freq / 1000}k` : `${freq}`,
            x + xDistance,
            ty
          );
        } else {
          this.#gridLayer.stroke(25);
          this.#gridLayer.strokeWeight(0.4);
        }

        this.#gridLayer.line(x, 0, x, gh);
      });
    });

    // y: db
    const dbTicks = Array.from(
      { length: Math.floor((this.maxDb - this.minDb) / this.dbStep) + 1 },
      (_, i) => this.minDb + i * this.dbStep
    );

    this.#labelsLayer.textAlign(this.#p.RIGHT, this.#p.CENTER);
    //this.#labelsLayer.textAlign(this.#p.LEFT, this.#p.CENTER);
    dbTicks.forEach((db) => {
      if (db <= this.minDb || db >= this.maxDb) {
        return;
      }
      const y = this.#p.map(db, this.minDb, this.maxDb, gh, 0);
      const isMajor = db % 12 === 0;

      this.#gridLayer.stroke(isMajor ? 100 : 50);
      this.#gridLayer.strokeWeight(db === 0 ? 2 : isMajor ? 1 : 0.8);
      this.#gridLayer.line(0, y, gw, y);
      this.#labelsLayer.text(`${db}`, lw, y + yDistance);
    });
  }

  #setBaseGraphics() {
    this.#nyquist = this.#sampleRate / 2;
    this.#bandWidth = this.#nyquist / this.#fft.bins;

    this.#setSize();
    this.#createBase();
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
  const baseFreq = 1000;

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
