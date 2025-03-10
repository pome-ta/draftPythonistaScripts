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
from pathlib import Path

UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')
UIColor = ObjCClass('UIColor')

UIImage = ObjCClass('UIImage')
UIImageView = ObjCClass('UIImageView')
#[UIView.ContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/contentmode)
scaleAspectFit = 1

UILabel = ObjCClass('UILabel')
#pdbg.state(UILabel.alloc())

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6

IS_LAYOUT_DEBUG = True

#/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/test/Boat@2x.png

dummy_img_uri = '/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/test/Boat@2x.png'


class WrapView:

  def __init__(self, *args, **kwargs):
    self.view = UIView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.view.initWithFrame_(CGRectZero)

  def _init(self):

    if IS_LAYOUT_DEBUG:
      self.view.layer().setBorderWidth_(1.0)
    self.view.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.view

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init()


class WrapImageView(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UIImageView.alloc().initWithImage_(kwargs['image'])


class WrapLabelView(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UILabel.new()
    self.view.setText_(kwargs['text'])
    self.view.sizeToFit()


class TopViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']

    self.dummy_img_path = Path(dummy_img_uri)
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
    self.header_view.setBackgroundColor_(UIColor.systemRedColor())

    #self.header_icon_view = UIImageView.alloc()
    self.header_icon_img = UIImage.imageWithContentsOfFile_(
      str(self.dummy_img_path))

    #self.header_icon_view = UIImageView.alloc().initWithImage_(self.header_icon_img)

    self.header_icon_view = WrapImageView.new(image=self.header_icon_img)
    self.header_icon_view.setContentMode_(scaleAspectFit)
    #pdbg.state(self.header_icon_view)
    #setContentMode
    
    self.header_label = WrapLabelView.new(text=self.nav_title)
    #pdbg.state(self.header_label)

    self.header_view.addSubview_(self.header_icon_view)
    self.header_view.addSubview_(self.header_label)

    self.uid_view = WrapView.new()
    self.uid_view.setBackgroundColor_(UIColor.systemGreenColor())

    # --- layout
    view.addSubview_(self.header_view)
    view.addSubview_(self.uid_view)

    layoutMarginsGuide = view.layoutMarginsGuide()
    #pdbg.state(layoutMarginsGuide)

    NSLayoutConstraint.activateConstraints_([
      # --- header_main
      self.header_view.topAnchor().constraintEqualToAnchor_(
        view.topAnchor()),  # todo: top 定義しないと、子view のYセンター軸が定義できない
      self.header_view.leadingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor()),
      self.header_view.trailingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor()),
      self.header_view.widthAnchor().constraintEqualToAnchor_multiplier_(
        layoutMarginsGuide.widthAnchor(), 1.0),
      self.header_view.heightAnchor().constraintEqualToConstant_(80.0),

      # --- img
      self.header_icon_view.widthAnchor().constraintEqualToAnchor_multiplier_(
        self.header_view.heightAnchor(), 1.0),
      self.header_icon_view.heightAnchor().constraintEqualToAnchor_multiplier_(
        self.header_view.heightAnchor(), 1.0),
      #self.header_icon_view.centerYAnchor().constraintEqualToAnchor_multiplier_(self.header_view.heightAnchor(),0.5),
      self.header_icon_view.centerYAnchor().constraintEqualToAnchor_(
        self.header_view.centerYAnchor()),
      
      # --- label
      self.header_label.trailingAnchor().constraintEqualToAnchor_(
        self.header_view.trailingAnchor()),
      self.header_label.centerYAnchor().constraintEqualToAnchor_(
        self.header_view.centerYAnchor()),
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

  def didLayoutSubviews(self, this: UIViewController):
    #pdbg.state()
    #print('j')
    #pdbg.state(self.header_view.centerYAnchor().constraintsAffectingLayout())
    pass


if __name__ == '__main__':
  top_name = 'Artifacter'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)

