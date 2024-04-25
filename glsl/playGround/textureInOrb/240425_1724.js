precision highp float;

uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform sampler2D u_texture;
uniform vec4 u_tint_color;
uniform vec4 u_fill_color;
varying vec2 v_tex_coord;


const float PI = acos(-1.0);
const float SQRT2 = sqrt(2.0);

vec2 ComputeEdgeGradients(ivec2 pos) {
  float g = 
    - texture2D(u_texture, pos + ivec2(-1.0, -1.0)).a
    - texture2D(u_texture, pos + ivec2(-1.0,  1.0)).a
    + texture2D(u_texture, pos + ivec2( 1.0, -1.0)).a
    + texture2D(u_texture, pos + ivec2( 1.0,  1.0)).a;
    
  return normalize(vec2(
    g + texture2D(u_texture, pos + ivec2(1.0, 0.0)).a - texture2D(u_texture, pos + ivec2(-1.0, 0.0)).a * SQRT2,
    g + texture2D(u_texture, pos + ivec2(0.0, 1.0)).a - texture2D(u_texture, pos + ivec2(0.0, -1.0)).a * SQRT2
  ));
}



float ApproximateEdgeDelta(vec2 grad, float a) {
  if (grad.x == 0.0 || grad.y == 0.0) {
    // linear function is correct if both gx and gy are zero
    // and still fair if only one of them is zero
    return 0.5 - a;
  }
  // reduce symmetrical equation to first octant only
  grad = abs(normalize(grad));
  float gmax = max(grad.x, grad.y);
  float gmin = min(grad.x, grad.y);

  // compute delta
  float a1 = 0.5 * gmin / gmax;
  if (a < a1) {
    // 0 <= a < a1
    return 0.5 * (gmax + gmin) - sqrt(2.0 * gmax * gmin * a);
  }
  if (a < (1.0 - a1)) {
    // a1 <= a <= 1 - a1
    return (0.5 - a) * gmax;
  }
  // 1-a1 < a <= 1
  return -0.5 * (gmax + gmin) + sqrt(2.0 * gmax * gmin * (1.0 - a));
}

float InitializeDistance(vec2 grad, float alpha) {
  if (alpha <= 0.0) {
    // outside
    return 10000.0;  // 浮動小数点数の精度が心もとないので気持ち小さめにする
  } else if (alpha < 1.0) {
    // on the edge
    return ApproximateEdgeDelta(grad, alpha);
  } else {
    // inside
    return 0.0;
  }
}


vec4 UpdateDistance(vec4 p, vec2 pos, vec2 o) {
  vec4 neighbor = texture2D(u_texture, pos + o);
  vec2 ndelta = vec2(neighbor.xy);
  vec4 closest = texture2D(u_texture, pos + o - ndelta);
  if (closest.a == 0.0 || o == ndelta) {
    // neighbor has no closest yet or neighbor's closest is p itself
    return p;
  }
  
}

void main(){
  //vec2 uv = v_tex_coord;
  vec2 pos = v_tex_coord;
  vec2 grad = ComputeEdgeGradients(pos);
  
  
  
  //vec4 texmain = texture2D(u_texture, uv);
  //vec4 mask = vec4(fract(smoothstep(0.2, 0.8, texmain.a)));
  //vec4 mask = vec4(texmain.a);
  
  
  
  
  gl_FragColor = vec4(grad, 0.0, 1.0);
}

