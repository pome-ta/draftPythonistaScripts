import ctypes

from pyrubicon.objc.types import with_preferred_encoding

# [SCNVector3 | Apple Developer Documentation](https://developer.apple.com/documentation/scenekit/scnvector3)
# wip: iOS - `float`, macOS - `CGFloat`
_SCNVector3Encoding = b'{SCNVector3=fff}'


@with_preferred_encoding(_SCNVector3Encoding)
class SCNVector3(ctypes.Structure):
  _fields_ = [
    ('x', ctypes.c_float),
    ('y', ctypes.c_float),
    ('z', ctypes.c_float),
  ]

  def __repr__(self):
    return f'<SCNVector3({self.x}, {self.y}, {self.z})>'

  def __str__(self):
    return f'x={self.x}, y={self.y}, z={self.z}'

