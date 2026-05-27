const title = 'spectrum 調整';

class EventWrapper {
  constructor() {
    [this.click, this.start, this.move, this.end, this.isTouch] =
      /iPhone|iPad|iPod|Android/.test(navigator.userAgent)
        ? ['click', 'touchstart', 'touchmove', 'touchend', true]
        : ['click', 'mousedown', 'mousemove', 'mouseup', false];
  }
}

const eventWrap = new EventWrapper();

const sketch = (p) => {
  let w, h;
  let setupWidth, setupHeight, setupRatio;

  let bgColor;
  let toneOsc;
  const frq = 440;
  const toneTypes = [
    'sine',
    'triangle',
    'sawtooth',
    'square',
    'square',
    'sawtooth',
    'triangle',
    'sine',
  ];
  let currentTypeIndex = 0;
  let xQuarterSize = 0;

  let fft;

  let touchX = null;
  let touchY = null;
  const delayTime = 0.2;

  let ts;

  class TapScreen {
    tapSize = 48;
    baseColrHSB = [0.0, 0.0, 1.0];

    constructor(mainCanvas) {
      this.p = mainCanvas;
      this.pg = null;
      this.x = null;
      this.y = null;
    }

    update() {
      if (this.pg === null && this.x === null && this.y === null) {
        return;
      }
      this.p.image(
        this.pg,
        this.x - this.tapSize / 2,
        this.y - this.tapSize / 2
      );
    }

    initTapMark() {
      this.pg = this.pg ?? this.p.createGraphics(this.tapSize, this.tapSize);

      this.pg.colorMode(this.pg.HSB, 1.0, 1.0, 1.0, 1.0);
      this.pgColor = this.pg.color(...this.baseColrHSB);
      this.pgColor.setAlpha(0.5);
      this.pg.fill(this.pgColor);

      this.pg.noStroke();
      this.pg.circle(this.tapSize / 2, this.tapSize / 2, this.tapSize);
    }

    tapStarted(x, y) {
      this.initTapMark();
      this.x = x;
      this.y = y;
    }

    taphMoved(x, y) {
      this.x = x;
      this.y = y;
    }

    tapEnded() {
      this.pg?.remove();
      this.pg = null;
    }
  }

  p.setup = () => {
    // sound init
    window._cacheSounds?.forEach((s) => {
      s.stop();
      s.disconnect();
    });

    p.userStartAudio();
    p.canvas.addEventListener(eventWrap.move, (e) => e.preventDefault(), {
      passive: false,
    });

    // put setup code here
    windowFlexSize(true);
    //p.colorMode(p.HSB, 1.0, 1.0, 1.0, 1.0);
    p.colorMode(p.HSB, toneTypes.length, 1.0, 1.0, 1.0);
    bgColor = p.color(0, 0, 64 / 255);
    p.background(bgColor);

    toneOsc = new p5.Oscillator(frq, toneTypes[currentTypeIndex]);
    //toneOsc = new p5.SinOsc();
    //toneOsc = new p5.TriOsc();
    //toneOsc = new p5.SawOsc();
    //toneOsc = new p5.SqrOsc();

    fft = new p5.FFT();
    p.textAlign(p.CENTER, p.CENTER);
    p.textSize(32);

    ts = new TapScreen(p);

    window._cacheSounds = [toneOsc];
  };

  p.draw = () => {
    // put drawing code here
    //p.background(bgColor);
    if (touchX !== null || touchY !== null) {
      p.background(p.color(currentTypeIndex, 0.32, 64 / 255));
    } else {
      p.background(bgColor);
    }

    let spectrum = fft.analyze();
    p.noStroke();
    p.fill(0.2, 0.5, 0.8);
    for (let i = 0; i < spectrum.length; i++) {
      let x = p.map(i * 8, 0, spectrum.length, 0, p.width);
      let h = -p.height + p.map(spectrum[i], 0, 255, p.height, 0);
      p.rect(x, p.height, p.width / spectrum.length, h);
    }

    let waveform = fft.waveform();
    p.noFill();
    p.beginShape();
    p.stroke(0.8, 0.5, 0.8);
    for (let i = 0; i < waveform.length; i++) {
      let x = p.map(i, 0, waveform.length, 0, p.width);
      let y = p.map(waveform[i], -1, 1, 0, p.height);
      p.vertex(x, y);
    }
    p.endShape();

    p.noStroke();
    p.fill(0.0, 0.0, 0.8);

    if (touchX !== null || touchY !== null) {
      p.text(
        `${toneTypes[currentTypeIndex]}\n${toneOsc.f}`,
        p.width / 2,
        p.height / 2
      );
      ts.update();
    } else {
      p.text(`${'osc type'}\n${'frequency'}`, p.width / 2, p.height / 2);
    }
  };

  p.touchStarted = (e) => {
    getTouchXY();
    chooseSetType(touchX);
    toneOsc.freq(frqRatio(touchX));
    toneOsc.amp(valueRatio(touchY));
    toneOsc.start();

    ts.tapStarted(touchX, touchY);
  };

  p.touchMoved = (e) => {
    getTouchXY();
    chooseSetType(touchX);
    toneOsc.freq(frqRatio(touchX));
    toneOsc.amp(valueRatio(touchY));

    ts.taphMoved(touchX, touchY);
  };

  p.touchEnded = (e) => {
    touchX = null;
    touchY = null;
    toneOsc.amp(0, delayTime);
    toneOsc.stop(delayTime + 0.05);

    ts.tapEnded();
  };

  p.windowResized = (event) => {
    windowFlexSize(true);
  };

  function getTouchXY() {
    if (eventWrap.isTouch) {
      for (let touch of p.touches) {
        touchX = 0 <= touch.x && touch.x <= p.width ? touch.x : null;
        touchY = 0 <= touch.y && touch.y <= p.height ? touch.y : null;
      }
    } else {
      // xxx: PC 用。。。ダサい
      touchX =
        p.mouseIsPressed && 0 <= p.mouseX && p.mouseX <= p.width
          ? p.mouseX
          : null;
      touchY =
        p.mouseIsPressed && 0 <= p.mouseY && p.mouseY <= p.height
          ? p.mouseY
          : null;
    }
  }

  function chooseSetType(x) {
    const typeIndex = Math.floor(x / xQuarterSize);
    if (currentTypeIndex === typeIndex) {
      return;
    }
    //console.log(`${currentTypeIndex}`)
    currentTypeIndex = typeIndex;
    toneOsc.setType(toneTypes[currentTypeIndex]);
  }

  function frqRatio(f) {
    const fr = (f / (p.width / 2)) * frq;
    return Math.ceil(fr * 1000) / 1000;
  }

  function valueRatio(v) {
    const vl = v === null ? 0 : v / p.height - 1;
    return vl;
  }

  function windowFlexSize(isFullSize = false) {
    const isInitialize =
      typeof setupWidth === 'undefined' || typeof setupHeight === 'undefined';

    [setupWidth, setupHeight] = isInitialize
      ? [p.width, p.height]
      : [setupWidth, setupHeight];

    const sizeRatio = 1;
    const windowWidth = p.windowWidth * sizeRatio;
    const windowHeight = p.windowHeight * sizeRatio;

    if (isFullSize) {
      w = windowWidth;
      h = windowHeight;
    } else {
      const widthRatio =
        windowWidth < setupWidth ? windowWidth / setupWidth : 1;
      const heightRatio =
        windowHeight < setupHeight ? windowHeight / setupHeight : 1;

      setupRatio = Math.min(widthRatio, heightRatio);
      w = setupWidth * setupRatio;
      h = setupHeight * setupRatio;
    }
    xQuarterSize = w / toneTypes.length;
    p.resizeCanvas(w, h);
  }
};

new p5(sketch);
//window._p5Instance = new p5(sketch);
