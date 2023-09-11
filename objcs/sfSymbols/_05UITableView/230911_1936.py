import ctypes
from objc_util import c, ObjCClass, ObjCInstance

UITableViewCell = ObjCClass('UITableViewCell')

NSStringFromClass = c.NSStringFromClass
NSStringFromClass.argtypes = [ctypes.c_void_p]
NSStringFromClass.restype = ctypes.c_void_p
'''
s = NSStringFromClass(UITableViewCell)

ss = ObjCInstance(s)
'''

for i in range(4):
  print(NSStringFromClass(UITableViewCell))

