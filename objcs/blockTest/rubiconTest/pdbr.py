from objc_util import ObjCInstance
import pdbg


def state(rubicon_obj):
  pdbg.state(ObjCInstance(rubicon_obj.ptr.value))

