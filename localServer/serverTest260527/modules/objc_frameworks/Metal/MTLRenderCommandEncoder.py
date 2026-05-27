from enum import IntEnum


class MTLPrimitiveType(IntEnum):
  #[doc(alias = "MTLPrimitiveTypePoint")]
  point = 0
  #[doc(alias = "MTLPrimitiveTypeLine")]
  line = 1
  #[doc(alias = "MTLPrimitiveTypeLineStrip")]
  lineStrip = 2
  #[doc(alias = "MTLPrimitiveTypeTriangle")]
  triangle = 3
  #[doc(alias = "MTLPrimitiveTypeTriangleStrip")]
  triangleStrip = 4


class MTLCullMode(IntEnum):
  #[doc(alias = "MTLCullModeNone")]
  none = 0
  #[doc(alias = "MTLCullModeFront")]
  front = 1
  #[doc(alias = "MTLCullModeBack")]
  back = 2


class MTLWinding(IntEnum):
  #[doc(alias = "MTLWindingClockwise")]
  clockwise = 0
  #[doc(alias = "MTLWindingCounterClockwise")]
  counterClockwise = 1


class MTLTriangleFillMode(IntEnum):
  #[doc(alias = "MTLTriangleFillModeFill")]
  fill = 0
  #[doc(alias = "MTLTriangleFillModeLines")]
  lines = 1

