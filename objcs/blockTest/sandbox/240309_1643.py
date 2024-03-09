import ctypes
from objc_util import ObjCClass, ns

from pyBlock import Block


@Block
def hoge(s: ctypes.c_void_p) -> ctypes.c_void_p:
  return ns(1)

