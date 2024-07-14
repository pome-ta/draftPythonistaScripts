import webbrowser
import ctypes
from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, c

import pdbg

NSFileManager = ObjCClass('NSFileManager')


def NSSearchPathForDirectoriesInDomains(directory, domainMask, expandTilde):
  fnc = c.NSSearchPathForDirectoriesInDomains
  fnc.restype = ctypes.c_void_p
  fnc.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
  return ObjCInstance(fnc(directory, domainMask, expandTilde))

def get_toplevel_path(up_level: int=9) -> str:
  origin_path = './'
  parent_level = lambda l: '../' * int(l)
  return origin_path + parent_level(up_level)


libraryPath = NSSearchPathForDirectoriesInDomains(5, 1, True).firstObject()

path = get_toplevel_path() + str(libraryPath)
#print(path)
webbrowser.open(f'pythonista3://{path}')
