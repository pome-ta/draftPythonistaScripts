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
  vec2 p = -1.0 + 2.0 * v_tex_coord + (0.5 / u_sprite_size * 2.0);
    float len = length(p);
    vec2 uv = v_tex_coord + (p/len) * 1.5 * cos(len*50.0 - u_time*10.0) * 0.03;
    uv.x += sin(u_time);
    gl_FragColor = texture2D(u_texture,uv);
  
}

