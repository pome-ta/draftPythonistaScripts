from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import on_main_thread, sel

from SystemColor import systemDarkBlueColor, systemGray2Color, systemCyanColor, systemBrownColor, systemBackgroundColor, systemTealColor
import pdbg

file_name = Path(__file__).name

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')

UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')


class ObjcUIViewController:

  def __init__(self):
    self._this: ObjCInstance
    self._viewController: UIViewController
    self._navigationController: UINavigationController
    self._nvDelegate: 'UINavigationControllerDelegate'

  @on_main_thread
  def _init(self):
    self._override_viewController()
    self._override_navigationController()
    self._nvDelegate = self.create_navigationControllerDelegate()

    vc = self._viewController.new().autorelease()
    nv = self._navigationController.alloc()
    nv.initWithRootViewController_(vc).autorelease()
    nv.setDelegate_(self._nvDelegate)
    self._this = nv

  def _override_viewController(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      #view.backgroundColor = Red
      view.backgroundColor = systemGray2Color

      tmp_frame = ((0.0, 0.0), (100.0, 100.0))

      sub_view = UIView.new()
      sub_view.setFrame_(tmp_frame)
      #sub_view.setAutoresizingMask_((1 << 1) | (1 << 4))
      sub_view.backgroundColor = systemCyanColor
      view.addSubview_(sub_view)

      _frame = ((0.0, 0.0), (100.0, 100.0))
      label1 = UILabel.alloc().initWithFrame_(_frame)
      label1.text = 'ほげ'
      label2 = UILabel.alloc().initWithFrame_(_frame)
      label2.text = 'ほげ'

      label2.setBackgroundColor_(systemBrownColor)
      #pdbg.state(label1)
      view.addSubview_(label1)
      view.addSubview_(label2)
      #pdbg.state(this)
      #pdbg.state(this.edgesForExtendedLayout())

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
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      topViewController = this.topViewController()
      topViewController.dismissViewControllerAnimated_completion_(True, None)

    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      pdbg.state(window)

    # --- `UIViewController` set up
    _methods = [
      doneButtonTapped_,
      viewDidLoad,
    ]

    create_kwargs = {
      'name': '_nv',
      'superclass': UINavigationController,
      'methods': _methods,
    }
    _nv = create_objc_class(**create_kwargs)
    self._navigationController = _nv

  def create_navigationControllerDelegate(self):
    # --- `UINavigationControllerDelegate` Methods
    def navigationController_willShowViewController_animated_(
        _self, _cmd, _navigationController, _viewController, _animated):

      navigationController = ObjCInstance(_navigationController)
      viewController = ObjCInstance(_viewController)

      view = navigationController.view()
      window = view.window()

      #window.backgroundColor = systemDarkBlueColor

      #pdbg.state(navigationController.view().window().backgroundColor())

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      #pdbg.state(appearance)
      #appearance.configureWithOpaqueBackground()
      appearance.configureWithDefaultBackground()
      #appearance.configureWithTransparentBackground()

      #appearance.backgroundColor = BLUE
      #window.backgroundColor = systemTealColor

      # --- navigationBar
      navigationBar = navigationController.navigationBar()

      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance

      navigationBar.prefersLargeTitles = True

      viewController.setEdgesForExtendedLayout_(0)

      #navigationController.setExtendedLayoutIncludesOpaqueBars_(True)
      #viewController.setExtendedLayoutIncludesOpaqueBars_(True)
      #print(navigationController.edgesForExtendedLayout())
      #print(navigationController.extendedLayoutIncludesOpaqueBars())
      #print(navigationBar.isTranslucent())
      #print(this.isTranslucent())
      #pdbg.state(navigationController)
      #pdbg.state(navigationBar)

      _done_btn = UIBarButtonItem.alloc()
      done_btn = _done_btn.initWithBarButtonSystemItem_target_action_(
        0, navigationController, sel('doneButtonTapped:'))

      topViewController = navigationController.topViewController()

      # --- navigationItem
      navigationItem = topViewController.navigationItem()
      navigationItem.setTitle_(str(file_name))
      navigationItem.rightBarButtonItem = done_btn

      #pdbg.state(navigationController.automaticallyAdjustsScrollViewInsets())

    def navigationController_didShowViewController_animated_(
        _self, _cmd, _navigationController, _viewController, _animated):
      #print('did')
      pass

    # --- `UINavigationControllerDelegate` set up
    _methods = [
      navigationController_willShowViewController_animated_,
      navigationController_didShowViewController_animated_,
    ]
    _protocols = [
      'UINavigationControllerDelegate',
    ]

    create_kwargs = {
      'name': '_nvDelegate',
      'methods': _methods,
      'protocols': _protocols,
    }
    _nvDelegate = create_objc_class(**create_kwargs)
    return _nvDelegate.new()

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
  vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

