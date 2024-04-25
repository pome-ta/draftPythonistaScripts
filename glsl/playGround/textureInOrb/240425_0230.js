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
  uv.x += sin(u_time);
  
  
  
  if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0)discard;
  //gl_FragColor = vec4(uv.x, uv.y, 0.0, 1.0);
  gl_FragColor = texture2D(u_texture, uv);
  
}

