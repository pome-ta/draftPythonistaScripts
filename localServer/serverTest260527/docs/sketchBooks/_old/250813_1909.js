// `soundReset` の改善

const spectrumAnalyzerPath = '../../sketchBooks/modules/spectrumAnalyzer.js';
const interactionTraceKitPath =
  '../../sketchBooks/modules/interactionTraceKit.js';

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let SpectrumAnalyzer;
  let pointerTracker;
  let tapIndicator;

  let osca;
  let lfo;
  let oscb;

  p.preload = () => {
    p.loadModule(spectrumAnalyzerPath, (m) => {
      const SpectrumAnalyzer = m.default;
      spectrumAnalyzer = new SpectrumAnalyzer(p);
    });
    p.loadModule(interactionTraceKitPath, (m) => {
      const { PointerTracker, TapIndicator } = m;
      pointerTracker = new PointerTracker(p);
      tapIndicator = new TapIndicator(p);
    });
  };

  p.setup = () => {
    // put setup code here
    soundReset();

    p.canvas.addEventListener(pointerTracker.move, (e) => e.preventDefault(), {
      passive: false,
    });

    p.createCanvas(w, h);
    p.colorMode(p.HSL, 1, 1, 1);

    bgColor = [0, 0, 0.25];
    p.background(...bgColor);

    fft = new p5.FFT();

    spectrumAnalyzer.setup(fft);
    //tapIndicator.setup();

    // sound
    const types = ['sine', 'triangle', 'sawtooth', 'square'];

    osca = new p5.Oscillator(types[0], 440 + p.random() * 440);
    osca.aname = 'a';

    //osc.amp(0.4);
    //osca.start();

    lfo = new p5.Oscillator(0.3, 'sine'); // 速さ
    lfo.amp(500); // 幅
    lfo.start();
    osca.start();
    lfo.disconnect();
    lfo.connect(osca.freqNode);

    oscb = new p5.Oscillator(types[1], 880 + p.random() * 440);
    oscb.aname = 'b';
    oscb.amp(0.4);
    oscb.start();

    window._cacheSounds = [osca, lfo, oscb];
  };

  p.draw = () => {
    // put drawing code here
    p.background(...bgColor);

    const spectrum = fft.analyze();
    spectrumAnalyzer.drawSpectrum(spectrum);
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };

  function soundReset() {
    const actx = p.getAudioContext();
    //dispose
    console.log(p.soundOut.soundArray);

    const soundArray = p.soundOut.soundArray;
    //console.log(p.soundOut);

    //console.log(p.soundOut);
    //console.log(actx)
    //console.log(p)
    //console.log(p5)

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
