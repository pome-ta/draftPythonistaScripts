// [p5.js-sound/examples/Filter_BandPass/sketch.js at main · processing/p5.js-sound · GitHub](https://github.com/processing/p5.js-sound/blob/main/examples/Filter_BandPass/sketch.js)


/**
 *  Example: Apply a p5.BandPass filter to white noise.
 *  Visualize the sound with FFT.
 *  Map mouseX to the bandpass frequency
 *  and mouseY to resonance/width of the a BandPass filter
 */


const interactionTraceKitPath = 'modules/interactionTraceKit.js';

const sketch = (p) => {
  let w, h;
  
  let noise;
  let fft;
  let filter, filterFreq, filterWidth;

  let pointerTracker;
  let tapIndicator;
  
  let description = 'loading';
  let pTag1;

  p.preload = () => {
    p.loadModule(interactionTraceKitPath, (m) => {
      const {PointerTracker, TapIndicator} = m;
      pointerTracker = new PointerTracker(p);
      tapIndicator = new TapIndicator(p);
    });
  };

  p.setup = () => {
    // put setup code here
    w = p.windowWidth;
    h = p.windowHeight;

    
    p.createCanvas(w, h);
    p.fill(255, 40, 255);
    
    filter = new p5.BandPass();

    noise = new p5.Noise();

    noise.disconnect(); // Disconnect soundfile from main output...
    filter.process(noise); // ...and connect to filter so we'll only hear BandPass.
    noise.start();

    fft = new p5.FFT();
    
    pTag1 = [w * 0.5, h * 0.3];
    p.textAlign(p.CENTER);
    p.textFont('monospace');
    p.text(description, ...pTag1);
    
    
    p.canvas.addEventListener(pointerTracker.move, (e) => e.preventDefault(), {
      passive: false,
    });
    
    
    tapIndicator.setup();
    
  };

  p.draw = () => {
    // put drawing code here
    p.background(30);
    
    // Map mouseX to a bandpass freq from the FFT spectrum range: 10Hz - 22050Hz
    filterFreq = p.map (p.mouseX, 0, w, 10, 22050);
    // Map mouseY to resonance/width
    filterWidth = p.map(p.mouseY, 0, h, 0, 90);
    // set filter parameters
    filter.set(filterFreq, filterWidth);
    
    
    // Draw every value in the FFT spectrum analysis where
    // x = lowest (10Hz) to highest (22050Hz) frequencies,
    // h = energy / amplitude at that frequency
    const spectrum = fft.analyze();
    const length = spectrum.length;
    p.noStroke();
    
    spectrum.forEach((value, idx)=> {
      const x = p.map(idx, 0, length, 0, h);
      const _h = -h + p.map(value, 0, 255, h, 0);
      p.rect(x, h, w/length, _h) ;
    });
    updateDescription();
    
  };

  function updateDescription() {
    p.push();
    p.fill(255 - 30);
    description = 'Playing! Press any key to pause.\nFilter Frequency:\n' + filterFreq + '\nFilter Width:\n' + filterWidth;
    
    p.text(description, ...pTag1);
    p.pop();
  }
  
  p.touchStarted = (e) => {
  };

  p.touchMoved = (e) => {
  };

  p.touchEnded = (e) => {
  };

  p.windowResized = (e) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };
};

new p5(sketch);

