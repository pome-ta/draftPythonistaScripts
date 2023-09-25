from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIViewController = ObjCClass('UIViewController')


class ObjcUIViewController:

  def __init__(self):
    self._this: UIViewController
    self._override()

  def _override(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      #pdbg.state(this)

    def viewWillAppear_(_self, _cmd, _animated):
      print('viewWillAppear')

    def viewDidAppear_(_self, _cmd, _animated):
      print('viewDidAppear')

    def viewWillDisappear_(_self, _cmd, _animated):
      print('viewWillDisappear')

    def viewDidDisappear_(_self, _cmd, _animated):
      print('viewDidDisappear')

    def viewWillLayoutSubviews(_self, _cmd):
      print('viewWillLayoutSubviews')

    def viewDidLayoutSubviews(_self, _cmd):
      print('viewDidLayoutSubviews')

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._this = _vc.new()

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._this


@on_main_thread
def present_objc(vc):

  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow()
  root_vc = window.rootViewController()

  #pdbg.state(root_vc)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

