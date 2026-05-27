const spectrumAnalyzerPath = '../../sketchBooks/modules/spectrumAnalyzer.js';

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

  let spectrumAnalyzer;

  p.preload = () => {
    p.loadModule(spectrumAnalyzerPath, (m) => {
      const SpectrumAnalyzer = m.default;
      spectrumAnalyzer = new SpectrumAnalyzer(p);
    });
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
    metrEnv.setRange(0.4, 0);

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

    kickTone = new p5.Oscillator(types[1]);
    kickTone.start();
    kickTone.amp(0.0);

    kickEnv = new p5.Envelope();
    kickEnv.setADSR(0.01, 0.2);
    //kickEnv.setRange(1, 0);

    kickPhrase = new p5.Phrase(
      'kick',
      (time, playbackRate) => {
        kickTone.freq(330);
        kickTone.amp(0);

        kickTone.freq(32, 0.5);
        kickEnv.play(kickTone);
      },
      [
        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0,

        1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0,
      ]
    );

    part = new p5.Part();
    part.setBPM(BPM);
    // part.addPhrase(metrPhrase);
    part.addPhrase(kickPhrase);

    part.loop();

    window._cacheSounds = [kickTone, kickEnv, metrTone, metrEnv, part];

    spectrumAnalyzer.setup(fft);
    //p.frameRate(10);
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
