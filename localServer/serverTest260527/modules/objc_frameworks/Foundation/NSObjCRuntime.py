from pyrubicon.objc.api import ObjCInstance
from pyrubicon.objc.runtime import Foundation, Class, objc_id


def NSStringFromClass(cls: Class) -> ObjCInstance:
  '''
  ref: [NSObjCRuntime.rs - source](https://docs.rs/objc2-foundation/latest/src/objc2_foundation/generated/NSObjCRuntime.rs.html#382-389)
  '''
  try:
    _func = NSStringFromClass._cfunc
  except AttributeError:
    _func = Foundation.NSStringFromClass
    _func.restype = objc_id
    _func.argtypes = [Class]
    NSStringFromClass._cfunc = _func

  return ObjCInstance(_func(cls))

