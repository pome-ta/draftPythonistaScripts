from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import on_main_thread, sel

import pdbg

file_name = Path(__file__).name

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')

UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIColor = ObjCClass('UIColor')
Red = UIColor.redColor()
BLUE = UIColor.blueColor()
CYAN = UIColor.cyanColor()


class ObjcUIViewController:

  def __init__(self):
    self._this: ObjCInstance
    self._viewController: UIViewController
    self._navigationController: UINavigationController

  @on_main_thread
  def _init(self):
    self._override_viewController()
    self._override_navigationController()

    vc = self._viewController.new().autorelease()
    nv = self._navigationController.alloc()
    nv.initWithRootViewController_(vc).autorelease()

    self._this = nv

  def _override_viewController(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      view.backgroundColor = Red

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()

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
    def doneButtonTapped_(_self, _cmd, _sender):
      ObjCInstance(_self).dismissViewControllerAnimated_completion_(True, None)

    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(this.presentingViewController())

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      '''
      presentedViewController
      presentingViewController  -> PASlidingContainerViewController
      parentModalViewController
      parentViewController
      childModalViewController
      '''
      #pdbg.state(this.presentingViewController())
      pdbg.state(this.topViewController())

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(this.childModalViewController())
      '''

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      appearance.configureWithOpaqueBackground()
      appearance.backgroundColor = BLUE

      # --- navigationBar
      navigationBar = this.navigationBar()

      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance


      _done_btn = UIBarButtonItem.alloc()
      done_btn = _done_btn.initWithBarButtonSystemItem_target_action_(
        0, this, sel('doneButtonTapped:'))

      # --- navigationItem
      navigationItem = this.navigationItem()
      navigationItem.setTitle_(str(file_name))

      navigationItem.leftBarButtonItem = done_btn
      '''

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
    navigationController_methods = [
      doneButtonTapped_,
      viewDidLoad,
      viewWillAppear_,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
    ]

    # --- `UINavigationControllerDelegate` Methods
    def navigationController_willShowViewController_animated_(
        _self, _cmd, _navigationController, _viewController, _animated):
      pass

    navigationController_create_kwargs = {
      'name': '_nv',
      'superclass': UINavigationController,
      'methods': navigationController_methods,
    }

    _nv = create_objc_class(**navigationController_create_kwargs)
    self._navigationController = _nv

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    _cls._init()
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
  #vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

