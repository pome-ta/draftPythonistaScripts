import webbrowser
import ctypes
from pathlib import Path
import urllib.parse

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

# todo: NSSearchPathDirectory
developerApplicationDirectory = 3
libraryDirectory = 5
NSAutosavedInformationDirectory = 11

# todo: NSSearchPathDomainMask
NSUserDomainMask = 1
NSAllDomainsMask = 0x0ffff
libraryPath = NSSearchPathForDirectoriesInDomains(102, 0x0ffff, True).firstObject()

_path = get_toplevel_path() + str(libraryPath)
#print(path)
path = urllib.parse.quote(_path)
webbrowser.open(f'pythonista3://{path}')
