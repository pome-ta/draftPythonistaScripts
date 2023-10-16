import ctypes

from objc_util import c, load_framework, ObjCClass, ObjCInstance


# まだ動かない
_vvsqrtf = c.vvsqrtf
_vvsqrtf.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_int32]
_vvsqrtf.restype = ctypes.c_void_p


x = 



'''
simd_equal = c.simd_equal

simd_equal.argtypes = []
simd_equal.restype = ctypes.c_void_p
m = ObjCInstance(simd_equal())
'''
