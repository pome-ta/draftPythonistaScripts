let song;
const url =
  'https://github.com/processing/p5.js-sound/blob/main/examples/files/Damscray_DancingTiger.ogg';

function preload() {
  // 外部URLから音源をロード
  const githubusercontent = (githubUrl) =>
    githubUrl
      .replace('https://github.com/', 'https://raw.githubusercontent.com/')
      .replace('/blob/', '/');
  song = loadSound(githubusercontent(url));
}

function setup() {
  createCanvas(400, 200);
  textAlign(CENTER, CENTER);
  textSize(16);
  text('クリックで再生', width / 2, height / 2);
}

function mousePressed() {
  if (song.isPlaying()) {
    song.pause();
  } else {
    song.play();
  }
}

// https://raw.githubusercontent.com/processing/p5.js-sound/main/examples/files/Damscray_DancingTiger.ogg

// https://github.com/processing/p5.js-sound/blob/main/examples/files/Damscray_DancingTiger.ogg

//const rawUrl = blobUrl.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/");
//const rawUrl = blobUrl.replace('https://github.com/', 'https://raw.githubusercontent.com/').replace('/blob/', '/');
