from ctypes import cdll, c_char_p, c_void_p
import sys



PY3 = sys.version_info[0] >= 3
_cached_classes = {}
c = cdll.LoadLibrary(None)


objc_getClass: cdll = c.objc_getClass
objc_getClass.argtypes = [c_char_p]
objc_getClass.restype = c_void_p


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
    print(name)
    _name = name.encode('ascii')
    print(_name)
    self.ptr = objc_getClass(_name)
    print(self.ptr)


if __name__ == '__main__':
  NSObject = ObjCClass('NSObject')
  print(PY3)
