import ctypes

from objc_util import c, load_framework, ObjCClass, ObjCInstance,on_main_thread


# まだ動かない
_vvsqrtf = c.vvsqrtf
_vvsqrtf.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_int32]
#_vvsqrtf.restype = None

@on_main_thread
def main():
  x = 1000.0
  y = 1.0
  n = 1
  _vvsqrtf(x,y,n)

main()

'''
simd_equal = c.simd_equal

simd_equal.argtypes = []
simd_equal.restype = ctypes.c_void_p
m = ObjCInstance(simd_equal())
'''
