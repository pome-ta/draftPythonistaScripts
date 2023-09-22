from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')


class ObjcUIViewController(object):
  
  def __init__(self):
    # xxx: 名前酷いけど取り急ぎ
    self._this: ObjCInstance
    self._override()

  def _override(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      pass

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
    ]
    
    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
      #'protocols': _protocols,
    }
    _vc = create_objc_class(**create_kwargs)
    pdbg.state(_vc.new())


@on_main_thread
def present_objc(vc):
  pass


if __name__ == '__main__':
  ObjcUIViewController()

