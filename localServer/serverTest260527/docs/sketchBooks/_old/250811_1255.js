const spectrumAnalyzerPath = '../../sketchBooks/modules/spectrumAnalyzer.js';
const interactionTraceKitPath =
  '../../sketchBooks/modules/interactionTraceKit.js';

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;
  let bgColor;

  let spectrumAnalyzer;
  let pointerTracker;
  let tapIndicator;

  const BPM = 90;

  let fft;

  let osc;
  let env;
  let phrase;
  let part;

  // todo: `0` に近い、最小値として
  const zero = 1e-3 + 1e-4;

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
    tapIndicator.setup();

    // --- sound
    p.setBPM(BPM);

    const types = ['sine', 'triangle', 'sawtooth', 'square'];
    osc = new p5.Oscillator(types[0]);
    osc.start();
    osc.amp(0);

    env = new p5.Envelope();
    env.setADSR(zero, 0.1, 1, zero + zero);
    env.setExp(true);

    phrase = new p5.Phrase(
      'metronom',
      (time, playbackRate) => {
        if (!playbackRate) {
          return;
        }

        osc.freq(playbackRate);
        env.play(osc);
      },
      [880, 0, 0, 0, 440, 0, 0, 0, 440, 0, 0, 0, 440, 0, 0, 0]
    );

    part = new p5.Part();
    part.addPhrase(phrase);
    part.loop();

    window._cacheSounds = [osc, env, part];
  };

  p.draw = () => {
    // put drawing code here
    p.background(...bgColor);

    const spectrum = fft.analyze();
    spectrumAnalyzer.drawSpectrum(spectrum);
  };

  p.touchStarted = (e) => {};

  p.touchMoved = (e) => {};

  p.touchEnded = (e) => {};

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
