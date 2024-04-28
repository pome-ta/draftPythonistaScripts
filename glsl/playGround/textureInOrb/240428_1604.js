precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform sampler2D u_texture;
uniform vec4 u_tint_color;
uniform vec4 u_fill_color;
varying vec2 v_tex_coord;




void main(){
  vec2 uv = v_tex_coord;
  vec4 texmain = texture2D(u_texture, uv);
  vec3 mainc = texmain.rgb;
  float am = texmain.a;
  
  float diff = 0.05;
  float aU = texture2D(u_texture, vec2(uv.x, uv.y - diff)).a;
  float aD = texture2D(u_texture, vec2(uv.x, uv.y + diff)).a;
  float aR = texture2D(u_texture, vec2(uv.x - diff, uv.y)).a;
  float aL = texture2D(u_texture, vec2(uv.x + diff, uv.y)).a;
  
  float mixal = 0.0;
  mixal += am;
  mixal += aU;
  mixal += aD;
  
  mixal = 0.0;
  mixal += uv.x * 0.5;
  
  
  
  
  //float mainal = clamp(mixal, 0.0, 1.0);
  float mainal = mixal;
  
  
  
  vec3 main3 = vec3(mainal);
  
  
  gl_FragColor = vec4(main3, 1.0);
}

