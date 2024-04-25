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
  //float diff = -sin(u_time) / 10.0;
  float diff = 0.05;
  vec4 texU = texture2D(u_texture, vec2(uv.x, uv.y - diff));
  vec4 texD = texture2D(u_texture, vec2(uv.x, uv.y + diff));
  vec4 texR = texture2D(u_texture, vec2(uv.x - diff, uv.y));
  vec4 texL = texture2D(u_texture, vec2(uv.x + diff, uv.y));
  
  float max1 = max(texU.a, texD.a);
  float max2 = max(texR.a, texL.a);
  float maxFull = max(max1, max2);
  
  vec4 wrap = vec4(vec3(1.0, 0.5, 1.0), maxFull);
  vec4 main = texture2D(u_texture, uv);
  vec4 tex = mix(wrap,main, 0.1);
  
  
  
  
  //if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0)discard;
  //gl_FragColor = vec4(uv.x, uv.y, 0.0, 1.0);
  //gl_FragColor = texture2D(u_texture, uv);
  //gl_FragColor = vec4(vec3(maxFull), 1.0);
  //gl_FragColor = main;
  gl_FragColor = tex;
  
  
}

