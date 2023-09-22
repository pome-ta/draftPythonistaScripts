# [https://github.com/tdamdouni/Pythonista/blob/master/objc/objc-get-names.py](https://github.com/tdamdouni/Pythonista/blob/master/objc/objc-get-names.py)

# coding: utf-8

# https://forum.omz-software.com/topic/2808/bug-objc_util-and-dir

import ctypes
import re
from pprint import pprint
from objc_util import ObjCClass, c

import pdbg

objc_getClassList = c.objc_getClassList
objc_getClassList.restype = ctypes.c_int
objc_getClassList.argtypes = [ctypes.c_void_p, ctypes.c_int]

class_getName = c.class_getName
class_getName.restype = ctypes.c_char_p
class_getName.argtypes = [ctypes.c_void_p]

num_classes = objc_getClassList(None, 0)
buffer = (ctypes.c_void_p * num_classes)()
objc_getClassList(buffer, num_classes)

class_names = [class_getName(b).decode('ascii') for b in buffer]
class_names.sort()


target = 'PAS'

#prog = re.compile(target, flags=re.IGNORECASE)
prog = re.compile(target)
grep_names =  [c_name for c_name in class_names if prog.search(c_name)]
#pprint(class_names)

pprint(grep_names)

