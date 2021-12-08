import ctypes
from vector3 import Vector3


class float9(ctypes.Structure):
  _fields_ = [
    ('m', ctypes.c_float * 9)
  ]


class m9(ctypes.Structure):
  _fields_ = [
    ('m00', ctypes.c_float), ('m01', ctypes.c_float), ('m02', ctypes.c_float),
    ('m10', ctypes.c_float), ('m11', ctypes.c_float), ('m12', ctypes.c_float),
    ('m20', ctypes.c_float), ('m21', ctypes.c_float), ('m22', ctypes.c_float)
  ]


class columns(ctypes.Structure):
  _fields_ = [
    ('c0', Vector3),
    ('c1', Vector3),
    ('c2', Vector3)
  ]


class Matrix3(ctypes.Union):
  _anonymous_ = ['columns', 's1', 's2']
  _fields_ = [
    ('columns', columns),
    ('s1', float9),
    ('s2', m9)
  ]

  def __str__(self):
    values = [float(x) for x in self.s1.m]
    mstr = f'''Matrix3:
  [{values[0]:.4f}, {values[1]:.4f}, {values[2]:.4f}]
  [{values[3]:.4f}, {values[4]:.4f}, {values[5]:.4f}]
  [{values[6]:.4f}, {values[7]:.4f}, {values[8]:.4f}]'''
    return mstr

  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    cols = (
      Vector3(1.0, 0.0, 0.0),
      Vector3(0.0, 1.0, 0.0),
      Vector3(0.0, 0.0, 1.0))
    self.columns = cols


if __name__ == '__main__':
  m4 = Matrix3()
  print(m4)
