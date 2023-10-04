from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import c, on_main_thread, sel, CGRect

import SystemColor as sc
import pdbg

file_name = Path(__file__).name

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

#pdbg.state(NSLayoutConstraint)


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
    self.redView: UIView
    self.yellowView: UIView

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      view.backgroundColor = sc.systemDarkGrayColor
      #pdbg.state(view.translatesAutoresizingMaskIntoConstraints())

      #view.translatesAutoresizingMaskIntoConstraints = False

      CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
      self.redView = UIView.alloc().initWithFrame_(CGRectZero)
      self.redView.backgroundColor = sc.systemRedColor
      self.redView.translatesAutoresizingMaskIntoConstraints = False

      self.yellowView = UIView.alloc().initWithFrame_(CGRectZero)
      self.yellowView.backgroundColor = sc.systemYellowColor
      self.yellowView.translatesAutoresizingMaskIntoConstraints = False

      view.addSubview_(self.redView)
      view.addSubview_(self.yellowView)

      #pdbg.state(view)
      '''

      tmp_frame = ((0.0, 0.0), (100.0, 100.0))

      sub_view = UIView.new()
      sub_view.setFrame_(tmp_frame)
      #sub_view.setAutoresizingMask_((1 << 1) | (1 << 4))
      sub_view.backgroundColor = sc.systemCyanColor
      view.addSubview_(sub_view)

      _frame = ((0.0, 0.0), (100.0, 100.0))
      label1 = UILabel.alloc().initWithFrame_(_frame)
      label1.text = 'ほげ'
      label2 = UILabel.alloc().initWithFrame_(_frame)
      label2.text = 'ほげ'

      #label2.setBackgroundColor_(sc.systemBrownColor)
      view.addSubview_(label1)
      view.addSubview_(label2)
      '''

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

      # [NSLayoutAttribute | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutattribute?language=objc)
      '''
      3:NSLayoutAttributeTop
      5:NSLayoutAttributeLeading
      4:NSLayoutAttributeBottom
      7:NSLayoutAttributeWidth
      
      '''
      # [NSLayoutRelation | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nslayoutrelation?language=objc)
      '''
      0:NSLayoutRelationEqual
      '''

      redViewTopConstraint = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        self.redView, 3, 0, view, 3, 1.0, 88)
      view.addConstraint_(redViewTopConstraint)

      redViewLeadingConstraint = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        self.redView, 5, 0, view, 5, 1.0, 10)
      view.addConstraint_(redViewLeadingConstraint)

      redViewBottonConstraint = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        self.redView, 4, 0, view, 4, 1.0, -20)
      view.addConstraint_(redViewBottonConstraint)

      redViewWidthConstraint = NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
        self.redView, 7, 0, view, 7, 0.4, 0)
      view.addConstraint_(redViewWidthConstraint)

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

