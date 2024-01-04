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
NSTextAlignmentCenter = 1
UITextField = ObjCClass('UITextField')
UITextFieldViewModeAlways = 3
NSAttributedString = ObjCClass('NSAttributedString')

UIFont = ObjCClass('UIFont')

UIScrollView = ObjCClass('UIScrollView')

UISwitch = ObjCClass('UISwitch')

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6

dummy_img_uri = '/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/test/Boat@2x.png'

UIStackView = ObjCClass('UIStackView')
UILayoutConstraintAxisHorizontal = 0
UILayoutConstraintAxisVertical = 1

UIStackViewAlignmentFill = 0
UIStackViewAlignmentLeading = 1
UIStackViewAlignmentFirstBaseline = 2
UIStackViewAlignmentCenter = 3
UIStackViewAlignmentTrailing = 4
UIStackViewAlignmentLastBaseline = 5
UIStackViewAlignmentTop = UIStackViewAlignmentLeading
UIStackViewAlignmentBottom = UIStackViewAlignmentTrailing

UIStackViewDistributionFill = 0
UIStackViewDistributionFillEqually = 1
UIStackViewDistributionFillProportionally = 2
UIStackViewDistributionEqualSpacing = 3
UIStackViewDistributionEqualCentering = 4


class ObjcView:

  def __init__(self, *args, **kwargs):
    self.instance = UIView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.instance.initWithFrame_(CGRectZero)

  def _init(self):

    if IS_LAYOUT_DEBUG:
      color = UIColor.systemRedColor()
      self.instance.layer().setBorderWidth_(1.0)
      self.instance.layer().setBorderColor_(color.cgColor())
    self.instance.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.instance

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init()


class ObjcStackView(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UIStackView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.instance.initWithFrame_(CGRectZero)


class ObjcImageView(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UIImageView.alloc().initWithImage_(kwargs['image'])


class ObjcLabel(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UILabel.new()
    self.instance.setText_(kwargs['text'])
    self.instance.sizeToFit()


class ObjcTextField(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UITextField.new()


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
    def setupHeaderStack(_self, _cmd):
      # xxx: `return` 調べてないので`self` で全体的に持つ
      this = ObjCInstance(_self)
      view = this.view()
      # --- stack init
      self.header_stack = ObjcStackView.new()
      self.header_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      self.header_stack.setAlignment_(UIStackViewAlignmentCenter)

      # --- stack items
      self.header_icon_img = UIImage.imageWithContentsOfFile_(
        str(self.dummy_img_path))
      self.header_icon = ObjcImageView.new(image=self.header_icon_img)
      self.header_icon.setContentMode_(scaleAspectFit)
      #self.header_icon.setBackgroundColor_(UIColor.systemRedColor())

      self.header_label = ObjcLabel.new(text=self.nav_title)
      self.header_label.setTextAlignment_(NSTextAlignmentCenter)
      self.header_label.setFont_(UIFont.systemFontOfSize_(48.0))

      # --- layout
      self.header_stack.addArrangedSubview_(self.header_icon)
      self.header_stack.addArrangedSubview_(self.header_label)
      view.addSubview_(self.header_stack)

      layoutMarginsGuide = view.layoutMarginsGuide()

      NSLayoutConstraint.activateConstraints_([
        self.header_stack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.header_stack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.header_stack.widthAnchor().constraintEqualToAnchor_multiplier_(
          layoutMarginsGuide.widthAnchor(), 1.0),
        self.header_stack.heightAnchor().constraintEqualToConstant_(80.0),
        self.header_icon.widthAnchor().constraintEqualToAnchor_(
          self.header_stack.heightAnchor()),
        self.header_icon.heightAnchor().constraintEqualToAnchor_(
          self.header_stack.heightAnchor()),
      ])

    @self.add_msg
    def setupUIDStack(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      # --- stack init
      self.uid_stack = ObjcStackView.new()
      self.uid_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      self.uid_stack.setAlignment_(UIStackViewAlignmentFill)

      self.uid_stack.setSpacing_(16.0)

      # --- stack items
      self.uid_label = ObjcLabel.new(text='UID:')
      self.uid_textfield = ObjcTextField.new()
      placeholder = NSAttributedString.alloc().initWithString_(
        'input to UID ...')
      self.uid_textfield.setAttributedPlaceholder_(placeholder)
      #self.uid_textfield.setBackgroundColor_(UIColor.systemDarkGrayColor())
      self.uid_textfield.setBackgroundColor_(UIColor.systemDarkRedColor())
      #systemDarkExtraLightGrayColor
      #systemDarkLightGrayColor
      #systemDarkGrayColor
      #pdbg.state(self.uid_textfield.layer())
      self.uid_textfield.layer().setCornerRadius_(16)
      self.uid_textfield.setClipsToBounds_(True)
      self.uid_textfield.setClearButtonMode_(UITextFieldViewModeAlways)
      
      pdbg.state(self.uid_textfield)

      # --- layout
      self.uid_stack.addArrangedSubview_(self.uid_label)
      self.uid_stack.addArrangedSubview_(self.uid_textfield)

      view.addSubview_(self.uid_stack)

      layoutMarginsGuide = view.layoutMarginsGuide()
      NSLayoutConstraint.activateConstraints_([
        self.uid_stack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.uid_stack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.uid_stack.heightAnchor().constraintEqualToConstant_(32.0),
      ])

    @self.add_msg
    def setupUserRankStack(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()

      # --- stack init
      self.userrank_stack = ObjcStackView.new()
      self.userrank_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      self.userrank_stack.setDistribution_(UIStackViewDistributionEqualSpacing)

      self.userrank_stack.setAlignment_(UIStackViewAlignmentFill)

      self.userrank_stack.setSpacing_(16.0)
      #pdbg.state(self.userrank_stack)

      # --- stack items
      font_size = UIFont.systemFontOfSize_(16.0)
      # --- leading
      leading_stack = ObjcStackView.new()
      leading_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      leading_stack.setAlignment_(UIStackViewAlignmentFill)
      leading_stack.setSpacing_(8.0)

      self.username_key_label = ObjcLabel.new(text='ユーザー名:')
      self.username_key_label.setFont_(font_size)
      self.username_value_label = ObjcLabel.new(text='hogehoge fugapiyooo hogehoge')
      self.username_value_label.setFont_(font_size)
      leading_stack.addArrangedSubview_(self.username_key_label)
      leading_stack.addArrangedSubview_(self.username_value_label)

      # --- trailing

      trailing_stack = ObjcStackView.new()
      trailing_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      trailing_stack.setAlignment_(UIStackViewAlignmentFill)
      trailing_stack.setSpacing_(8.0)

      self.worldrank_key_label = ObjcLabel.new(text='世界ランク:')
      self.worldrank_key_label.setFont_(font_size)

      self.worldrank_value_label = ObjcLabel.new(text='60')
      self.worldrank_value_label.setFont_(font_size)

      trailing_stack.addArrangedSubview_(self.worldrank_key_label)
      trailing_stack.addArrangedSubview_(self.worldrank_value_label)

      # --- layout
      self.userrank_stack.addArrangedSubview(leading_stack)
      self.userrank_stack.addArrangedSubview(trailing_stack)
      view.addSubview_(self.userrank_stack)

      layoutMarginsGuide = view.layoutMarginsGuide()
      NSLayoutConstraint.activateConstraints_([
        self.userrank_stack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.userrank_stack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.userrank_stack.heightAnchor().constraintEqualToConstant_(32.0),
        #leading_stack.widthAnchor().constraintEqualToAnchor_multiplier_(layoutMarginsGuide.widthAnchor(), 0.7),
        #trailing_stack.widthAnchor().constraintEqualToAnchor_multiplier_(layoutMarginsGuide.widthAnchor(), 0.3),
      ])

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    #view.setBackgroundColor_(UIColor.systemBlueColor())

    # --- view
    self.main_stack = ObjcStackView.new()
    this.setupHeaderStack()
    this.setupUIDStack()
    this.setupUserRankStack()

    # --- layout
    NSLayoutConstraint.activateConstraints_([
      self.header_stack.topAnchor().constraintEqualToAnchor_(view.topAnchor()),
      self.uid_stack.topAnchor().constraintEqualToAnchor_constant_(
        self.header_stack.bottomAnchor(), 16.0),
      self.userrank_stack.topAnchor().constraintEqualToAnchor_constant_(
        self.uid_stack.bottomAnchor(), 16.0),
    ])


if __name__ == '__main__':
  IS_LAYOUT_DEBUG = True
  IS_LAYOUT_DEBUG = False
  top_name = 'Artifacter'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)

