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
  float a0 = texmain.a;
  
  float a1 = texture2D(u_texture, vec2(uv.x + 0.2, uv.y)).a;
  
  float rzlt = 0.0;
  rzlt += (a1 + a0) / 2.0;
  vec3 main3 = vec3(a0-rzlt);
  
  
  gl_FragColor = vec4(main3, 1.0);
}

