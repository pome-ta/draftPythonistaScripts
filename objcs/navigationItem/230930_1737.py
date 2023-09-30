from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import on_main_thread

import pdbg

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')

UIColor = ObjCClass('UIColor')

#pdbg.state(UINavigationBarAppearance.new())


class ObjcUIViewController:

  def __init__(self):
    self._this: UIViewController | UINavigationController
    self._viewController: UIViewController
    self._navigationController: UINavigationController

  @on_main_thread
  def init(self):
    #self._override_navigationController()
    #self._this = self._navigationController.new()
    self._override_viewController()
    vc = self._viewController.new()
    nv = UINavigationController.alloc()
    nv.initWithRootViewController_(vc)

    _nva = UINavigationBarAppearance.new()
    navigationBarAppearance = _nva.configureWithDefaultBackground()
    
    #pdbg.state(navigationBarAppearance)

    self._this = nv

  def _override_viewController(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      view.backgroundColor = UIColor.redColor()
      this.navigationItem().setTitle_('ほげ')

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(this)

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
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()

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
    self._viewController = _vc

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def viewDidLoad(_self, _cmd):
      print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      this.navigationItem().setTitle_('ほげ')

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(this)
      pdbg.mthd(view)

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
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()

    # --- `UINavigationController` set up
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
      'name': '_nc',
      'superclass': UINavigationController,
      'methods': _methods,
    }
    _nc = create_objc_class(**create_kwargs)
    self._navigationController = _nc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    _cls.init()
    return _cls._this


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()
  '''
  case -2 : automatic
  case -1 : none
  case  0 : fullScreen
  case  1 : pageSheet <- default ?
  case  2 : formSheet
  case  3 : currentContext
  case  4 : custom
  case  5 : overFullScreen
  case  6 : overCurrentContext
  case  7 : popover
  case  8 : blurOverFullScreen
  '''
  vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

