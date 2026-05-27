// [p5.js-sound/examples/_monosynth_basic/sketch.js at main · processing/p5.js-sound · GitHub](https://github.com/processing/p5.js-sound/blob/main/examples/_monosynth_basic/sketch.js)


const interactionTraceKitPath =
  '../../sketchBooks/modules/interactionTraceKit.js';

const sketch = (p) => {
  let w, h;

  let pointerTracker;
  let tapIndicator;
  
  
  let monoSynth;

  p.preload = () => {
    p.loadModule(interactionTraceKitPath, (m) => {
      const { PointerTracker, TapIndicator } = m;
      pointerTracker = new PointerTracker(p);
      tapIndicator = new TapIndicator(p);
    });
  };

  p.setup = () => {
    // put setup code here
    w = p.windowWidth;
    h = p.windowHeight;

    p.canvas.addEventListener(pointerTracker.move, (e) => e.preventDefault(), {
      passive: false,
    });
    
    
    monoSynth = new p5.MonoSynth();

    p.createCanvas(w, h);
    
    
    p.textAlign(p.CENTER);
    p.text('press to play a random note at a random velocity', w/2, h/2);
    
    tapIndicator.setup();
  };


  p.draw = () => {
    // put drawing code here
    //p.background(128);
    
  };

  /*
  p.mousePressed = (e) => {
  };

  p.mouseReleased = (e) => {
  };
  */

  p.touchStarted = (e) => {
    // pick a random midi note
    const midiVal = p.midiToFreq(p.round(p.random(50,72) ));
    monoSynth.triggerAttack(midiVal, p.random() );
  };

  p.touchMoved = (e) => {};

  p.touchEnded = (e) => {
    monoSynth.triggerRelease();
  };


  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };
};

new p5(sketch);
