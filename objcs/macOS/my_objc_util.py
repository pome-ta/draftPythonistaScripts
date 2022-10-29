from ctypes import cdll, c_char_p, c_void_p

c = cdll.LoadLibrary(None)


objc_getClass: cdll = c.objc_getClass
objc_getClass.argtypes = [c_char_p]
objc_getClass.restype = c_void_p


class ObjCClass:
  def __init__(self, name: str):
    print(name)
    _name = name.encode('ascii')
    print(_name)
    self.ptr = objc_getClass(_name)
    print(self.ptr)


if __name__ == '__main__':
  NSObject = ObjCClass('NSObject')
