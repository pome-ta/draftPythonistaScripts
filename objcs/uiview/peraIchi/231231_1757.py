from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

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
      """（自身の）アプリケーション終了
      `NavigationController` から生やした`done_btn` ボタンのアクション
      
      """
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

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型ちゃんとやる
    self._viewController: UIViewController
    self.override()

  def override(self):
    # todo: objc で特別にmethod 生やしたいときなど
    pass

  def add_msg(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

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

    if self._msgs: _methods.extend(self._msgs)

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
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
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
NSLayoutDimension = ObjCClass('NSLayoutDimension')

dim = NSLayoutDimension.new()
#pdbg.state(dim.constraintEqualToConstant_(40.0))

#constraintEqualToConstant

UIColor = ObjCClass('UIColor')
UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6




class WrapView:

  def __init__(self):
    self.view = UIView.alloc()

  def _init(self):
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.view.initWithFrame_(CGRectZero)
    self.view.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.view

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._init()


class TopViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']

    self.header_view: UIView
    self.uid_view: UIView

  def override(self):

    @self.add_msg
    def btnClick_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      sender = ObjCInstance(_sender)


  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    view.setBackgroundColor_(UIColor.systemBlueColor())
    self.header_view = WrapView.new()
    self.uid_view = WrapView.new()
    
    self.header_view.layer().setBorderWidth_(1.0)
    #pdbg.state(self.header_view.layer())

    self.header_view.setBackgroundColor_(UIColor.systemRedColor())
    self.uid_view.setBackgroundColor_(UIColor.systemGreenColor())

    # --- layout
    view.addSubview_(self.header_view)
    view.addSubview_(self.uid_view)

    
    layoutMarginsGuide = view.layoutMarginsGuide()

    NSLayoutConstraint.activateConstraints_([
      self.header_view.leadingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor()),
      self.header_view.trailingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor()),
      self.header_view.widthAnchor().constraintEqualToAnchor_multiplier_(
        layoutMarginsGuide.widthAnchor(), 1.0),
      self.header_view.heightAnchor().constraintEqualToConstant_(80.0),
    ])
    NSLayoutConstraint.activateConstraints_([
      self.uid_view.topAnchor().constraintEqualToAnchor_constant_(
        self.header_view.bottomAnchor(), 8.0),
      self.uid_view.leadingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor()),
      self.uid_view.trailingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor()),
      self.uid_view.heightAnchor().constraintEqualToConstant_(32.0),
    ])


if __name__ == '__main__':
  top_name = 'Artifacter'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)

