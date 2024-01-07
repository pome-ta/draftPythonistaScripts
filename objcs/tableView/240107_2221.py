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

UIViewContentModeScaleToFill = 0
UIViewContentModeScaleAspectFit = 1

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

UIGraphicsImageRenderer = ObjCClass('UIGraphicsImageRenderer')


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
    def setupTableView(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      self.cell_identifier: str = 'cell'
      self.table_extensions = self.create_table_extensions()

      self.tableView = ObjcTableView.new(style=UITableViewStylePlain)
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
        self.tableView.heightAnchor().constraintEqualToConstant_(512.0),
      ])

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    #view.setBackgroundColor_(UIColor.systemBlueColor())

    # --- view

    this.setupTableView()

    # --- layout

    views = [
      self.tableView,
    ]
    _pre_view = None
    activateConstraints = []
    for v in views:
      if _pre_view:
        activateConstraints.append(
          v.topAnchor().constraintEqualToAnchor_constant_(
            _pre_view.bottomAnchor(), 16.0))
      else:
        activateConstraints.append(v.topAnchor().constraintEqualToAnchor_(
          view.topAnchor()))

      _pre_view = v

    NSLayoutConstraint.activateConstraints_(activateConstraints)

  def create_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 3

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      #cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(self.cell_identifier, indexPath)

      cell = UITableViewCell.alloc().initWithStyle_reuseIdentifier_(
        UITableViewCellStyleValue1, self.cell_identifier)

      main_text = 'main' + str(indexPath.pt_row())
      #pdbg.state(indexPath.pt_row())
      secondary_text = 'secondary'

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(main_text)
      content.setSecondaryText_(secondary_text)
      #pdbg.state(content)

      cell.setContentConfiguration_(content)
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

  dummy_img_uri = '/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/test/Boat@2x.png'

  top_name = 'tv cell style test'
  fvc = TopViewController.new(name=top_name)
  nvc = NavigationController.new(fvc)
  present_objc(nvc)

