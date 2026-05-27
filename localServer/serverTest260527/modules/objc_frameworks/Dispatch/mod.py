import ctypes
import functools

from pyrubicon.objc.api import ObjCInstance
from pyrubicon.objc.runtime import libobjc, objc_block, objc_id

dispatch_time_t = ctypes.c_uint64

# DISPATCH_TIME_FOREVER (~0ull)
DISPATCH_TIME_FOREVER = dispatch_time_t(2**64 - 1)  # ~0ull
DISPATCH_TIME_NOW = dispatch_time_t(0)


class struct_dispatch_queue_s(ctypes.Structure):
  pass  # No _fields_, because this is an opaque structure.


_dispatch_main_q = struct_dispatch_queue_s.in_dll(libobjc, '_dispatch_main_q')


def dispatch_get_main_queue():
  return ObjCInstance(ctypes.cast(ctypes.byref(_dispatch_main_q), objc_id))


def dispatch_sync(queue, block_obj:objc_block):
  try:
    _func = dispatch_sync._cfunc
  except AttributeError:
    _func = libobjc.dispatch_sync
    _func.restype = None
    _func.argtypes = [
      objc_id,
      objc_block,
    ]
    dispatch_sync._cfunc = _func
  
  _func(queue, block_obj)
  

def dispatch_async(queue, block_obj:objc_block):
  try:
    _func = dispatch_async._cfunc
  except AttributeError:
    _func = libobjc.dispatch_async
    _func.restype = None
    _func.argtypes = [
      objc_id,
      objc_block,
    ]
    dispatch_async._cfunc = _func
  
  _func(queue, block_obj)
  
  

def dispatch_semaphore_create(value: int) -> ObjCInstance | None:
  try:
    _func = dispatch_semaphore_create._cfunc
  except AttributeError:
    _func = libobjc.dispatch_semaphore_create
    _func.restype = objc_id
    _func.argtypes = [
      ctypes.c_long,
    ]
    dispatch_semaphore_create._cfunc = _func

  return _ptr if (_ptr := _func(value)) is None else ObjCInstance(_ptr)


def dispatch_semaphore_wait(dsema: ObjCInstance, timeout: int = None) -> int:
  try:
    _func = dispatch_semaphore_wait._cfunc
  except AttributeError:
    _func = libobjc.dispatch_semaphore_wait
    _func.restype = ctypes.c_long
    _func.argtypes = [
      objc_id,
      ctypes.c_uint64,
    ]
    dispatch_semaphore_wait._cfunc = _func

  t = DISPATCH_TIME_FOREVER if timeout is None else timeout

  return _func(dsema, t)


def dispatch_semaphore_signal(dsema: ObjCInstance) -> int:
  try:
    _func = dispatch_semaphore_signal._cfunc
  except AttributeError:
    _func = libobjc.dispatch_semaphore_signal
    _func.restype = ctypes.c_long
    _func.argtypes = [
      objc_id,
    ]
    dispatch_semaphore_signal._cfunc = _func

  return _func(dsema)

