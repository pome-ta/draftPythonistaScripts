import ctypes

from pyrubicon.objc.api import ObjCInstance
from pyrubicon.objc.runtime import Foundation, Class


def NSStringFromClass(cls: Class) -> ObjCInstance:
  _function = Foundation.NSStringFromClass
  _function.restype = ctypes.c_void_p
  _function.argtypes = [
    Class,
  ]
  return ObjCInstance(_function(cls))

