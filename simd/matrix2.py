import ctypes
from vector2 import Vector2


class float4(ctypes.Structure):
  _fields_ = [
    ('m', ctypes.c_float * 4)
  ]


class m4(ctypes.Structure):
  _fields_ = [
    ('m00', ctypes.c_float), ('m01', ctypes.c_float),
    ('m10', ctypes.c_float), ('m11', ctypes.c_float)
  ]


class columns(ctypes.Structure):
  _fields_ = [
    ('c0', Vector2),
    ('c1', Vector2)
  ]


class Matrix2(ctypes.Union):
  _anonymous_ = ['columns', 's1', 's2']
  _fields_ = [
    ('columns', columns),
    ('s1', float4),
    ('s2', m4)
  ]

  def __str__(self):
    valus = [float(x) for x in self.s1.m]
    mstr = f'''Matrix2:
  [{valus[0]:.4f}, {valus[1]:.4f}]
  [{valus[2]:.4f}, {valus[3]:.4f}]'''
    return mstr

  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    cols = (
      Vector2(1.0, 0.0),
      Vector2(0.0, 1.0))
    self.columns = cols


if __name__ == '__main__':
  m2 = Matrix2()
  print(m2)
