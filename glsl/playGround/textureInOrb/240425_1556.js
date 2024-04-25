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
  vec4 mask = vec4(sign(texmain.a));
  vec4 outto = mix(vec4(1.0, 0.0, 0.0, 1.0),texmain, mask);
  vec4 outline = vec4(outto.a * -1.0 + 1.0);
  
  
  
  
  gl_FragColor = outline;
}

