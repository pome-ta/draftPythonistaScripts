#version 300 es
precision highp float;
uniform float blockOffset;
uniform float sampleRate;

out vec4 outColor;

vec2 mainSound(float time){
  //return vec2(sin(6.2831*440.*time));
  //return vec2(sin(6.2831*440.*time)*exp(-3.*time));
  //return vec2(sin(6.2831*440.*time)+sin(6.2831*440.*1.5*time));
  //return vec2((fract(sin(time*1e3)*1e6)-.5)*pow(fract(-time*4.),mod(time*4.,2.)*8.));
  
  //return vec2(3.0*sin(3e2*time)*pow(fract(-time*2.),4.));
  return vec2(3.0*sin(3e2*time)*pow(fract(-time*1.25),6.));
}
void main(){
  float time = blockOffset + ((gl_FragCoord.x - 0.5) + (gl_FragCoord.y - 0.5) * 512.0) / sampleRate;
  vec2 XY = mainSound(time);
  vec2 XV = floor((0.5 + 0.5 * XY) * 65536.0);
  vec2 XL = mod(XV, 256.0) / 255.0;
  vec2 XH = floor(XV / 256.0) / 255.0;
  outColor = vec4(XL.x, XH.x, XL.y, XH.y);
}

