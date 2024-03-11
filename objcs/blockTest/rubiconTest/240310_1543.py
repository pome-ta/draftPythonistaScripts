import ctypes
#import objc
from objc import ObjCClass, Block

import pdbg


@Block
def hoge(s: ctypes.c_void_p) -> ctypes.c_void_p:
  return ns(1)

