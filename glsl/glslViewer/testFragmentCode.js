#version 300 es
precision highp float;

out vec4 fragColor;

uniform float u_time;
uniform vec2 u_mouse;
uniform vec2 u_resolution;

void main() {
  vec2 p = (gl_FragCoord.xy * 2.0 - u_resolution) / min(u_resolution.x, u_resolution.y);
  vec3 outColor = vec3(p, abs(sin(u_time)));

  fragColor = vec4(outColor, 1.0);
}

