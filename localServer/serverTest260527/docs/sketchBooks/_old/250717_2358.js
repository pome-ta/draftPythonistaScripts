// ちゃっぴーのスペクトラムアナライザー

let osc, env, fft;
let started = false;
const fftSize = 1024; // より細かい解析が必要なら増やす

new p5((p) => {
  p.setup = () => {
    p.createCanvas(400, 250);
    p.textFont('monospace', 10);
    fft = new p5.FFT(0.8, fftSize); // smooth: 0.8, bins: 1024
  };

  p.draw = () => {
    p.background(0);

    if (!started) {
      p.fill(255);
      p.textAlign(p.CENTER, p.CENTER);
      p.text('Tap to Start Audio', p.width / 2, p.height / 2);
      return;
    }

    // FFT 解析と描画
    const spectrum = fft.analyze();
    const binWidth = p.width / spectrum.length;

    // グリッド(縦線 + ラベル)
    drawGrid(p, spectrum.length);

    // FFT バー描画
    p.noStroke();
    p.fill(0, 255, 100);
    for (let i = 0; i < spectrum.length; i++) {
      const h = -p.map(spectrum[i], 0, 255, 0, p.height - 30); // ラベルぶん下げ
      p.rect(i * binWidth, p.height, binWidth, h);
    }
  };

  // iOS含むモバイル対応
  p.touchStarted = () => {
    if (!started) {
      p.userStartAudio();
      started = true;

      osc = new p5.Oscillator('sine');
      osc.amp(0);
      osc.start();

      env = new p5.Envelope();
      env.setADSR(0.001, 0.1, 0, 0.3);
      env.setRange(1, 0);

      fft.setInput(osc);

      playKick();
    } else {
      playKick();
    }
  };

  function playKick() {
    osc.freq(150);
    osc.amp(0);
    osc.freq(60, 0.15);
    env.play(osc, 0, 0.01);
  }

  function drawGrid(p, bins) {
    const freqs = [60, 120, 250, 500, 1000, 2000, 4000, 8000, 12000, 16000]; // 表示したい周波数
    const nyquist = p.sampleRate() / 2;

    p.stroke(180); // ← 見えるように白寄りのグレー
    p.fill(200);
    p.textAlign(p.CENTER, p.BOTTOM);
    p.textSize(10);

    for (let i = 0; i < freqs.length; i++) {
      const f = freqs[i];
      const index = Math.floor((f / nyquist) * bins);

      // 周波数に対応するX座標
      const x = p.map(index, 0, bins, 0, p.width);

      if (x >= 0 && x <= p.width) {
        p.line(x, 0, x, p.height); // グリッド線
        p.noStroke();
        p.text(f + 'Hz', x, p.height - 2); // ラベル
        p.stroke(180); // stroke 消されたので再設定
      }
    }
  }
});
