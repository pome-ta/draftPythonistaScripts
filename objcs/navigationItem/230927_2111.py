from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UIColor = ObjCClass('UIColor')


class ObjcUIViewController:

  def __init__(self):
    self._this: UIViewController
    self._override()

  def _override(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      navigationItem = this.navigationItem()
      navigationBar = navigationItem.navigationBar()
      #navigationItem.setTitle_('ほげ')
      view.backgroundColor = UIColor.cyanColor()
      #pdbg.state(view.window())
      #pdbg.state(view)
      #pdbg.state(navigationItem)
      #pdbg.state(navigationBar)
      #pdbg.state(this.navigationController())

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(window)
      #pdbg.state(this.navigationController())
      navigationItem = this.navigationItem()
      navigationBar = navigationItem.navigationBar()
      navigationItem.setTitle_('ほげ')

    def viewWillDisappear_(_self, _cmd, _animated):
      #print('viewWillDisappear')
      pass

    def viewDidDisappear_(_self, _cmd, _animated):
      #print('viewDidDisappear')
      pass

    def viewWillLayoutSubviews(_self, _cmd):
      #print('viewWillLayoutSubviews')
      pass

    def viewDidLayoutSubviews(_self, _cmd):
      #print('viewDidLayoutSubviews')
      pass

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
      #'superclass': UIViewController,
      'superclass': UINavigationController,
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
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()
  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()

  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

