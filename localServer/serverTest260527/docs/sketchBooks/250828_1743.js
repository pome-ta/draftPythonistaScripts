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
  let w, h;

  let pointerTracker;
  let tapIndicator;

  let fftHeight;
  let fftWidth;

  let soundFile;
  let fft;

  let compressor;

  //UI Objects
  let cntrls;

  //knob info

  //colors
  let knobBckg;
  let knobLine;
  let threshLineCol;

  //dimensions
  let knobRad;
  let knobLineLen;

  let pressed = false;
  let cntrlIndex;

  let description;

  p.preload = () => {
    p.loadModule(interactionTraceKitPath, (m) => {
      const { PointerTracker, TapIndicator } = m;
      pointerTracker = new PointerTracker(p);
      tapIndicator = new TapIndicator(p);
    });

    const url = githubusercontent(soundFileURL);
    soundFile = p.loadSound(url);
  };

  p.setup = () => {
    // put setup code here
    w = p.windowWidth;
    h = p.windowHeight;

    p.canvas.addEventListener(pointerTracker.move, (e) => e.preventDefault(), {
      passive: false,
    });

    p.angleMode(p.DEGREES);
    p.createCanvas(w, h);

    fftHeight = 0.75 * h;
    fftWidth = 0.8 * w;

    compressor = new p5.Compressor();

    // Disconnect soundfile from main output.
    // メイン出力からサウンドファイルを切断します。
    // Then, connect it to the filter, so that we only hear the filtered sound
    // 次に、フィルターに接続して、フィルタリングされた音だけが聞こえるようにします
    soundFile.disconnect();
    compressor.process(soundFile);

    fft = new p5.FFT();

    soundFile.loop();

    //Create cntrls
    const x = 0.0625 * w;
    const y = 0.25 * h;

    cntrls = ['attack', 'knee', 'ratio', 'release', 'drywet'].map((t, idx) => {
      const knob = new Knob(t);
      const [_x, _y] =
        idx >= 3 && idx <= 4 ? [w - x, y * (idx - 1)] : [x, y + y * idx];
      knob.x = _x;
      knob.y = _y;

      return knob;
    });

    knobRad = 0.15 * h;
    knobLineLen = knobRad / 2;

    cntrls.push(new ThreshLine('threshold'));

    knobBckg = p.color(150);
    knobLine = p.color(30);
    threshLineCol = p.color(30);

    description = p.createDiv(
      'p5.Compressor: <br>' +
        "Adjust the knobs to control the compressor's " +
        'attack, knee, ratio, release, and wet / dry values ' +
        'Move the slider to adjust threshold.' +
        'For information on these audioParams, see <br>' +
        '<a href =https://www.w3.org/TR/webaudio/#the-dynamicscompressornode-interface>' +
        'Web Audio Dyanmics Compressor Node Interface</a>'
    );
    description.size(0.75 * fftWidth, p.AUTO);
    description.position(w - fftWidth, 1.15 * fftHeight);

    tapIndicator.setup();
  };

  // attack knee ratio threshold release

  p.draw = () => {
    // put drawing code here
    p.background(255);
    p.fill(180);

    const spectrum = fft.analyze();
    p.noStroke();

    for (let i = 0; i < spectrum.length; i++) {
      const x = p.map(i, 0, spectrum.length, 0.2 * w, fftWidth);
      const y = -fftHeight + p.map(spectrum[i], 0, 255, fftHeight, 0.125 * h);
      p.rect(x, fftHeight, fftWidth / spectrum.length, y);
    }

    if (pressed) {
      cntrls[cntrlIndex].change();
    }

    cntrls.forEach((cntrl) => cntrl.display());
  };

  /*
  p.mousePressed = (e) => {
    for (let i = 0; i < cntrls.length; i++) {
      if (cntrls[i].mouseOver()) {
        pressed = true;
        cntrlIndex = i;
        break;
      }
    }
  };

  p.mouseReleased = (e) => {
    pressed = false;
  };
  */
  
  p.touchStarted = (e) => {
    for (let i = 0; i < cntrls.length; i++) {
      if (cntrls[i].mouseOver()) {
        pressed = true;
        cntrlIndex = i;
        break;
      }
    }
  };


  p.touchMoved = (e) => {};

  p.touchEnded = (e) => {
    pressed = false;
  };


  const getRange = (type) => {
    switch (type) {
      case 'attack':
        return [0, 1];
      case 'knee':
        return [0, 40];
      case 'ratio':
        return [1, 20];
      case 'release':
        return [0, 1];
      case 'threshold':
        return [-100, 0];
      case 'drywet':
        return [0, 1];
      default:
        return 0;
    }
  };

  const getDefault = (type) => {
    switch (type) {
      case 'attack':
        return 0.003;
      case 'knee':
        return 30;
      case 'ratio':
        return 12;
      case 'release':
        return 0.25;
      case 'threshold':
        return -24;
      case 'drywet':
        return compressor.drywet(1);
      default:
        return 0;
    }
  };

  const updateVal = (range, curAngle, cntrlIndex) => {
    const newVal = p.map(curAngle, 0, 270, range[0], range[1]);
    switch (cntrlIndex) {
      case 0:
        compressor.attack(newVal);
        break;
      case 1:
        compressor.knee(newVal);
        break;
      case 2:
        compressor.ratio(newVal);
        break;
      case 3:
        compressor.release(newVal);
        break;
      case 4:
        compressor.drywet(newVal);
        break;
      case 5:
        compressor.threshold(newVal);
        break;
      default:
        break;
    }
    return newVal;
  };

  function ThreshLine(type) {
    this.type = type;
    this.x = w - fftWidth;
    this.range = getRange(type);
    this.current = getDefault(type);
    this.y = p.map(this.current, -100, 0, fftHeight, h - fftHeight);

    this.length = fftWidth;

    this.display = function () {
      p.stroke(threshLineCol);
      p.line(this.x, this.y, this.length, this.y);
      p.noStroke();
      p.text(type, fftWidth - 50, this.y + knobLineLen, knobRad, knobRad);
      p.text(
        this.current,
        fftWidth - 50,
        this.y + knobLineLen + 10,
        knobRad,
        knobRad
      );
    };

    this.change = function () {
      // this.y = mouseY;
      if (p.mouseY < h - fftHeight) {
        this.y = h - fftHeight;
      } else if (p.mouseY > fftHeight) {
        this.y = fftHeight;
      } else {
        this.y = mouseY;
      }
      this.current = p.map(this.y, fftHeight, h - fftHeight, -100, 0);
    };

    this.mouseOver = function () {
      if (
        p.mouseX > this.x &&
        p.mouseX < w - this.x &&
        p.mouseY < this.y + 5 &&
        p.mouseY > this.y - 5
      ) {
        return true;
      } else {
        return false;
      }
    };
  }

  function Knob(type) {
    this.type = type;
    this.range = getRange(type);
    this.default = getDefault(type);
    this.current = this.default;
    this.curAngle = p.map(this.current, this.range[0], this.range[1], 50, 320);
    this.x;
    this.y;

    this.display = function () {
      p.noStroke();
      p.fill(knobBckg);
      p.ellipse(this.x, this.y, knobRad, knobRad);

      //draw the indicator line from knob center
      p.translate(this.x, this.y);
      p.rotate(this.curAngle);
      p.stroke(knobLine);
      p.line(0, 0, 0, knobLineLen);
      p.rotate(-this.curAngle);
      p.translate(-this.x, -this.y);
      p.noStroke();
      p.text(
        type,
        this.x - knobLineLen,
        this.y + knobLineLen,
        knobRad,
        knobRad
      );
      p.text(
        p.float(this.current).toFixed(2),
        this.x - knobLineLen,
        this.y + knobLineLen + 10,
        knobRad,
        knobRad
      );
    };

    this.mouseOver = function () {
      if (
        p.mouseX > this.x - knobLineLen &&
        p.mouseX < this.x + knobLineLen &&
        p.mouseY < this.y + knobLineLen &&
        p.mouseY > this.y - knobLineLen
      ) {
        return true;
      } else {
        return false;
      }
    };

    this.change = function () {
      p.translate(this.x, this.y);
      const a = p.atan2(p.mouseY - this.y, p.mouseX - this.x);
      this.curAngle = a - 90;

      if (this.curAngle < 0) {
        this.curAngle = this.curAngle + 360;
      }
      if (this.curAngle < 50) {
        this.curAngle = 50;
      } else if (this.curAngle > 320) {
        this.curAngle = 320;
      }
      this.current = updateVal(this.range, this.curAngle - 50, cntrlIndex);

      p.translate(-this.x, -this.y);
    };
  }

  p.windowResized = (e) => {
    console.log('re');
    w = p.windowWidth;
    h = p.windowHeight;
    p.resizeCanvas(w, h);
  };
};

new p5(sketch);
