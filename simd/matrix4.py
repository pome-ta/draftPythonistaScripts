import ctypes
from vector4 import Vector4



class float16(ctypes.Structure):
  _fields_ = [
    ('m', ctypes.c_float * 16),
  ]


class m16(ctypes.Structure):
  _fields_ = [
    ('m00', ctypes.c_float), ('m01', ctypes.c_float), ('m02', ctypes.c_float), ('m03', ctypes.c_float),
    ('m10', ctypes.c_float), ('m11', ctypes.c_float), ('m12', ctypes.c_float), ('m13', ctypes.c_float),
    ('m20', ctypes.c_float), ('m21', ctypes.c_float), ('m22', ctypes.c_float), ('m23', ctypes.c_float),
    ('m30', ctypes.c_float), ('m31', ctypes.c_float), ('m32', ctypes.c_float), ('m33', ctypes.c_float),
  ]

class columns(ctypes.Structure):
  _fields_ = [
    ('c0', Vector4),
    ('c1', Vector4),
    ('c2', Vector4),
    ('c3', Vector4),
  ]


class Matrix4(ctypes.Union):
  _anonymous_ = ['columns', 's1', 's2']
  _fields_ = [
    ('columns', columns),
    ('s1', float16),
    ('s2', m16),
  ]
  
  def __str__(self):
    valus = [float(x) for x in self.s1.m]
    mstr = f'''Matrix4:
  [{valus[0]:.4f}, {valus[1]:.4f}, {valus[2]:.4f}, {valus[3]:.4f}]
  [{valus[4]:.4f}, {valus[5]:.4f}, {valus[6]:.4f}, {valus[7]:.4f}]
  [{valus[8]:.4f}, {valus[9]:.4f}, {valus[10]:.4f}, {valus[11]:.4f}]
  [{valus[12]:.4f}, {valus[13]:.4f}, {valus[14]:.4f}, {valus[15]:.4f}]'''
    return mstr
  
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)
    columns = (
      Vector4(1.0, 0.0, 0.0, 0.0),
      Vector4(0.0, 1.0, 0.0, 0.0),
      Vector4(0.0, 0.0, 1.0, 0.0),
      Vector4(0.0, 0.0, 0.0, 1.0))
    self.columns = columns

if __name__ == '__main__':
  m4 = Matrix4()
  print(m4)
