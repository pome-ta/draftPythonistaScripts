//const title = 'Spectrum analyzer';

class PointerEventMapper {
  #p;

  constructor(mainInstance) {
    //const IS_TOUCH_DEVICE = window.matchMedia('(hover: none)').matches;
    this.#p = mainInstance;
    this.x = null;
    this.y = null;
    [this.click, this.start, this.move, this.end, this.isTouchDevice] =
      /iPhone|iPad|iPod|Android/.test(navigator.userAgent)
        ? ['click', 'touchstart', 'touchmove', 'touchend', true]
        : ['click', 'mousedown', 'mousemove', 'mouseup', false];
  }

  updateXY() {
    this.isTouchDevice ? this.#touchUpdate() : this.#mouseUpdate();
  }

  #touchUpdate() {
    for (let touch of this.#p.touches) {
      this.x = 0 <= touch.x && touch.x <= this.#p.width ? touch.x : null;
      this.y = 0 <= touch.y && touch.y <= this.#p.height ? touch.y : null;
    }
  }

  #mouseUpdate() {
    if (!this.#p.mouseIsPressed) {
      this.x = null;
      this.y = null;
      return;
    }
    this.x =
      0 <= this.#p.mouseX && this.#p.mouseX <= this.#p.width
        ? this.#p.mouseX
        : null;
    this.y =
      0 <= this.#p.mouseY && this.#p.mouseY <= this.#p.height
        ? this.#p.mouseY
        : null;
  }
}

class TapMarkOnScreen {
  #p;
  #pg;
  #markSize;
  #markCenter;

  baseColrHSB = [0.0, 0.0, 1.0];

  constructor(mainInstance, markSize = 48) {
    this.#p = mainInstance;
    this.#pg = null;
    this.#markSize = markSize;
    this.#markCenter = markSize * 0.5;
    this.x = null;
    this.y = null;
  }

  draw() {
    if (this.#pg === null || this.x === null || this.y === null) {
      return;
    }
    //this.#p.image(this.#pg, this.x - this.#markCenter, this.y - this.#markCenter);
  }

  setup() {
    this.#pg =
      this.#pg ?? this.#p.createGraphics(this.#markSize, this.#markSize);
    console.log(this.#pg);

    this.#pg.colorMode(this.#pg.HSB, 1.0, 1.0, 1.0, 1.0);
    const pgColor = this.#pg.color(...this.baseColrHSB);
    pgColor.setAlpha(0.5);
    this.#pg.fill(pgColor);

    this.#pg.noStroke();
    this.#pg.circle(this.#markCenter, this.#markCenter, this.#markSize);
    this.#p.image(
      this.#pg,
      this.x - this.#markCenter,
      this.y - this.#markCenter
    );
  }

  started(x, y) {
    this.setup();
    this.x = x;
    this.y = y;
  }

  moved(x, y) {
    this.x = x;
    this.y = y;
  }

  ended() {
    this.#pg?.remove();
    this.#pg = null;
  }
}

const sketch = (p) => {
  let w = p.windowWidth;
  let h = p.windowHeight;

  const pointerEvents = new PointerEventMapper(p);
  const tapMark = new TapMarkOnScreen(p);

  let b = 0;

  p.setup = () => {
    // put setup code here
    p.canvas.addEventListener(pointerEvents.move, (e) => e.preventDefault(), {
      passive: false,
    });

    p.createCanvas(w, h);
    p.colorMode(p.RGB, 1);
    p.background(0.5);
  };
  p.draw = () => {
    // put drawing code here
    //p.background(p.random());
    tapMark.draw();
  };

  p.touchStarted = (e) => {
    if (b) {
      return;
    }
    b = 1;
    pointerEvents.updateXY();
    tapMark.started(pointerEvents.x, pointerEvents.y);
  };

  p.touchMoved = (e) => {
    if (b) {
      return;
    }
    pointerEvents.updateXY();
    tapMark.moved(pointerEvents.x, pointerEvents.y);
  };

  p.touchEnded = (e) => {
    if (b) {
      return;
    }
    pointerEvents.updateXY();
    tapMark.ended();
  };

  p.windowResized = (event) => {
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };
};

new p5(sketch);
