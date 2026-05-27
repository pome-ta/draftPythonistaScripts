from enum import IntEnum


class MDLGeometryType(IntEnum):
  # [doc(alias = "MDLGeometryTypePoints")]
  points = 0
  # [doc(alias = "MDLGeometryTypeLines")]
  lines = 1
  # [doc(alias = "MDLGeometryTypeTriangles")]
  triangles = 2
  # [doc(alias = "MDLGeometryTypeTriangleStrips")]
  triangleStrips = 3
  # [doc(alias = "MDLGeometryTypeQuads")]
  quads = 4
  # [doc(alias = "MDLGeometryTypeVariableTopology")]
  variableTopology = 5

