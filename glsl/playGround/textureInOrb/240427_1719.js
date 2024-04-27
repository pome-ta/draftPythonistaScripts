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
  //vec2 uv = v_tex_coord;
  vec2 uv = (v_tex_coord - vec2(0.5)) * 2.0;
  
  float am = texture2D(u_texture, uv).a;
  
  float blurNum = 0.0;
  
  vec2 lr = vec2(blurNum, 0.0) / v_tex_coord;
  vec2 tb = vec2(0.0, blurNum) / v_tex_coord;
  vec4 color = vec4(0.0);
  color += texture2D(u_texture, uv);
  color += texture2D(u_texture, uv + lr);
  color += texture2D(u_texture, uv - lr);
  color += texture2D(u_texture, uv + tb);
  color += texture2D(u_texture, uv - tb);
  color += texture2D(u_texture, uv + lr + tb);
  color += texture2D(u_texture, uv + lr - tb);
  color += texture2D(u_texture, uv - lr + tb);
  color += texture2D(u_texture, uv - lr - tb);
  vec4 ccc =  vec4(color.rgb / color.w, 1.0);
  
  //gl_FragColor = ccc;
  gl_FragColor = texture2D(u_texture, uv);
}

