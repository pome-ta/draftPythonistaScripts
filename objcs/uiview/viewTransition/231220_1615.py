from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, ns, CGRect

import pdbg

# --- navigation
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

# --- viewController
UIViewController = ObjCClass('UIViewController')


class NavigationController:

  def __init__(self):
    self._navigationController: UINavigationController

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

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

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      appearance.configureWithDefaultBackground()

      # --- navigationBar
      navigationBar = navigationController.navigationBar()

      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance

      viewController.setEdgesForExtendedLayout_(0)

      done_btn = UIBarButtonItem.alloc(
      ).initWithBarButtonSystemItem_target_action_(0, navigationController,
                                                   sel('doneButtonTapped:'))

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


class _ViewController:

  def __init__(self):
    self._msgs: list['def'] = []  # xxx: 型ちゃんとやる
    self._viewController: UIViewController
    self.override()

  def override(self):
    # todo: objc でmethod 生やしたいときなど
    # xxx: wrap やりたい
    # [Pythonのデコレータにはwrapsをつけるべきという覚え書き #Python - Qiita](https://qiita.com/moonwalkerpoday/items/9bd987667a860adf80a2)
    pass

  def add_msg(self, method):
    self._msgs.append(method)

  def didLoad(self, this: UIViewController):
    pass

  def willAppear(self, this: UIViewController, animated: bool):
    pass

  def willLayoutSubviews(self, this: UIViewController):
    pass

  def didLayoutSubviews(self, this: UIViewController):
    pass

  def didAppear(self, this: UIViewController, animated: bool):
    pass

  def willDisappear(self, this: UIViewController, animated: bool):
    pass

  def didDisappear(self, this: UIViewController, animated: bool):
    pass

  def _override_viewController(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      self.didLoad(this)

    def viewWillAppear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.willAppear(this, animated)

    def viewWillLayoutSubviews(_self, _cmd):
      this = ObjCInstance(_self)
      self.willLayoutSubviews(this)

    def viewDidLayoutSubviews(_self, _cmd):
      this = ObjCInstance(_self)
      self.didLayoutSubviews(this)

    def viewDidAppear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.didAppear(this, animated)

    def viewWillDisappear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.willDisappear(this, animated)

    def viewDidDisappear_(_self, _cmd, animated):
      this = ObjCInstance(_self)
      self.didDisappear(this, animated)

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
    ]

    if self._msgs:
      _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    return vc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._init()


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()

  vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


### ### ###
# --- view
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIColor = ObjCClass('UIColor')
UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')


class FirstViewController(_ViewController):

  def __init__(self):
    super().__init__()
    self.nav_title = 'FirstViewController'
    self.sub_view = UIView.alloc()
    self.btn = UIButton.new()

  def override(self):

    def www(_self, _cmd):
      print('www')

    self.add_msg(www)

  def didLoad(self, this: UIViewController):
    view = this.view()
    view.setBackgroundColor_(UIColor.systemBlueColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view

    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_('tap')
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemGreenColor())

    self.btn.setConfiguration_(config)
    this.www()

    # --- layout
    view.addSubview_(self.btn)

    self.btn.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.btn.centerXAnchor().constraintEqualToAnchor_(view.centerXAnchor()),
      self.btn.centerYAnchor().constraintEqualToAnchor_(view.centerYAnchor()),
      self.btn.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.4),
      self.btn.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.1),
    ])


class SecondViewController(_ViewController):

  def __init__(self):
    self.nav_title = 'SecondViewController'
    self.sub_view = UIView.alloc()
    self.btn = UIButton.new()

  def didLoad(self, this: UIViewController):
    view = this.view()
    view.setBackgroundColor_(UIColor.systemGreenColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view

    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_('tap')
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemBlueColor())

    self.btn.setConfiguration_(config)

    # --- layout
    view.addSubview_(self.btn)

    self.btn.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.btn.centerXAnchor().constraintEqualToAnchor_(view.centerXAnchor()),
      self.btn.centerYAnchor().constraintEqualToAnchor_(view.centerYAnchor()),
      self.btn.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.4),
      self.btn.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.1),
    ])


if __name__ == '__main__':
  fvc = FirstViewController.new()
  nvc = NavigationController.new(fvc)
  present_objc(nvc)

