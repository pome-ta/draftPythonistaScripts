//import { Engine } from "https://esm.sh/@babylonjs/core/Engines/engine";
/*
(async() => {
  const { dayjs } = await import("https://esm.sh/dayjs");
  console.log(dayjs)
})();
*/
const dayjsURLPath = 'https://esm.sh/dayjs';
let dayjs;

let noise2D;
//console.log(window);

// Metronom
class GridAndLabels {
  #p;

  #fft;
  #minFreq;
  #maxFreq;

  #labelsLayer;
  #gridLayer;
  #spectrumLayer;

  #labelsSize;
  #labelsPosition;
  #gridSize;
  #gridPosition;

  #xyListOld;

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

    this.#xyListOld = [];
  }

  get #sampleRate() {
    return this.#p.sampleRate();
  }

  setup(fft) {
    this.#fft = fft;
    this.#setBaseGraphics();
    this.#useWindowResized();
  }

  drawSpectrum(spectrum) {
    this.#drawBaseGraphics();

    if (this.#p.frameCount % 9 !== 0) {
      // 描画悪あがき
      this.#p.image(this.#spectrumLayer, ...this.#gridPosition);
      return;
    }

    this.#spectrumLayer.clear();

    const [pgw, pgh] = this.#gridSize;
    const [pgx, pgy] = this.#gridPosition;

    const xyList = spectrum.map((amplitude, index) => {
      const bin = index * this.#minFreq;

      const x = this.#p.map(
        Math.log10(bin ? bin : 1e-12),
        Math.log10(this.#minFreq),
        Math.log10(this.#maxFreq),
        0,
        pgw
      );

      const amplitudeRatio = amplitude / 255;
      const logDb = 20 * Math.log10(amplitudeRatio || 1e-10);
      const y = this.#p.map(logDb, this.minDb, this.maxDb, pgh, 0);
      return [x, y];
    });

    // xxx: 今後の場合分け用？

    //this.#spectrumLayer.noFill();
    this.#spectrumLayer.noStroke();
    this.#spectrumLayer.fill(0, 255, 255, 64);
    this.#spectrumLayer.beginShape();
    this.#spectrumLayer.vertex(0, pgh);

    [...xyList].forEach((xy) => {
      this.#spectrumLayer.vertex(...xy);
    });

    this.#spectrumLayer.vertex(pgw, pgh);
    this.#spectrumLayer.endShape();

    this.#spectrumLayer.noFill();
    if (this.#xyListOld?.length) {
      this.#spectrumLayer.stroke(255, 0, 255, 192);
      this.#spectrumLayer.beginShape();
      //this.#spectrumLayer.vertex(0, pgh);

      [...this.#xyListOld].forEach((xy) => {
        this.#spectrumLayer.vertex(...xy);
      });

      //this.#spectrumLayer.vertex(pgw, pgh);
      this.#spectrumLayer.endShape();
    }

    this.#spectrumLayer.stroke(0, 255, 255, 192);
    this.#spectrumLayer.beginShape();
    //this.#spectrumLayer.vertex(0, pgh);

    [...xyList].forEach((xy) => {
      this.#spectrumLayer.vertex(...xy);
    });

    //this.#spectrumLayer.vertex(pgw, pgh);
    this.#spectrumLayer.endShape();

    this.#xyListOld = xyList;
    this.#p.image(this.#spectrumLayer, ...this.#gridPosition);
  }

  #createBase() {
    this.#labelsLayer.clear();
    this.#gridLayer.clear();

    const [lw, lh] = this.#labelsSize;
    const [lx, ly] = this.#labelsPosition;
    const [gw, gh] = this.#gridSize;
    const [gx, gy] = this.#gridPosition;

    const xDistance = (lw - gw) / 2;
    const yDistance = (lh - gh) / 2;

    const minLog = Math.log10(this.#minFreq);
    const maxLog = Math.log10(this.#maxFreq);

    // x: hz
    const decades = Array.from(
      { length: Math.floor(maxLog) - Math.floor(minLog) + 1 },
      (_, d) => d + Math.floor(minLog)
    );

    const ticks = [...Array(9)].map((_, i) => i + 1);

    const digits = Math.floor(Math.log10(this.#minFreq));
    // 20hz 用
    const minimumFreq = Math.floor(this.#minFreq / 10 ** digits) * 10 ** digits;

    this.#labelsLayer.textFont('monospace');
    this.#labelsLayer.textSize(8);
    this.#labelsLayer.fill(255);

    this.#labelsLayer.textAlign(this.#p.CENTER, this.#p.BOTTOM);
    decades.forEach((d, idx) => {
      ticks.forEach((i) => {
        const freq = i * 10 ** d;

        if (freq < minimumFreq || freq >= this.#maxFreq) {
          return;
        }

        const x = this.#p.map(Math.log10(freq), minLog, maxLog, 0, gw);
        const isMajor = i === 1;

        if (i % 2 === 0 || isMajor) {
          this.#gridLayer.stroke(isMajor ? 100 : 50);
          this.#gridLayer.strokeWeight(isMajor ? 1 : 0.8);

          const ty = isMajor ? gh + ly : lh - yDistance / 2;
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
    this.nyquist = this.#sampleRate / 2;
    this.bandWidth = this.nyquist / this.#fft.bins;

    this.#minFreq = this.bandWidth;
    this.#maxFreq = this.nyquist;

    this.#setSize();
    this.#createBase();
    this.#drawBaseGraphics();
  }

  #drawBaseGraphics() {
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

  const BPM = 98;
  let metrTone, metrEnv, metrPhrase;

  let kickTone, kickEnv, kickPhrase;
  let osc;

  let part;
  let phrase;
  let fft;

  const gridGraph = new GridAndLabels(p);

  p.preload = () => {
    console.log('p');
    //p.loadModule('dummy');

    p.loadModule(dayjsURLPath, (mod) => {
      dayjs = mod.default;
      console.log(dayjs);
    });

    /*
    p.loadModule(dayjsURLPath).then((m) => {
      dayjs = m.default;
      console.log(dayjs)
    })
    */

    //dayjs = p.loadModule(dayjsURLPath);

    /*
    import(dayjsURLPath).then((module) => {
      
      dayjs = module.default;
      //console.log(dayjs);
    }).then(()=>{
      console.log('then');
      console.log(dayjs);
    });
    */

    /*
    
    const { createNoise2D } = await import('https://cdn.jsdelivr.net/npm/simplex-noise@4.0.1/dist/esm/simplex-noise.js');
    */
    //noise2D = createNoise2D();
    //console.log(noise2D);

    //console.log(dayjs);
  };

  p.setup = () => {
    // put setup code here
    soundReset();

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);

    bgColor = [0, 0, 0.25];
    p.background(...bgColor);

    fft = new p5.FFT();

    const types = ['sine', 'triangle', 'sawtooth', 'square'];
    // metronom
    metrTone = new p5.Oscillator(types[1]);
    metrTone.start();
    metrTone.amp(0.0);

    metrEnv = new p5.Envelope();
    metrEnv.setADSR(0.001, 0.05, 0.01, 0.1);
    metrEnv.setRange(1, 0);

    metrPhrase = new p5.Phrase(
      'metr',
      (time, playbackRate) => {
        if (!playbackRate) {
          //metrTone.amp(0.0);
          return;
        }
        metrTone.freq(playbackRate);
        //metrTone.amp(1.0);
        metrEnv.play(metrTone);
      },
      [...Array(4)].flatMap((_, idx) => [
        idx ? 440 : 800,
        ...Array(3).fill(null),
      ])
    );

    // sound

    kickTone = new p5.Oscillator(types[0]);
    kickTone.start();
    kickTone.amp(0.0);

    kickEnv = new p5.Envelope(0.001, 0.1, 0, 0.2);
    kickEnv.setRange(1, 0);

    kickPhrase = new p5.Phrase(
      'kick',
      (time, playbackRate) => {
        kickTone.freq(220);
        kickTone.amp(0);

        kickTone.freq(24, 0.15);
        kickEnv.play(kickTone, 0, 0.01);
      },
      [
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 1, 0,
      ]
    );

    part = new p5.Part();
    part.setBPM(BPM);
    part.addPhrase(metrPhrase);
    part.addPhrase(kickPhrase);

    part.loop();

    window._cacheSounds = [kickTone, kickEnv, metrTone, metrEnv, part];

    gridGraph.setup(fft);
    p.frameRate(10);
    //console.log(noise2D);
    console.log('s');
    //dayjs.then(m=>console.log(m.format()))
    console.log(dayjs().format());
  };

  p.draw = () => {
    // put drawing code here
    //console.log(dayjs);
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
      s?.stop && s?.stop();
      s?.disconnect && s?.disconnect();
    });

    gain.value = defaultValue;
    p.userStartAudio();
  }
};

new p5(sketch);

/*
(async () => {
  dayjs = (await import(dayjsURLPath)).default;

  //console.log(dayjs().format()); // 現在日時のISO文字列
  //console.log(dayjs); // 現在日時のISO文字列
  new p5(sketch);
})();
*/

/*
import(dayjsURLPath).then((module) => {
  dayjs = module.default;
}).then(() => {
  new p5(sketch);
});

*/
