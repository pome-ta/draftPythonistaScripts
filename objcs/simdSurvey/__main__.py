from objc_util import c, load_framework, ObjCClass, ObjCInstance
import ctypes

# まだ動かない

simd_equal = c.simd_equal

simd_equal.argtypes = []
simd_equal.restype = ctypes.c_void_p
m = ObjCInstance(simd_equal())

