from objc_util import ObjCInstance, create_objc_class,class_getSuperclass,objc_getClass,objc_registerClassPair,objc_allocateClassPair

from objcista import *
import pdbg


def viewDidLoad(_self, _cmd):
  this = ObjCInstance(_self)
  #pdbg.state(this)
  #_allocateClassPair = objc_allocateClassPair(_self, 'vc', 0)
  #sc = objc_getClass(objc_registerClassPair(_self))
  #print(sc)
  #print((_cmd))
  pdbg.state(this)


_methods = [
  viewDidLoad,
]
create_kwargs = {
  'name': 'vc',
  'superclass': UIViewController,
  'methods': _methods,
}

if __name__ == "__main__":
  vc = create_objc_class(**create_kwargs)

  style = UIModalPresentationStyle.pageSheet
  run_controller(vc.new(), style)

