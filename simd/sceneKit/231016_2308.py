from math import pi
import ctypes

from objc_util import c, load_framework, ObjCClass, _struct_class_from_fields, struct_from_tuple

import pdbg

load_framework('SceneKit')


class SCNMatrix4(ctypes.Structure):
  _fields_ = [
    ('a', ctypes.c_float),
    ('b', ctypes.c_float),
    ('c', ctypes.c_float),
    ('d', ctypes.c_float),
    ('e', ctypes.c_float),
    ('f', ctypes.c_float),
    ('g', ctypes.c_float),
    ('h', ctypes.c_float),
    ('i', ctypes.c_float),
    ('j', ctypes.c_float),
    ('k', ctypes.c_float),
    ('l', ctypes.c_float),
    ('m', ctypes.c_float),
    ('n', ctypes.c_float),
    ('o', ctypes.c_float),
    ('p', ctypes.c_float),
  ]

  def __str__(self):
    return f'{self.a=}, {self.b=}, {self.c=}, {self.d=},\n{self.e=}, {self.f=}, {self.g=}, {self.h=},\n{self.i=}, {self.j=}, {self.k=}, {self.l=},\n{self.m=}, {self.n=}, {self.o=}, {self.p=},\n'


def SCNMatrix4MakeRotation(angle, x, y, z):
  _func = c.SCNMatrix4MakeRotation
  _func.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
  ]
  _func.restype = SCNMatrix4
  #pdbg.state(_func)
  _instance = _func(angle, x, y, z)
  #pdbg.state(_instance.a)
  #obj_instance = ObjCInstance(_instance)
  #return obj_instance
  return _instance


rt = SCNMatrix4MakeRotation(-pi / 2, 1, 0, 0)
#pdbg.state(rt)
print(rt)

#st = _struct_class_from_fields(range(6))

