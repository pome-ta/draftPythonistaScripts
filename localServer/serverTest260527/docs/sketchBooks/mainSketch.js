const v = 360;

function setup() {
  createCanvas(v, v);
  colorMode(HSL, v, 1, 1);
}

function draw() {
  background(frameCount % v, 1, 0.5);
}


