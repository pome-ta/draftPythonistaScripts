from ctypes import c_bool, c_char_p, sizeof, c_void_p, cdll

LP64 = (sizeof(c_void_p) == 8)

c = cdll.LoadLibrary(None)

class_getName = c.class_getName
class_getName.restype = c_char_p
class_getName.argtypes = [c_void_p]

class_getSuperclass = c.class_getSuperclass
class_getSuperclass.restype = c_void_p
class_getSuperclass.argtypes = [c_void_p]

class_addMethod = c.class_addMethod
class_addMethod.restype = c_bool

if __name__ == '__main__':
  print(class_getName)
