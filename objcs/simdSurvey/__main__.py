from objc_util import c, load_framework, ObjCClass, ObjCInstance
import ctypes




#void vvceil(double *, const double *, const int *);

vvceil = c.vvceil

MTLCreateSystemDefaultDevice.argtypes = []
MTLCreateSystemDefaultDevice.restype = ctypes.c_void_p
m = ObjCInstance(MTLCreateSystemDefaultDevice())

