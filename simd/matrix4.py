import ctypes
from vector4 import Vector4


class float16(ctypes.Structure):
  _fields_ = [
    ('m', ctypes.c_float * 16)
  ]


class m16(ctypes.Structure):
  _fields_ = [
    ('m00', ctypes.c_float), ('m01', ctypes.c_float), ('m02', ctypes.c_float), ('m03', ctypes.c_float),
    ('m10', ctypes.c_float), ('m11', ctypes.c_float), ('m12', ctypes.c_float), ('m13', ctypes.c_float),
    ('m20', ctypes.c_float), ('m21', ctypes.c_float), ('m22', ctypes.c_float), ('m23', ctypes.c_float),
    ('m30', ctypes.c_float), ('m31', ctypes.c_float), ('m32', ctypes.c_float), ('m33', ctypes.c_float)
  ]


class columns(ctypes.Structure):
  _fields_ = [
    ('c0', Vector4),
    ('c1', Vector4),
    ('c2', Vector4),
    ('c3', Vector4)
  ]


class Matrix4(ctypes.Union):
  _anonymous_ = ['columns', 's1', 's2']
  _fields_ = [
    ('columns', columns),
    ('s1', float16),
    ('s2', m16)
  ]

  def __str__(self):
    values = [float(x) for x in self.s1.m]
    mstr = f'''Matrix4:
  [{values[0]:.4f}, {values[1]:.4f}, {values[2]:.4f}, {values[3]:.4f}]
  [{values[4]:.4f}, {values[5]:.4f}, {values[6]:.4f}, {values[7]:.4f}]
  [{values[8]:.4f}, {values[9]:.4f}, {values[10]:.4f}, {values[11]:.4f}]
  [{values[12]:.4f}, {values[13]:.4f}, {values[14]:.4f}, {values[15]:.4f}]'''
    return mstr

  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    cols = (
      Vector4(1.0, 0.0, 0.0, 0.0),
      Vector4(0.0, 1.0, 0.0, 0.0),
      Vector4(0.0, 0.0, 1.0, 0.0),
      Vector4(0.0, 0.0, 0.0, 1.0))
    self.columns = cols


if __name__ == '__main__':
  m4 = Matrix4()
  print(m4)
