from ctypes import cdll, c_char_p, c_void_p
import sys

PY3 = sys.version_info[0] >= 3

_cached_classes = {}
c = cdll.LoadLibrary(None)

# objc_getClass: cdll = c.objc_getClass
# objc_getClass.argtypes = [c_char_p]
# objc_getClass.restype = c_void_p


def objc_getClass(objc_className: str) -> c_void_p:
  _func = c.objc_getClass
  _func.argtypes = [c_char_p]
  _func.restype = c_void_p
  return _func(objc_className)


class ObjCClass:

  def __new__(cls, name):
    if PY3 and isinstance(name, str):
      name = name.encode('ascii')
    # クラスを名前でメモ（毎回同じオブジェクトを取得）
    cached_class = _cached_classes.get(name)
    if cached_class:
      return cached_class
    cached_class = super(ObjCClass, cls).__new__(cls)
    return cached_class

  def __init__(self, name: str):
    if PY3 and isinstance(name, str):
      name = name.encode('ascii')
    self.ptr = objc_getClass(name)
    if self.ptr is None:
      raise ValueError(f'no Objective-C class named \'{name}\' found')
    self._as_parameter_ = self.ptr
    self.class_name = name
    self._cached_methods = {}

  def __str__(self) -> str:
    return f'<ObjCClass: {self.class_name}>'


if __name__ == '__main__':
  NSObject = ObjCClass('NSObject')
  NSDictionary = ObjCClass('NSDictionary')
  NSMutableDictionary = ObjCClass('NSMutableDictionary')
  NSArray = ObjCClass('NSArray')
  NSMutableArray = ObjCClass('NSMutableArray')
  NSSet = ObjCClass('NSSet')
  NSMutableSet = ObjCClass('NSMutableSet')
  NSString = ObjCClass('NSString')
  NSMutableString = ObjCClass('NSMutableString')
  NSData = ObjCClass('NSData')
  NSMutableData = ObjCClass('NSMutableData')
  NSNumber = ObjCClass('NSNumber')
  NSURL = ObjCClass('NSURL')
  NSEnumerator = ObjCClass('NSEnumerator')
  NSThread = ObjCClass('NSThread')
  NSBundle = ObjCClass('NSBundle')

  UIColor = ObjCClass('UIColor')
  UIImage = ObjCClass('UIImage')
  UIBezierPath = ObjCClass('UIBezierPath')
  UIApplication = ObjCClass('UIApplication')

