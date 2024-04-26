precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform sampler2D u_texture;
uniform vec4 u_tint_color;
uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


const float PI = acos(-1.0);

bool xorb(float a, float b) {
  bool ab = bool(a);
  bool bb = bool(b);
  if (ab != bb) {
    return true;
  }
  return false;
}

void main(){
  vec2 uv = v_tex_coord;
  vec4 texmain = texture2D(u_texture, uv);
  vec3 mainc = texmain.rgb;
  
  float diff = 0.05;
  float aU = texture2D(u_texture, vec2(uv.x, uv.y - diff)).a;
  float aD = texture2D(u_texture, vec2(uv.x, uv.y + diff)).a;
  float aR = texture2D(u_texture, vec2(uv.x - diff, uv.y)).a;
  float aL = texture2D(u_texture, vec2(uv.x + diff, uv.y)).a;
  float am = texture2D(u_texture, uv).a;
  
  float xxx = 0.0;
  if (xorb(aU, aD)) {
    //xxx += max(aU, aD);
    //xxx += mix(aU, aD, 0.5);
    xxx = smoothstep(0.2, xxx, aU);
  }
  if (xorb(aR, aL)) {
    xxx += max(aR, aL);
  }
  
  float line = fract(smoothstep(0.1, 0.5, am));
  float dots = length(vec2(xxx,line));
  
  
  vec3 auaua = vec3(xxx);
  //vec3 auaua = vec3(am);
  
  //vec3 auaua = vec3(steps);
  

  //gl_FragColor = texmain;
  gl_FragColor = vec4(auaua, 1.0);
}

