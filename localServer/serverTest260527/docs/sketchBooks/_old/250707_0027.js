const sketch = (p) => {
  p.setup = () => {
    // put setup code here
    fitFullSizeCanvas();
    p.background(255 - 23);
  };

  p.draw = () => {
    // put drawing code here
  };

  p.windowResized = (event) => {
    fitFullSizeCanvas();
  };

  function fitFullSizeCanvas() {
    p.resizeCanvas(p.windowWidth, p.windowHeight);
  }
};

document.addEventListener('DOMContentLoaded', () => {
  // --- start
  const myp5 = new p5(sketch);
});
