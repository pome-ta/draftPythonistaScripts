const title = '4.2 ケーススタディ:Wave Clock';

const sketch = (p) => {
  let w, h;
  let setupWidth, setupHeight;

  let _angnoise, _radiusnosise;
  let _xnoise, _ynoise;
  let _angle = -p.PI / 2;
  let _radius;
  let _strokeCol = 254;
  let _strokeChange = -1;

  p.setup = () => {
    // put setup code here
    p.createCanvas(p.windowWidth, p.windowHeight);
    windowFlexSize();
    p.frameRate(30);
    p.background(255 - 23);
    p.noFill();

    _angnoise = p.random(10);
    _radiusnosise = p.random(10);
    _xnoise = p.random(10);
    _ynoise = p.random(10);
  };

  p.draw = () => {
    _radiusnosise += 0.005;
    _radius = p.noise(_radiusnosise) * 550 + 1;

    _angnoise += 0.005;
    _angle += p.noise(_angnoise) * 6 - 3;
    if (_angle > 360) {
      _angle -= 360;
    }
    if (_angle < 0) {
      _angle += 360;
    }

    _xnoise += 0.01;
    _ynoise += 0.01;
    const centerx = w / 2 + p.noise(_xnoise) * 100 - 50;
    const centery = h / 2 + p.noise(_ynoise) * 100 - 50;

    const rad = p.radians(_angle);
    const x1 = centerx + _radius * p.cos(rad);
    const y1 = centery + _radius * p.sin(rad);

    const opprad = rad + p.PI;
    const x2 = centerx + _radius * p.cos(opprad);
    const y2 = centery + _radius * p.sin(opprad);

    _strokeCol += _strokeChange;
    if (_strokeCol > 254) {
      _strokeChange = -1;
    }
    if (_strokeCol < 0) {
      _strokeChange = 1;
    }
    p.stroke(_strokeCol, 60);
    p.strokeWeight(1);

    p.line(x1, y1, x2, y2);
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

document.addEventListener('DOMContentLoaded', () => {
  // --- start
  window._p5Instance = new p5(sketch);
});
