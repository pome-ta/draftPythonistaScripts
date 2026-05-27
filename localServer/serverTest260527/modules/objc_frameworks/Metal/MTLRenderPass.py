import ctypes

from pyrubicon.objc.types import with_encoding, with_preferred_encoding


# ref: `[#L37 | MKCoordinateRegion | toga/iOS/src/toga_iOS/libs/mapkit.py](https://github.com/beeware/toga/blob/f1f9979a939e0d2e27d493c01b4b7b4d5ea19cb1/iOS/src/toga_iOS/libs/mapkit.py#L37)`
@with_preferred_encoding(b'{MTLClearColor=dddd}')
@with_encoding(b'{?=dddd}')
class MTLClearColor(ctypes.Structure):

  _fields_ = [
    ('red', ctypes.c_double),
    ('green', ctypes.c_double),
    ('blue', ctypes.c_double),
    ('alpha', ctypes.c_double),
  ]

  def __repr__(self):
    return f'<MTLClearColor({self.red}, {self.green}, {self.blue}, {self.alpha})>'

  def __str__(self):
    return f'red={self.red}, green={self.green}, blue={self.blue}, alpha={self.alpha}'


def MTLClearColorMake(red: ctypes.c_double, green: ctypes.c_double,
                      blue: ctypes.c_double,
                      alpha: ctypes.c_double) -> MTLClearColor:
  return MTLClearColor(red, green, blue, alpha)

