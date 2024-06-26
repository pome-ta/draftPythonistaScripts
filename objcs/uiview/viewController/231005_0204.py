# [Auto Layoutをコードで書いてみた - Qiita](https://qiita.com/dddisk/items/8001598ea7951bcdcc30)

from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import SystemColor as sc
import pdbg

file_name = Path(__file__).name
#file_name = 'NSLayoutAnchor でレイアウト😤'

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')
#NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class NSLayoutAttribute:
  """
  [NSLayoutAttribute | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutattribute?language=objc)
  """
  left = 1
  right = 2
  top = 3
  bottom = 4
  leading = 5
  trailing = 6
  width = 7
  height = 8
  centerX = 9
  centerY = 10
  lastBaseline = 11
  firstBaseline = 12
  leftMargin = 13
  rightMargin = 14
  topMargin = 15
  bottomMargin = 16
  leadingMargin = 17
  trailingMargin = 18
  centerXWithinMargins = 19
  centerYWithinMargins = 20
  notAnAttribute = 0


class NSLayoutRelation:
  """
  [NSLayoutRelation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutrelation?language=objc)
  """
  lessThanOrEqual = -1
  equal = 0
  greaterThanOrEqual = 1


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

    self.redView = UIView.alloc()

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      view.backgroundColor = sc.systemDarkGrayColor

      CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
      self.redView.initWithFrame_(CGRectZero)
      #self.redView.initWithFrame_(view.frame())
      self.redView.backgroundColor = sc.systemRedColor
      self.redView.translatesAutoresizingMaskIntoConstraints = False

      view.addSubview_(self.redView)
      '''
      bottomAnchor
      centerXAnchor
      centerYAnchor
      firstBaselineAnchor
      heightAnchor
      lastBaselineAnchor
      leadingAnchor
      leftAnchor
      rightAnchor
      topAnchor
      trailingAnchor
      widthAnchor
      '''
      self.redView.centerXAnchor().constraintEqualToAnchor_(
        view.centerXAnchor()).setActive_(True)
      self.redView.centerYAnchor().constraintEqualToAnchor_(
        view.centerYAnchor()).setActive_(True)
      self.redView.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.5).setActive_(True)

      self.redView.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.9).setActive_(True)

      #pdbg.state(self.redView.widthAnchor())
      #pdbg.state(self.redView.heightAnchor().constraintEqualToAnchor_multiplier_(view.heightAnchor(), 0.5))

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

    def didReceiveMemoryWarning(_self, _cmd):
      # Dispose of any resources that can be recreated.
      print('Dispose of any resources that can be recreated.')

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
      didReceiveMemoryWarning,
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
      #view.backgroundColor = sc.systemWhiteColor
      view.backgroundColor = sc.systemDarkExtraLightGrayColor

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

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      appearance.configureWithDefaultBackground()
      #appearance.configureWithOpaqueBackground()
      #appearance.configureWithTransparentBackground()
      #appearance.backgroundColor = sc.systemExtraLightGrayColor

      # --- navigationBar
      navigationBar = navigationController.navigationBar()
      '''
      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance
      '''

      #navigationBar.prefersLargeTitles = True

      viewController.setEdgesForExtendedLayout_(0)
      #viewController.setExtendedLayoutIncludesOpaqueBars_(True)

      _done_btn = UIBarButtonItem.alloc()
      done_btn = _done_btn.initWithBarButtonSystemItem_target_action_(
        0, navigationController, sel('doneButtonTapped:'))

      topViewController = navigationController.topViewController()

      # --- navigationItem
      navigationItem = topViewController.navigationItem()

      navigationItem.standardAppearance = appearance
      navigationItem.scrollEdgeAppearance = appearance
      navigationItem.compactAppearance = appearance
      navigationItem.compactScrollEdgeAppearance = appearance

      navigationItem.setTitle_(str(file_name))
      navigationItem.rightBarButtonItem = done_btn

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


