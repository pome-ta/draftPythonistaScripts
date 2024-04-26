precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform sampler2D u_texture;
uniform vec4 u_tint_color;
uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


const float PI = acos(-1.0);


void main(){
  vec2 uv = v_tex_coord;
  vec4 texmain = texture2D(u_texture, uv);
  float ms = texmain.a;
  float ls = pow(ms, -1.0);
  smoothstep()
  
  vec3 auau = vec3(ls);
  
  //gl_FragColor = texmain;
  gl_FragColor = vec4(auau, 1.0);
}

