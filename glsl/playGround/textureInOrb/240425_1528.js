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
  float alf = texmain.a;
  float ralf = sign(alf);
  //if (ralf < 0.0 || ralf > 1.0) discard;
  vec4 masks = vec4(1.0, 0.0, 0.0, 1.0);
  vec4 outto = mix(masks,texmain, alf);
  
  
  
  gl_FragColor = outto;
}

