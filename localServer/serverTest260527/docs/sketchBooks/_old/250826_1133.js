// [p5.js-sound/examples/Compressor/sketch.js at main · processing/p5.js-sound · GitHub](https://github.com/processing/p5.js-sound/blob/main/examples/Compressor/sketch.js)

const soundFileURL =
  'https://github.com/processing/p5.js-sound/blob/main/examples/files/beat.ogg';

// todo: `p.loadSound` 用 => 通常のGitHub URL を`githubusercontent` へ置き換え
const githubusercontent = (githubUrl) =>
  githubUrl
    .replace('https://github.com/', 'https://raw.githubusercontent.com/')
    .replace('/blob/', '/');

const interactionTraceKitPath =
  '../../sketchBooks/modules/interactionTraceKit.js';

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  let pointerTracker;
  let tapIndicator;

  let soundFile;

  p.preload = () => {
    soundReStart();

    p.loadModule(interactionTraceKitPath, (m) => {
      const { PointerTracker, TapIndicator } = m;
      pointerTracker = new PointerTracker(p);
      tapIndicator = new TapIndicator(p);
    });

    const url = githubusercontent(soundFileURL);
    console.log(url);
    soundFile = p.loadSound(url);
  };

  p.setup = () => {
    // put setup code here
    //soundReStart();

    p.canvas.addEventListener(pointerTracker.move, (e) => e.preventDefault(), {
      passive: false,
    });

    p.createCanvas(w, h);
    tapIndicator.setup();
    /*

    const url = githubusercontent(soundFileURL);
    console.log(url);
    soundFile = p.loadSound(url);

    console.log(soundFile);
    */
  };

  p.draw = () => {
    // put drawing code here
    p.background(255);
  };
  /*
  p.mousePressed = (e)=> {
    console.log(p)
    if (soundFile.isPlaying()) {
      soundFile.pause();
    } else {
      soundFile.play();
    }
  }
  */

  p.touchStarted = (e) => {};

  p.touchMoved = (e) => {};

  p.touchEnded = (e) => {
    if (soundFile.isPlaying()) {
      soundFile.pause();
    } else {
      soundFile.play();
    }
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };

  function soundReStart() {
    // wip: クリップノイズ対策
    p.disposeSound();

    const soundArray = p.soundOut.soundArray;
    for (let soundIdx = soundArray.length - 1; soundIdx >= 0; soundIdx--) {
      const sound = soundArray[soundIdx];
      // todo: 過剰処理?
      sound?.stop && sound.stop();
      sound?.dispose && sound.dispose();
      sound?.disconnect && sound.disconnect();

      soundArray.splice(soundIdx, 1);
    }

    const parts = p.soundOut.parts;
    for (let partIdx = parts.length - 1; partIdx >= 0; partIdx--) {
      const phrases = parts[partIdx].phrases;
      for (let phraseIdx = phrases.length - 1; phraseIdx >= 0; phraseIdx--) {
        phrases.splice(phraseIdx, 1);
      }
      parts.splice(partIdx, 1);
    }

    p.soundOut.soundArray = [];
    p.soundOut.parts = [];
    p.soundOut.extensions = []; // todo: 対応必要?

    p.userStartAudio();
  }
};

new p5(sketch);
