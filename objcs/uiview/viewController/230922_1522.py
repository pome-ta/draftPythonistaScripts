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
      this = ObjCInstance(_self)
      pdbg.state(this)

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
    #pdbg.state(_vc.new())
    self._this = _vc.new()


@on_main_thread
def present_objc(vc):
  app = UIApplication.sharedApplication()
  if app.keyWindow():
    print('t')
    window = app.keyWindow()
  else:
    print('f')
    window = app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  _vc_i = ObjcUIViewController()
  _vc = _vc_i._this
  present_objc(_vc)

