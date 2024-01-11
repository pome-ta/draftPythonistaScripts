from pathlib import Path
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UsrAgn = 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'


class Artifacter:

  def __init__(self, uid):
    self.uid = uid
    ThreadPoolExecutor().submit(self.Initialization).result()

  def Initialization(self):
    # データの表記名データをEnka.Network公式Githubから取得
    #self.locale_jp = ThreadPoolExecutor().submit(self.locale).result()
    # キャラクターデータをEnka.Network公式Githubから取得
    #self.characters_json = ThreadPoolExecutor().submit(self.character_json).result()
    #self.costumes = ThreadPoolExecutor().submit(self.costume_json).result()

    url = f'https://enka.network/api/uid/{self.uid}'
    try:

      req = urllib.request.Request(url, headers={'User-Agent': UsrAgn})
      print('r')
      print(req)
      json_data = urllib.request.urlopen(req).read().decode(errors='ignore')
      self.player_data = json.loads(json_data)
    except:
      self.player_data = {}

  def main(self):
    print('o')

'''
if __name__ == '__main__':
  uid_path = Path('./uid.txt')
  UID = uid_path.read_text()
  artifacter = Artifacter(UID)
  print('h')
  #ThreadPoolExecutor().submit(artifacter.main)


[https://github.com/pome-ta/draftPythonistaScripts/blob/main/objcs/uiview/peraIchi/240109_2331.py](https://github.com/pome-ta/draftPythonistaScripts/blob/main/objcs/uiview/peraIchi/240109_2331.py)
'''

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
      """(自身の)アプリケーション終了
      `NavigationController` から生やした`done_btn` ボタンのアクション
      
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

UIKeyboardTypeDefault = 0
UIKeyboardTypeNumbersAndPunctuation = 2
UIKeyboardTypeNumberPad = 4
UIKeyboardTypeASCIICapableNumberPad = 11
UIReturnKeySearch = 6

NSAttributedString = ObjCClass('NSAttributedString')

UIFont = ObjCClass('UIFont')

UIScrollView = ObjCClass('UIScrollView')

UISwitch = ObjCClass('UISwitch')

UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6
UIControlEventValueChanged = 1 << 12

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

UITableView = ObjCClass('UITableView')
UITableViewStylePlain = 0

UITableViewCell = ObjCClass('UITableViewCell')
UITableViewCellStyleDefault = 0
UITableViewCellStyleValue1 = 1
UITableViewCellStyleValue2 = 2
UITableViewCellStyleSubtitle = 3


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


class ObjcTableView(ObjcView):

  def __init__(self, *args, **kwargs):
    self.instance = UITableView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    style = kwargs['style'] if kwargs['style'] else UITableViewStylePlain
    self.instance.initWithFrame_style_(CGRectZero, style)


class ObjcSwitch(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UISwitch.new()


class ObjcButton(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UIButton.new()
    title = kwargs['title']
    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_(title)
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemGreenColor())

    self.instance.setConfiguration_(config)


###
# --- TopViewController
###


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
      print('h')

    @self.add_msg
    def changeSwitch_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      sender = ObjCInstance(_sender)
      if sender.isOn():
        [switch.setOn_animated_(False, True) for switch in self.switches]
        sender.setOn_animated_(True, True)

    @self.add_msg
    def setupHeaderStack(_self, _cmd):
      # xxx: `return` 調べてないので`self` で全体的に持つ
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
        self.header_stack.heightAnchor().constraintEqualToConstant_(64.0),
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

      # --- stack items
      self.uid_label = ObjcLabel.new(text='UID:')
      self.uid_text_wrap = ObjcView.new()
      self.uid_text_wrap.layer().setCornerRadius_(16)
      #self.uid_text_wrap.setBackgroundColor_(UIColor.systemDarkGrayColor())
      self.uid_text_wrap.setBackgroundColor_(UIColor.systemGray3Color())

      self.uid_textfield = ObjcTextField.new()

      delegate = self.create_textField_delegate()
      self.uid_textfield.setDelegate_(delegate)

      self.uid_textfield.textInputTraits().setKeyboardType_(
        UIKeyboardTypeNumbersAndPunctuation)

      self.uid_textfield.textInputTraits().setReturnKeyType_(UIReturnKeySearch)

      placeholder = NSAttributedString.alloc().initWithString_(
        'input to UID ...')
      self.uid_textfield.setAttributedPlaceholder_(placeholder)
      self.uid_textfield.setClearButtonMode_(UITextFieldViewModeAlways)

      # --- layout
      self.uid_text_wrap.addSubview_(self.uid_textfield)

      self.uid_stack.addArrangedSubview_(self.uid_label)
      self.uid_stack.addArrangedSubview_(self.uid_text_wrap)

      view.addSubview_(self.uid_stack)

      layoutMarginsGuide = view.layoutMarginsGuide()
      NSLayoutConstraint.activateConstraints_([
        self.uid_stack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.uid_stack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.uid_stack.heightAnchor().constraintEqualToConstant_(32.0),
        self.uid_label.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.uid_stack.widthAnchor(), 0.1),
        self.uid_text_wrap.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.uid_stack.widthAnchor(), 0.86),
        self.uid_textfield.centerXAnchor().constraintEqualToAnchor_(
          self.uid_text_wrap.centerXAnchor()),
        self.uid_textfield.centerYAnchor().constraintEqualToAnchor_(
          self.uid_text_wrap.centerYAnchor()),
        self.uid_textfield.widthAnchor().constraintEqualToAnchor_constant_(
          self.uid_text_wrap.widthAnchor(), -32),
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

      # --- stack items
      font_size = UIFont.systemFontOfSize_(12.0)
      # --- leading
      leading_stack = ObjcStackView.new()
      leading_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      leading_stack.setAlignment_(UIStackViewAlignmentFill)

      self.username_key_label = ObjcLabel.new(text='ユーザー名:')
      self.username_key_label.setFont_(font_size)
      self.username_value_label = ObjcLabel.new(text='')
      #self.username_value_label = ObjcLabel.new(text='hogehoge fugapiyooo fugapiyooo')

      self.username_value_label.setFont_(font_size)
      leading_stack.addArrangedSubview_(self.username_key_label)
      leading_stack.addArrangedSubview_(self.username_value_label)

      # --- trailing

      trailing_stack = ObjcStackView.new()
      trailing_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      trailing_stack.setAlignment_(UIStackViewAlignmentFill)

      self.worldrank_key_label = ObjcLabel.new(text='世界ランク:')
      self.worldrank_key_label.setFont_(font_size)

      #self.worldrank_value_label = ObjcLabel.new(text='60')
      self.worldrank_value_label = ObjcLabel.new(text='')
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
        leading_stack.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.userrank_stack.widthAnchor(), 0.64),
        self.username_key_label.widthAnchor().
        constraintEqualToAnchor_multiplier_(leading_stack.widthAnchor(), 0.3),
        self.username_value_label.widthAnchor().
        constraintEqualToAnchor_multiplier_(leading_stack.widthAnchor(), 0.7),
        trailing_stack.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.userrank_stack.widthAnchor(), 0.28),
        self.worldrank_key_label.widthAnchor(
        ).constraintEqualToAnchor_multiplier_(trailing_stack.widthAnchor(),
                                              0.64),
        self.worldrank_value_label.widthAnchor(
        ).constraintEqualToAnchor_multiplier_(trailing_stack.widthAnchor(),
                                              0.36),
      ])

    @self.add_msg
    def setupTableView(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      self.cell_identifier: str = 'cell'
      self.table_extensions = self.create_table_extensions()

      self.tableView = ObjcTableView.new(style=UITableViewStylePlain)

      self.tableView.layer().setBorderWidth_(2.0)
      self.tableView.layer().setCornerRadius_(8)
      self.tableView.layer().setBorderColor_(
        UIColor.systemGray6Color().cgColor())
      self.tableView.registerClass_forCellReuseIdentifier_(
        UITableViewCell, self.cell_identifier)

      self.tableView.setDataSource(self.table_extensions)
      self.tableView.setDelegate(self.table_extensions)

      # --- layout
      view.addSubview_(self.tableView)
      layoutMarginsGuide = view.layoutMarginsGuide()
      NSLayoutConstraint.activateConstraints_([
        self.tableView.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.tableView.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.tableView.heightAnchor().constraintEqualToConstant_(128.0),
      ])

    @self.add_msg
    def setupSwitchStack(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      self.switchStack = ObjcStackView.new()
      #self.switchStack.setAlignment_(UIStackViewAlignmentFill)
      self.switchStack.setAxis_(UILayoutConstraintAxisVertical)

      leading_stack = ObjcStackView.new()
      leading_stack.setAxis_(UILayoutConstraintAxisVertical)
      leading_stack.setAlignment_(UIStackViewAlignmentFill)
      leading_stack.setSpacing_(16.0)
      trailing_stack = ObjcStackView.new()
      trailing_stack.setAxis_(UILayoutConstraintAxisVertical)
      trailing_stack.setAlignment_(UIStackViewAlignmentFill)
      #trailing_stack.setSpacing_(16.0)

      labels = [
        'HP換算:',
        '攻撃力換算:',
        '防御力換算:',
        'チャージ換算:',
        '熟知換算:',
      ]

      self.hp_switch = ObjcSwitch.new()
      self.power_switch = ObjcSwitch.new()
      self.defence_switch = ObjcSwitch.new()
      self.charge_switch = ObjcSwitch.new()
      self.familiarity_switch = ObjcSwitch.new()

      self.switches = [
        self.hp_switch,
        self.power_switch,
        self.defence_switch,
        self.charge_switch,
        self.familiarity_switch,
      ]

      font_size = UIFont.systemFontOfSize_(12.0)

      for n, (s, l) in enumerate(zip(self.switches, labels)):
        _stack = ObjcStackView.new()
        _stack.setAxis_(UILayoutConstraintAxisHorizontal)
        #_stack.setAlignment_(UIStackViewAlignmentFill)
        _stack.setAlignment_(UIStackViewAlignmentCenter)

        #_stack.setSpacing_(16.0)
        s.addTarget_action_forControlEvents_(this, sel('changeSwitch:'),
                                             UIControlEventValueChanged)
        _label = ObjcLabel.new(text=l)
        _label.setFont_(font_size)
        _stack.addArrangedSubview_(_label)
        _stack.addArrangedSubview_(s)
        NSLayoutConstraint.activateConstraints_([
          _stack.heightAnchor().constraintEqualToConstant_(32.0),
        ])
        leading_stack.addArrangedSubview_(
          _stack) if n < 3 else trailing_stack.addArrangedSubview_(_stack)

      wrap_stack = ObjcStackView.new()
      wrap_stack.setAxis_(UILayoutConstraintAxisHorizontal)
      wrap_stack.setAlignment_(UIStackViewAlignmentFill)
      #wrap_stack.setSpacing_(24.0)

      wrap_stack.addArrangedSubview_(leading_stack)
      wrap_stack.addArrangedSubview_(trailing_stack)

      computation_view = ObjcLabel.new(text='計算方式')
      self.switchStack.addArrangedSubview_(computation_view)
      self.switchStack.addArrangedSubview_(wrap_stack)
      view.addSubview_(self.switchStack)

      layoutMarginsGuide = view.layoutMarginsGuide()
      NSLayoutConstraint.activateConstraints_([
        self.switchStack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.switchStack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        leading_stack.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.switchStack.widthAnchor(), 0.36),
        trailing_stack.widthAnchor().constraintEqualToAnchor_multiplier_(
          self.switchStack.widthAnchor(), 0.36),
      ])

    @self.add_msg
    def setupButton(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()

      self.button_stack = ObjcStackView.new()
      self.make_button = ObjcButton.new(title='作成')
      self.make_button.addTarget_action_forControlEvents_(
        this, sel('btnClick:'), UIControlEventTouchUpInside)

      self.button_stack.addArrangedSubview_(self.make_button)
      view.addSubview_(self.button_stack)
      layoutMarginsGuide = view.layoutMarginsGuide()

      NSLayoutConstraint.activateConstraints_([
        self.button_stack.leadingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.leadingAnchor()),
        self.button_stack.trailingAnchor().constraintEqualToAnchor_(
          layoutMarginsGuide.trailingAnchor()),
        self.button_stack.heightAnchor().constraintEqualToConstant_(64.0),
      ])

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    #view.setBackgroundColor_(UIColor.systemBlueColor())

    # --- view
    #self.main_stack = ObjcStackView.new()
    this.setupHeaderStack()
    this.setupUIDStack()
    this.setupUserRankStack()
    this.setupTableView()
    this.setupSwitchStack()
    this.setupButton()

    # --- layout

    views = [
      self.header_stack,
      self.uid_stack,
      self.userrank_stack,
      self.tableView,
      self.switchStack,
      self.button_stack,
    ]
    _pre_view = None
    activateConstraints = []
    for v in views:
      if _pre_view:
        activateConstraints.append(
          v.topAnchor().constraintEqualToAnchor_constant_(
            _pre_view.bottomAnchor(), 32.0))
      else:
        activateConstraints.append(v.topAnchor().constraintEqualToAnchor_(
          view.topAnchor()))

      _pre_view = v

    NSLayoutConstraint.activateConstraints_(activateConstraints)

  def create_textField_delegate(self):
    # --- `UITextFieldDelegate` Methods
    def textFieldShouldReturn_(_self, _cmd, _textField):
      textField = ObjCInstance(_textField)
      textField.resignFirstResponder()
      #print(textField)
      #pdbg.state(textField.text())
      input_text = textField.text()
      self.artifacter = Artifacter(str(input_text))
      playerInfo = self.artifacter.player_data['playerInfo']
      nickname = playerInfo['nickname']
      level = playerInfo['level']
      #print(type(t))
      #print(t)
      #print(str(t))
      self.username_value_label.setText_(nickname)
      self.worldrank_value_label.setText_(str(level))
      #artifacter.player_data['playerInfo']['nickname']
      return True

    # --- `UITextFieldDelegate` set up
    _methods = [
      textFieldShouldReturn_,
    ]
    _protocols = [
      'UITextFieldDelegate',
    ]

    create_kwargs = {
      'name': 'textField_delegate',
      'methods': _methods,
      'protocols': _protocols,
    }

    textField_delegate = create_objc_class(**create_kwargs)
    return textField_delegate.new()

  def create_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      #return len(self.table_items)
      return 1

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      cell = UITableViewCell.alloc().initWithStyle_reuseIdentifier_(
        UITableViewCellStyleValue1, self.cell_identifier)

      main_text = 'main' + str(indexPath.pt_row())
      secondary_text = 'secondary'

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(main_text)
      content.setSecondaryText_(secondary_text)

      cell.setContentConfiguration_(content)

      content = cell.defaultContentConfiguration()
      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)

    # --- `UITableViewDataSource` & `UITableViewDelegate` set up
    _methods = [
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
      numberOfSectionsInTableView_,
      tableView_didSelectRowAtIndexPath_,
    ]
    _protocols = [
      'UITableViewDataSource',
      'UITableViewDelegate',
    ]

    create_kwargs = {
      'name': 'table_extensions',
      'methods': _methods,
      'protocols': _protocols,
    }

    table_extensions = create_objc_class(**create_kwargs)
    return table_extensions.new()


if __name__ == '__main__':
  IS_LAYOUT_DEBUG = True
  #IS_LAYOUT_DEBUG = False
  top_name = 'Artifacter'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)


