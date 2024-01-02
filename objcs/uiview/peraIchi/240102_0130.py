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
UITextField = ObjCClass('UITextField')
NSAttributedString = ObjCClass('NSAttributedString')

UIScrollView = ObjCClass('UIScrollView')

UISwitch = ObjCClass('UISwitch')

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6

IS_LAYOUT_DEBUG = True

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


class WrapTextFieldView(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UITextField.new()


class WrapScrollView(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UIScrollView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.view.initWithFrame_(CGRectZero)


class WrapSwitch(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UISwitch.new()


class WrapButton(WrapView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.view = UIButton.new()
    title = kwargs['title']
    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_(title)
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemGreenColor())

    self.view.setConfiguration_(config)


class TopViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']

    self.dummy_img_path = Path(dummy_img_uri)

  def override(self):

    @self.add_msg
    def btnClick_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      sender = ObjCInstance(_sender)

    @self.add_msg
    def roughSetLayouts_(_self, _cmd, _views):
      this = ObjCInstance(_self)
      view = this.view()
      layoutMarginsGuide = view.layoutMarginsGuide()

      views = ObjCInstance(_views)

      pre_child = None
      for child in views:
        view.addSubview_(child)

        NSLayoutConstraint.activateConstraints_([
          child.topAnchor().constraintEqualToAnchor_(pre_child.bottomAnchor())
          if pre_child else child.topAnchor().constraintEqualToAnchor_(
            view.topAnchor()),
          child.leadingAnchor().constraintEqualToAnchor_(
            layoutMarginsGuide.leadingAnchor()),
          child.trailingAnchor().constraintEqualToAnchor_(
            layoutMarginsGuide.trailingAnchor()),
        ])

        # xxx: ひでーけど、取り急ぎ(特定のclass かどうかを知りたい)
        if str(child)[:12] == '<UIImageView':
          NSLayoutConstraint.activateConstraints_([
            child.widthAnchor().constraintEqualToConstant_(48.0),
            child.heightAnchor().constraintEqualToConstant_(48.0),
          ])
        if str(child)[:13] == '<UIScrollView':
          NSLayoutConstraint.activateConstraints_([
            child.widthAnchor().constraintEqualToAnchor_multiplier_(
              layoutMarginsGuide.widthAnchor(), 1.0),
            child.heightAnchor().constraintEqualToAnchor_multiplier_(
              layoutMarginsGuide.widthAnchor(), 0.5),
          ])

        pre_child = child

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    view.setBackgroundColor_(UIColor.systemBlueColor())

    # xxx: 雑に並べていく
    self.header_icon_img = UIImage.imageWithContentsOfFile_(
      str(self.dummy_img_path))

    self.header_icon = WrapImageView.new(image=self.header_icon_img)
    self.header_icon.setContentMode_(scaleAspectFit)

    self.header_label = WrapLabelView.new(text=self.nav_title)

    self.uid_label = WrapLabelView.new(text='UID:')

    placeholder = NSAttributedString.alloc().initWithString_('📝 ここに、UID を入力 🥺')
    self.uid_textfield = WrapTextFieldView.new()
    self.uid_textfield.setAttributedPlaceholder_(placeholder)

    self.username_key_label = WrapLabelView.new(text='ユーザー名:')
    self.username_value_label = WrapLabelView.new(text='ここにユーザー名が入る？😂')

    self.worldrank_key_label = WrapLabelView.new(text='世界ランク:')
    self.worldrank_value_label = WrapLabelView.new(text='ここに世界ランクが入る?😂')

    self.result_scroll = WrapScrollView.new()
    self.result_scroll.setContentSize_((0.0, 1024.0))
    self.result_scroll.setBackgroundColor_(UIColor.systemRedColor())
    #pdbg.state(self.result_scroll)

    self.computation_view = WrapLabelView.new(text='計算方式')

    self.hp_label = WrapLabelView.new(text='HP(換算):')
    self.hp_switch = WrapSwitch.new()
    self.power_label = WrapLabelView.new(text='攻撃力(換算):')
    self.power_switch = WrapSwitch.new()
    self.defence_label = WrapLabelView.new(text='防御(換算):')
    self.defence_switch = WrapSwitch.new()
    self.charge_label = WrapLabelView.new(text='元素チャージ効率(換算):')
    self.charge_switch = WrapSwitch.new()

    self.familiarity_label = WrapLabelView.new(text='熟知(換算):')
    self.familiarity_switch = WrapSwitch.new()

    self.btn = WrapButton.new(title='作成')

    # todo: layout
    this.roughSetLayouts_([
      self.header_icon,
      self.header_label,
      self.uid_label,
      self.uid_textfield,
      self.username_key_label,
      self.username_value_label,
      self.worldrank_key_label,
      self.worldrank_value_label,
      self.result_scroll,
      self.computation_view,
      self.hp_label,
      self.hp_switch,
      self.power_label,
      self.power_switch,
      self.defence_label,
      self.defence_switch,
      self.charge_label,
      self.charge_switch,
      self.familiarity_label,
      self.familiarity_switch,
      self.btn,
    ])


if __name__ == '__main__':
  top_name = 'Artifacter'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)





