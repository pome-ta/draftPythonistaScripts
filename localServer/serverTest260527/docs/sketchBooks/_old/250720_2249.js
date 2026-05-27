// ちゃっぴーアナライザー

new p5((p) => {
  let fft, amp, osc;
  let peakHold = [];

  p.setup = () => {
    p.createCanvas(p.windowWidth, p.windowHeight);
    p.userStartAudio(); // iOS対応

    // sound
    osc = new p5.Oscillator(440, 'sine');
    osc.amp(0.4);
    osc.start();

    fft = new p5.FFT(0.8, 1024);
    amp = new p5.Amplitude();
  };

  p.draw = () => {
    p.background(0);
    const spectrum = fft.analyze();
    updatePeakHold(spectrum);
    drawDbGrid();
    drawFreqLabels();
    drawSpectrum(spectrum);
    drawRMS();
  };

  function updatePeakHold(spectrum) {
    const decay = 0.95;
    if (peakHold.length !== spectrum.length) {
      peakHold = spectrum.slice();
    }
    for (let i = 0; i < spectrum.length; i++) {
      peakHold[i] = Math.max(spectrum[i], peakHold[i] * decay);
    }
  }

  function ampToDb(amp) {
    const db = 20 * Math.log10(amp / 255);
    return p.constrain(db, -60, 0);
  }

  function drawDbGrid() {
    const dbSteps = [-60, -48, -36, -24, -12, 0];
    p.stroke(50);
    p.textAlign(p.RIGHT, p.CENTER);
    p.fill(150);
    dbSteps.forEach((db) => {
      const y = p.map(db, -60, 0, p.height, 0);
      p.line(0, y, p.width, y);
      p.noStroke();
      p.text(`${db} dB`, p.width - 5, y);
      p.stroke(50);
    });
  }

  function drawFreqLabels() {
    const freqs = [20, 100, 1000, 10000];
    const nyquist = p.sampleRate() / 2;
    p.textAlign(p.CENTER, p.BOTTOM);
    p.fill(150);
    p.noStroke();
    freqs.forEach((f) => {
      const x = p.map(
        Math.log10(f),
        Math.log10(20),
        Math.log10(nyquist),
        0,
        p.width
      );
      p.text(`${f >= 1000 ? f / 1000 + 'k' : f}Hz`, x, p.height);
      p.stroke(50);
      p.line(x, 0, x, p.height);
    });
  }

  function drawSpectrum(spectrum) {
    const nyquist = p.sampleRate() / 2;
    const binWidth = nyquist / spectrum.length;

    for (let i = 1; i < spectrum.length; i++) {
      const freq = i * binWidth;
      const x = p.map(
        Math.log10(freq),
        Math.log10(20),
        Math.log10(nyquist),
        0,
        p.width
      );
      const y = p.map(ampToDb(spectrum[i]), -60, 0, p.height, 0);
      const yPeak = p.map(ampToDb(peakHold[i]), -60, 0, p.height, 0);

      p.stroke(0, 255, 0);
      p.line(x, p.height, x, y);

      p.stroke(255, 100, 100);
      p.line(x, yPeak - 2, x, yPeak);
    }
  }

  function drawRMS() {
    const level = amp.getLevel();
    const dB = 20 * Math.log10(level || 0.0001); // avoid log(0)
    p.fill(255);
    p.noStroke();
    p.textAlign(p.LEFT, p.TOP);
    p.text(`RMS: ${dB.toFixed(1)} dB`, 10, 10);
  }
});
