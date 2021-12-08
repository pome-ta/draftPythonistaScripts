import math
import ctypes
from objc_util import parse_struct


class xy(ctypes.Structure):
  _fields_ = [
    ('x', ctypes.c_float),
    ('y', ctypes.c_float),
  ]


class st(ctypes.Structure):
  _fields_ = [
    ('s', ctypes.c_float),
    ('t', ctypes.c_float),
  ]


class float2(ctypes.Structure):
  _fields_ = [('v', ctypes.c_float * 2)]


class Vector2(ctypes.Union):
  _anonymous_ = ['s1', 's2', 's3']
  _fields_ = [
    ('s1', xy),
    ('s2', st),
    ('s3', float2),
  ]

  def __str__(self):
    values = [float(i) for i in self.s3.v]
    vstr = f'''Vector2:
  [{values[0]:.4f}, {values[1]:.4f}]'''
    return vstr
    
  def __add__(self, other):
    if isinstance(other, self.__class__):
      return Vector2Add(self, other)
    else:
      raise NotImplementedError()
      
  def __sub__(self, other):
    if isinstance(other, self.__class__):
      return Vector2Subtract(self, other)
    else:
      raise NotImplementedError()
      
  def __mul__(self, other):
    if isinstance(other, self.__class__):
      return Vector2Multiply(self, other)
    else:
      raise NotImplementedError()
      
  def __truediv__(self, other):
    if isinstance(other, self.__class__):
      return Vector2Divide(self, other)
    else:
      raise NotImplementedError()

  def __init__(self, x=0.0, y=0.0, *args, **kw):
    super().__init__(*args, **kw)
    self.x = x
    self.y = y


simd2 = parse_struct('{simd2=fff}')


def to_simd2(old):
  return ctypes.cast(ctypes.pointer(old), ctypes.POINTER(simd2)).contents


def from_simd2(old):
  return ctypes.cast(ctypes.pointer(old), ctypes.POINTER(Vector2)).contents


def getVector2(func):
  return from_simd2(func(restype=simd2, argtypes=[]))


def setVector2(func, newvalue):
  newvalue = to_simd2(newvalue)
  return func(newvalue, restype=ctypes.c_void_p, argtypes=[simd2])


def Vector2Make(x, y):
  return Vector2(x=x, y=y)


def Vector2MakeWithArray(values):
  return Vector2(v=(ctypes.c_float * 2)(*values))


def Vector2Length(vector):
  v = [float(x) for x in vector.v]
  r = 0
  for x in v:
    r += math.pow(x, 2)
  return math.sqrt(r)


def Vector2Distance(vectorStart, vectorEnd):
  assert isinstance(vectorEnd, Vector2)
  return math.sqrt(
    math.pow(vectorStart.x - vectorEnd.x, 2) + math.pow(
      vectorStart.y - vectorEnd.y, 2))


def Vector2Negate(vector):
  v = Vector2()
  v.x = -vector.x
  v.y = -vector.y
  return v


def Vector2Normalize(vector):
  l = Vector2Length(vector)
  nv = Vector2()
  if l != 0:
    nv.x = vector.x / l
    nv.y = vector.y / l
    return nv
  else:
    raise ValueError('Cannot Normalise Vector of length 0')


def Vector2AddScalar(vector, value):
  v = Vector2()
  v.x = vector.x + value
  v.y = vector.y + value
  return v


def Vector2SubtractScalar(vector, value):
  v = Vector2()
  v.x = vector.x - value
  v.y = vector.y - value
  return v


def Vector2MultiplyScalar(vector, value):
  v = Vector2()
  v.x = vector.x * value
  v.y = vector.y * value
  return v


def Vector2DivideScalar(vector, value):
  v = Vector2()
  v.x = vector.x / value
  v.y = vector.y / value
  return v


def Vector2Add(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = vectorLeft.x + vectorRight.x
  v.y = vectorLeft.y + vectorRight.y
  return v


def Vector2Subtract(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = vectorLeft.x - vectorRight.x
  v.y = vectorLeft.y - vectorRight.y
  return v


def Vector2Multiply(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = vectorLeft.x * vectorRight.x
  v.y = vectorLeft.y * vectorRight.y
  return v


def Vector2Divide(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = vectorLeft.x / vectorRight.x
  v.y = vectorLeft.y / vectorRight.y
  return v


def Vector2DotProduct(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  return vectorLeft.x * vectorRight.x + vectorLeft.y * vectorRight.y


def Vector2Lerp(vectorStart, vectorEnd, t):
  assert isinstance(vectorEnd, Vector2)
  v = Vector2()
  v.x = vectorStart.x + ((vectorEnd.x - vectorStart.x) * t)
  v.y = vectorStart.y + ((vectorEnd.y - vectorStart.y) * t)


def Vector2Project(vectorToProject, projectionVector):
  assert isinstance(projectionVector, Vector2)
  scale = Vector2DotProduct(projectionVector, vectorToProject)
  scale /= Vector2DotProduct(projectionVector, projectionVector)
  v = Vector2MultiplyScalar(projectionVector, scale)
  return v


def Vector2Maximum(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = max(vectorLeft.x, vectorRight.x)
  v.y = max(vectorLeft.y, vectorRight.y)
  return v


def Vector2Minimum(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  v = Vector2()
  v.x = min(vectorLeft.x, vectorRight.x)
  v.y = min(vectorLeft.y, vectorRight.y)
  return v


def Vector2EqualToScalar(vector, value):
  x = vector.x == value
  y = vector.y == value
  return x and y

# xxx: ? `__all__` 用途？
#'Vector2Make', 'Vector2MakeWithArray', 'Vector2Length', 'Vector2Distance', 'Vector2Negate', 'Vector2Normalize', 'Vector2AddScalar', 'Vector2SubtractScalar', 'Vector2MultiplyScalar', 'Vector2DivideScalar', 'Vector2Add', 'Vector2Subtract', 'Vector2Multiply', 'Vector2Divide', 'Vector2DotProduct', 'Vector2Lerp', 'Vector2Project', 'Vector2Maximum', 'Vector2Minimum', 'Vector2EqualToScalar', 'Vector2AllEqualToVector4', 'Vector2AllGreaterThanOrEqualToScalar',


def Vector2AllEqualToVector4(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  x = vectorLeft.x == vectorRight.x
  y = vectorLeft.y == vectorRight.y
  return x and y


def Vector2AllGreaterThanOrEqualToScalar(vector, value):
  x = vector.x >= value
  y = vector.y >= value
  return x and y


def Vector2AllGreaterThanOrEqualToVector4(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  x = vectorLeft.x >= vectorRight.x
  y = vectorLeft.y >= vectorRight.y
  return x and y


def Vector2AllGreaterThanScalar(vector, value):
  x = vector.x > value
  y = vector.y > value
  return x and y


def Vector2AllGreaterThanVector4(vectorLeft, vectorRight):
  assert isinstance(vectorRight, Vector2)
  x = vectorLeft.x > vectorRight.x
  y = vectorLeft.y > vectorRight.y
  return x and y


__all__ = ['Vector2', 'setVector2', 'getVector2']

if __name__ == '__main__':
  v = Vector2Make(1, 1)
  print(v)
  print(Vector2AddScalar(v, 10))
  print(Vector2Length(Vector2Normalize(Vector2AddScalar(v, 10))))
  print(Vector2Minimum(v, Vector2MultiplyScalar(v, 35)))
  print(Vector2Normalize(Vector2AddScalar(v, 10)))
  print(Vector2AllGreaterThanScalar(v, 1.1))
