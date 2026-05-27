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

  const BPM = 90;

  let fft;

  let osc;
  let env;
  let phrase;
  let part;

  let osca;
  let lfo;
  let oscb;

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
    //tapIndicator.setup();

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

    //window._cacheSounds = [osca, lfo, oscb];
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
    //const actx = p.getAudioContext();
    //dispose
    p.disposeSound();
    /*
    p.soundOut.soundArray.forEach((s) => {
      s?.stop && s.stop();
      s?.dispose && s.dispose();
      s?.disconnect && s.disconnect();
    });
    */

    const soundArray = p.soundOut.soundArray;
    for (let soundIdx = soundArray.length - 1; soundIdx >= 0; soundIdx--) {
      const sound = soundArray[soundIdx];
      sound?.stop && sound.stop();
      sound?.dispose && sound.dispose();
      sound?.disconnect && sound.disconnect();

      soundArray.splice(soundIdx, 1);
    }

    p.soundOut.soundArray = [];
    /*
    p.soundOut.parts.forEach((p)=> {
      console.log(p)
      deldet 
    });
    */

    const parts = p.soundOut.parts;
    for (let partIdx = parts.length - 1; partIdx >= 0; partIdx--) {
      const phrases = parts[partIdx].phrases;
      for (let phraseIdx = phrases.length - 1; phraseIdx >= 0; phraseIdx--) {
        phrases.splice(phraseIdx, 1);
      }

      console.log(p.soundOut.parts[partIdx]);
      //delete p.soundOut.parts[partIdx];
      parts.splice(partIdx, 1);
    }
    p.soundOut.parts = [];
    p.soundOut.extensions = [];

    //const soundArray = [...p.soundOut.soundArray];
    //console.log(p.soundOut);
    //console.log(p)
    console.log(p.soundOut);
    //console.log(soundArray);
    /*
    soundArray.forEach((s) => {
      console.log(s)
    })
    */
    /*
    console.log(soundArray.length)
    for (let i = 0; i < soundArray.length; i++) {
            console.log(soundArray)

      console.log(i)
      console.log(soundArray[i])
    }
    */

    /*
    const gain = p.soundOut.output.gain;
    const defaultValue = gain.defaultValue;
    // todo: クリップノイズ対策
    gain.value = -1;
    window._cacheSounds?.forEach((s) => {
      s?.stop && s?.stop();
      s?.disconnect && s?.disconnect();
    });

    gain.value = defaultValue;
    */

    p.userStartAudio();
  }
};

new p5(sketch);
