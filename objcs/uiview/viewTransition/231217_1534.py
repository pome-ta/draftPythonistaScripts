from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg

# --- navigation
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

# --- viewController
UIViewController = ObjCClass('UIViewController')

# --- view
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIColor = ObjCClass('UIColor')


class CustomViewController:

  def __init__(self):
    self._viewController: UIViewController
    self.nav_title = 'nav title'
    self.sub_view = UIView.alloc()

  def setup_viewDidLoad(self, this: UIViewController):
    # xxx: `viewDidLoad` が肥大化しそうなので、レイアウト関係以外はこっちで処理
    view = this.view()

    view.setBackgroundColor_(UIColor.systemBlueColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.sub_view.initWithFrame_(CGRectZero)
    self.sub_view.setBackgroundColor_(UIColor.systemRedColor())

  def _override_viewController(self):

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      self.setup_viewDidLoad(this)
      view = this.view()

      # --- layout
      view.addSubview_(self.sub_view)
      self.sub_view.translatesAutoresizingMaskIntoConstraints = False

      NSLayoutConstraint.activateConstraints_([
        self.sub_view.centerXAnchor().constraintEqualToAnchor(
          view.centerXAnchor()),
        self.sub_view.centerYAnchor().constraintEqualToAnchor(
          view.centerYAnchor()),
        self.sub_view.widthAnchor().constraintEqualToAnchor(view.widthAnchor(),
                                                            multiplier=0.9),
        self.sub_view.heightAnchor().constraintEqualToAnchor(
          view.heightAnchor(), multiplier=0.9),
      ])

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  #@on_main_thread
  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    return vc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._init()


class ObjcUIViewController:

  def __init__(self):
    self._navigationController: UINavigationController

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated(True,
                                                          completion=None)

    # --- `UINavigationController` set up
    _methods = [
      doneButtonTapped_,
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
      viewController.setEdgesForExtendedLayout_(0)

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      appearance.configureWithDefaultBackground()

      # --- navigationBar
      navigationBar = navigationController.navigationBar()

      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance

      done_btn = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
        0, target=navigationController, action=sel('doneButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()
      navigationItem.rightBarButtonItem = done_btn

    # --- `UINavigationControllerDelegate` set up
    _methods = [
      navigationController_willShowViewController_animated_,
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

  @on_main_thread
  def _init(self, vc: UIViewController):
    self._override_navigationController()
    _delegate = self.create_navigationControllerDelegate()
    nv = self._navigationController.alloc()
    nv.initWithRootViewController_(vc).autorelease()
    nv.setDelegate_(_delegate)
    return nv

  @classmethod
  def new(cls, vc: UIViewController) -> ObjCInstance:
    _cls = cls()
    return _cls._init(vc)


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()
  vc.setModalPresentationStyle(0)
  root_vc.presentViewController(vc, animated=True, completion=None)


if __name__ == '__main__':
  cvc = CustomViewController.new()
  ovc = ObjcUIViewController.new(cvc)
  present_objc(ovc)

