from enum import IntEnum, IntFlag

from .constants import _get_const


class SCNGeometrySourceSemantic:
  vertex = _get_const('SCNGeometrySourceSemanticVertex')
  normal = _get_const('SCNGeometrySourceSemanticNormal')
  texcoord = _get_const('SCNGeometrySourceSemanticTexcoord')
  color = _get_const('SCNGeometrySourceSemanticColor')
  tangent = _get_const('SCNGeometrySourceSemanticTangent')
  edgeCrease = _get_const('SCNGeometrySourceSemanticEdgeCrease')
  vertexCrease = _get_const('SCNGeometrySourceSemanticVertexCrease')
  boneIndices = _get_const('SCNGeometrySourceSemanticBoneIndices')
  boneWeights = _get_const('SCNGeometrySourceSemanticBoneWeights')


class SCNGeometryPrimitiveType(IntEnum):
  triangles = 0
  triangleStrip = 1
  line = 2
  point = 3
  polygon = 4

