import ctypes

from pyrubicon.objc.types import CGFloat
from pyrubicon.objc.types import __LP64__, with_preferred_encoding

from .constants import framework as CoreGraphics

if __LP64__:
  _CGAffineTransformEncoding = b'{CGAffineTransform=dddddd}'
else:
  _CGAffineTransformEncoding = b'{CGAffineTransform=ffffff}'


@with_preferred_encoding(_CGAffineTransformEncoding)
class CGAffineTransform(ctypes.Structure):

  _fields_ = [
    ('a', CGFloat),
    ('b', CGFloat),
    ('c', CGFloat),
    ('d', CGFloat),
    ('tx', CGFloat),
    ('ty', CGFloat),
  ]

  def __repr__(self):
    return f'<CGAffineTransform({self.a}, {self.b}, {self.c}, {self.d}, {self.tx}, {self.ty})>'

  def __str__(self):
    return f'a={self.a}, b={self.b}, c={self.c}, d={self.d}, tx={self.tx}, ty={self.ty}'


CGAffineTransformIdentity = CGAffineTransform.in_dll(
  CoreGraphics, 'CGAffineTransformIdentity')


def CGAffineTransformMakeScale(sx: CGFloat, sy: CGFloat) -> CGAffineTransform:
  try:
    _func = CGAffineTransformMakeScale._cfunc
  except AttributeError:
    _func = CoreGraphics.CGAffineTransformMakeScale
    _func.restype = CGAffineTransform
    _func.argtypes = [
      CGFloat,
      CGFloat,
    ]
    CGAffineTransformMakeScale._cfunc = _func

  return _func(sx, sy)


# CGAffineTransformMake
# CGAffineTransformMakeRotation
# CGAffineTransformMakeTranslation


def CGAffineTransformTranslate(t: CGAffineTransform, sx: CGFloat,
                               sy: CGFloat) -> CGAffineTransform:
  try:
    _func = CGAffineTransformTranslate._cfunc
  except AttributeError:
    _func = CoreGraphics.CGAffineTransformTranslate
    _func.restype = CGAffineTransform
    _func.argtypes = [
      CGAffineTransform,
      CGFloat,
      CGFloat,
    ]
    CGAffineTransformTranslate._cfunc = _func

  return _func(t, sx, sy)


# CGAffineTransformScale
# CGAffineTransformRotate
# CGAffineTransformInvert


def CGAffineTransformConcat(t1: CGAffineTransform,
                            t2: CGAffineTransform) -> CGAffineTransform:
  try:
    _func = CGAffineTransformConcat._cfunc
  except AttributeError:
    _func = CoreGraphics.CGAffineTransformConcat
    _func.restype = CGAffineTransform
    _func.argtypes = [
      CGAffineTransform,
      CGAffineTransform,
    ]
    CGAffineTransformConcat._cfunc = _func

  return _func(t1, t2)

