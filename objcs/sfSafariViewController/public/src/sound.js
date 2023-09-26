import {wavVisualize} from './visualizar.js';
import {barVisualize} from './visualizar.js';

console.log('out');

let VERTEX_SHADER_SOURCE;
let FRAGMENT_SHADER_SOURCE;
const DURATION = 180;
const BUFFER_WIDTH = 512;
const BUFFER_HEIGHT = 512;
const FFT_SIZE = 128;

VERTEX_SHADER_SOURCE = `#version 300 es
in vec3 p;
void main(){
  gl_Position = vec4(p, 1.0);
}`;

/*
FRAGMENT_SHADER_SOURCE = `#version 300 es
precision highp float;
uniform float blockOffset;
uniform float sampleRate;

out vec4 outColor;

vec2 mainSound(float time){
  //return vec2(sin(6.2831*440.*time));
  //return vec2(sin(6.2831*440.*time)*exp(-3.*time));
  //return vec2(sin(6.2831*440.*time)+sin(6.2831*440.*1.5*time));
  //return vec2((fract(sin(time*1e3)*1e6)-.5)*pow(fract(-time*4.),mod(time*4.,2.)*8.));
  return vec2(3.0*sin(3e2*time)*pow(fract(-time*2.),4.));
}
void main(){
  float time = blockOffset + ((gl_FragCoord.x - 0.5) + (gl_FragCoord.y - 0.5) * 512.0) / sampleRate;
  vec2 XY = mainSound(time);
  vec2 XV = floor((0.5 + 0.5 * XY) * 65536.0);
  vec2 XL = mod(XV, 256.0) / 255.0;
  vec2 XH = floor(XV / 256.0) / 255.0;
  outColor = vec4(XL.x, XH.x, XL.y, XH.y);
}
`;
*/


class Sound {
  constructor() {
    this.canvas = null;
    this.gl = null;
    this.program = null;
    this.vs = null;
    this.fs = null;
    this.attLocation = null;
    this.uniLocation = null;
    this.audioCtx = null;
    this.audioBufferSourceNode = null;
    this.audioAnalyserNode = null;
    this.audioFrequencyBinCount = 0;
    this.isPlay = false;
    
    this.waveCanvas = null;
    this.barCanvas = null;
    
    this.init();
  }
  
  init() {
    this.canvas = document.createElement('canvas');
    
    this.waveCanvas = document.querySelector('#waveVisualizer');
    this.barCanvas = document.querySelector('#barVisualizer');
    
    const wrap = document.querySelector('#wrap');
    wrap.appendChild(this.canvas);
    
    this.canvas.width = BUFFER_WIDTH;
    this.canvas.height = BUFFER_HEIGHT;
    
    this.gl = this.canvas.getContext('webgl2');
    this.vs = this.createShader(VERTEX_SHADER_SOURCE, true);
    
    this.audioCtx = new AudioContext();
  }
  
  render(source, draw=false) {
    FRAGMENT_SHADER_SOURCE = source;
    this.fs = this.createShader(FRAGMENT_SHADER_SOURCE, false);
    let program = this.gl.createProgram();
    this.gl.attachShader(program, this.vs);
    this.gl.attachShader(program, this.fs);
    this.gl.linkProgram(program);
    this.gl.deleteShader(this.fs);
    
    if(!this.gl.getProgramParameter(program, this.gl.LINK_STATUS)) {
      let msg = this.gl.getProgramInfoLog(program);
      console.log('render');
      console.log(msg);
      program = null;
      return;
    }
    
    if(draw !== true){return;}
    if(this.program != null) {
      this.gl.deleteProgram(this.program);
    }
    this.program = program;
    this.gl.useProgram(this.program);
    this.attLocation = this.gl.getAttribLocation(this.program, 'p');
    
    this.uniLocation = {
      blockOffset: this.gl.getUniformLocation(this.program, 'blockOffset'),
      sampleRate: this.gl.getUniformLocation(this.program, 'sampleRate'),
    };
    
    this.gl.bindBuffer(this.gl.ARRAY_BUFFER, this.gl.createBuffer());
    this.gl.bufferData(this.gl.ARRAY_BUFFER,
      new Float32Array(
        [-1.0,  1.0,  0.0, -1.0,
         -1.0,  0.0,  1.0,  1.0,
          0.0,  1.0, -1.0,  0.0]),
      this.gl.STATIC_DRAW);
    this.gl.enableVertexAttribArray(this.attLocation);
    this.gl.vertexAttribPointer(this.attLocation, 3, this.gl.FLOAT, false, 0, 0);
    
    this.gl.disable(this.gl.DEPTH_TEST);
    this.gl.disable(this.gl.CULL_FACE);
    this.gl.disable(this.gl.BLEND);
    this.gl.clearColor(0.0, 0.0, 0.0, 0.0);
    this.gl.clear(this.gl.COLOR_BUFFER_BIT);
    this.gl.viewport(0, 0, BUFFER_WIDTH, BUFFER_HEIGHT);
    
    this.draw();
  }
  
  draw() {
    const sample = this.audioCtx.sampleRate;
    const buffer = this.audioCtx.createBuffer(2, sample * DURATION, sample);
    
    const channelDataLeft  = buffer.getChannelData(0);
    const channelDataRight = buffer.getChannelData(1);
    const range = BUFFER_WIDTH * BUFFER_HEIGHT;
    const pixel = new Uint8Array(BUFFER_WIDTH * BUFFER_HEIGHT * 4);
    
    this.gl.uniform1f(this.uniLocation.sampleRate, sample);
    const block = Math.ceil((sample * DURATION) / range);
    for(let i = 0, j = block; i < j; ++i){
      this.gl.uniform1f(this.uniLocation.blockOffset, i * range / sample);
      this.gl.drawArrays(this.gl.TRIANGLE_STRIP, 0, 4);
      this.gl.readPixels(0, 0, BUFFER_WIDTH, BUFFER_HEIGHT, this.gl.RGBA, this.gl.UNSIGNED_BYTE, pixel);
      for(let k = 0, l = range; k < l; ++k){
        channelDataLeft[i * range + k]  = (pixel[k * 4 + 0] + 256 * pixel[k * 4 + 1]) / 65535 * 2 - 1;
        channelDataRight[i * range + k] = (pixel[k * 4 + 2] + 256 * pixel[k * 4 + 3]) / 65535 * 2 - 1;
      }
    }
    
    if(this.isPlay === true){
      this.audioBufferSourceNode.stop();
      this.isPlay = false;
    }
    
    this.audioBufferSourceNode = this.audioCtx.createBufferSource();
    this.audioAnalyserNode = this.audioCtx.createAnalyser();
    this.audioAnalyserNode.smoothingTimeConstant = 0.8;
    this.audioAnalyserNode.fftSize = FFT_SIZE * 2;
    this.audioFrequencyBinCount = this.audioAnalyserNode.frequencyBinCount;
    
    this.audioAnalyserNode.minDecibels = -90;
    this.audioAnalyserNode.maxDecibels = -10;
    wavVisualize(this.waveCanvas, this.audioAnalyserNode);
    barVisualize(this.barCanvas, this.audioAnalyserNode);
    
    this.audioBufferSourceNode.connect(this.audioAnalyserNode);
    this.audioAnalyserNode.connect(this.audioCtx.destination);
    this.audioBufferSourceNode.buffer = buffer;
    this.audioBufferSourceNode.loop = false;
    this.audioBufferSourceNode.start();
    this.isPlay = true;
  }
  
  createShader(source, isVertexShader){
    const type = isVertexShader === true ? this.gl.VERTEX_SHADER : this.gl.FRAGMENT_SHADER;
    const shader = this.gl.createShader(type);
    this.gl.shaderSource(shader, source);
    this.gl.compileShader(shader);
    if(!this.gl.getShaderParameter(shader, this.gl.COMPILE_STATUS)){
      let msg = this.gl.getShaderInfoLog(shader);
      console.log('createShader');
      console.warn(msg);
      return false;
    }
    return shader;
  }
}



console.log('start');
let mySound = null;


const soundShader_path = new URL(`shader/sound.py`, location.protocol + '//' + location.host + location.pathname).href

fetch(soundShader_path)
  .then((res) => res.text())
  .then((soundShader) => {
    mySound = new Sound();
    //console.log(soundShader);
    mySound.render(soundShader, true);
    document.addEventListener(eventName, initAudioContext);
   });


const eventName = typeof document.ontouchend !== 'undefined' ? 'touchend' : 'mouseup';
//document.addEventListener(eventName, initAudioContext);

function initAudioContext(){
  document.removeEventListener(eventName, initAudioContext);
  // wake up AudioContext
  //console.log('sound');
  //console.log(mySound.isPlay);
  mySound.audioCtx.resume();
  //mySound.render(true);
}


/*
window.addEventListener('DOMContentLoaded', () => {
  console.log('DOMContentLoaded');
  mySound = new Sound();
  mySound.render(true);
  
  // 着火のおまじない
  // xxx: 事前準備してるコードを走らせるので簡単に
  const eventName = typeof document.ontouchend !== 'undefined' ? 'touchend' : 'mouseup';
  document.addEventListener(eventName, initAudioContext);
  function initAudioContext(){
    document.removeEventListener(eventName, initAudioContext);
    // wake up AudioContext
    console.log('sound');
    console.log(mySound.isPlay);
    mySound.audioCtx.resume();
    //mySound.render(true);
  }
  
}, false);
*/
//})();


