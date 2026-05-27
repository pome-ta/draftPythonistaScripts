const title = 'p5 sound';

const sketch = (p) => {
  let w, h;
  let setupWidth, setupHeight;

  const v = 360;
  let sineTone, env, analyzer;

  p.setup = () => {
    // put setup code here
    p.createCanvas(p.windowWidth, p.windowHeight);
    windowFlexSize();
    p.frameRate(30);

    p.colorMode(p.HSL, v, 1, 1);

    sineTone = new p5.Oscillator('sine');
    const tone = 440 * p.random();
    console.log(`tone: ${tone}`);
    sineTone.freq(tone);
    sineTone.amp(0.5);

    sineTone.start();
  };

  p.draw = () => {
    p.background(p.frameCount % v, 1, 0.5);
  };

  function windowFlexSize() {
    const isInitialize =
      typeof setupWidth === 'undefined' || typeof setupHeight === 'undefined';
    [setupWidth, setupHeight] = isInitialize
      ? [p.width, p.height]
      : [setupWidth, setupHeight];

    const sizeRatio = 1;
    const windowWidth = p.windowWidth * sizeRatio;
    const windowHeight = p.windowHeight * sizeRatio;

    const widthRatio = windowWidth < setupWidth ? windowWidth / setupWidth : 1;
    const heightRatio =
      windowHeight < setupHeight ? windowHeight / setupHeight : 1;

    const setupRatio = Math.min(widthRatio, heightRatio);
    w = setupWidth * setupRatio;
    h = setupHeight * setupRatio;

    p.resizeCanvas(w, h);
  }
};

new p5(sketch);
//window._p5Instance = new p5(sketch);
