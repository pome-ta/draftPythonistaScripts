from pyrubicon.objc.api import objc_const, ObjCInstance
from pyrubicon.objc.runtime import load_library

framework = load_library('UIKit')


def _get_const(global_variable_name) -> ObjCInstance:
  return objc_const(framework, global_variable_name)

