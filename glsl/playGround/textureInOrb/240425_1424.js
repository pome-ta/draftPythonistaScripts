precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform sampler2D u_texture;
uniform vec4 u_tint_color;
uniform vec4 u_fill_color;
varying vec2 v_tex_coord;

uniform vec2 sprite_size;
uniform vec2 resolution;

const float PI = acos(-1.0);

void main(){
  //vec2 uv = (v_tex_coord * 2.0 - sprite_size) / min(sprite_size.x, sprite_size.y);
  //vec2 uv = (sprite_size * 2.0 - v_tex_coord) / min(v_tex_coord.x, v_tex_coord.y);
  //vec2 uv = min(sprite_size.x, sprite_size.y) / v_tex_coord;
  //vec2 uv = (u_sprite_size * 2.0 - v_tex_coord) / min(v_tex_coord.x, v_tex_coord.y);
  //vec4 texMs = texture2D(u_texture, uv);
  //gl_FragColor = texMs;
  //vec2 uv = (v_tex_coord * 2.0 - resolution) / min(resolution.x, resolution.y);
  //vec2 uv = v_tex_coord*resolution;
  vec2 uv = v_tex_coord;
  
  
  gl_FragColor = vec4(vec3(length(uv)), 1.0);
  
  
  
}

