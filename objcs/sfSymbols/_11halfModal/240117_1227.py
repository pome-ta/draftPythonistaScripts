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
# --- main
### ### ###
UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

UILabel = ObjCClass('UILabel')

scaleAspectFit = 1

disclosureIndicator = 1

pageSheet = 1

UISheetPresentationControllerDetent = ObjCClass(
  'UISheetPresentationControllerDetent')
#pdbg.state(UISheetPresentationControllerDetent)

largeDetent = UISheetPresentationControllerDetent.largeDetent()
mediumDetent = UISheetPresentationControllerDetent.mediumDetent()


class ObjcView:

  def __init__(self, *args, **kwargs):
    self.instance = UIView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.instance.initWithFrame_(CGRectZero)

  def _init(self):

    if 'IS_LAYOUT_DEBUG' in globals() and IS_LAYOUT_DEBUG:
      color = UIColor.systemRedColor()
      self.instance.layer().setBorderWidth_(1.0)
      self.instance.layer().setBorderColor_(color.cgColor())
    self.instance.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.instance

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init()


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


class TopViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']
    self.bundles = kwargs['_bundles']

    self.categories = self.bundles.categories
    # --- table
    self.tableView = UITableView.new()
    self.cell_identifier: str = 'cell'
    self.table_extensions = self.create_table_extensions()

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    # --- tableView
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.tableView.initWithFrame(CGRectZero, style=0)
    self.tableView.registerClass_forCellReuseIdentifier_(
      UITableViewCell, self.cell_identifier)

    self.tableView.setDataSource(self.table_extensions)
    self.tableView.setDelegate(self.table_extensions)

    # --- layout
    view.addSubview(self.tableView)
    self.tableView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      #self.tableView.leadingAnchor().constraintEqualToAnchor_(layoutMarginsGuide.leadingAnchor()),
      #self.tableView.trailingAnchor().constraintEqualToAnchor_(layoutMarginsGuide.trailingAnchor()),
      self.tableView.centerXAnchor().constraintEqualToAnchor_(
        view.centerXAnchor()),
      self.tableView.centerYAnchor().constraintEqualToAnchor_(
        view.centerYAnchor()),
      self.tableView.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 1.0),
      self.tableView.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 1.0),
    ])

  def create_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return len(self.categories)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      item = self.categories[indexPath.row()]
      cell_text = item['key']
      cell_image = UIImage.systemImageNamed(item['icon'])
      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(cell_text)
      content.setImage_(cell_image)

      cell.setContentConfiguration_(content)
      cell.setAccessoryType_(disclosureIndicator)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)
      this = ObjCInstance(_self)
      tableView = ObjCInstance(_tableView)

      nextResponder = tableView.superview().nextResponder()
      navigationController = nextResponder.navigationController()

      item = self.categories[indexPath.row()]
      cell_text = item['key']
      svc = SecondViewController.new(select=cell_text, _bundles=self.bundles)
      navigationController.pushViewController_animated_(svc, True)
      #tableView.deselectRowAtIndexPath_animated_(indexPath, True)

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


class SecondViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.select = kwargs['select']
    self.nav_title = self.select
    self.bundles = kwargs['_bundles']

    self.symbol_categories = self.bundles.symbol_categories

    self.table_items = [
      key for key, value in self.symbol_categories.items()
      if self.select in value
    ] if self.select != 'all' else list(self.symbol_categories.keys())

    # --- table
    self.tableView = UITableView.new()
    self.cell_identifier: str = 'cell'
    self.table_extensions = self.create_table_extensions()

  def didLoad(self, this: UIViewController):
    view = this.view()
    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    # --- tableView
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.tableView.initWithFrame(CGRectZero, style=0)
    self.tableView.registerClass_forCellReuseIdentifier_(
      UITableViewCell, self.cell_identifier)

    self.tableView.setDataSource(self.table_extensions)
    self.tableView.setDelegate(self.table_extensions)

    # --- layout
    view.addSubview(self.tableView)
    self.tableView.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.tableView.centerXAnchor().constraintEqualToAnchor_(
        view.centerXAnchor()),
      self.tableView.centerYAnchor().constraintEqualToAnchor_(
        view.centerYAnchor()),
      self.tableView.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 1.0),
      self.tableView.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 1.0),
    ])

  def create_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return len(self.table_items)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      cell_text = self.table_items[indexPath.row()]
      cell_image = UIImage.systemImageNamed(cell_text)

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(cell_text)
      content.setImage_(cell_image)

      cell.setContentConfiguration_(content)
      #cell.setAccessoryType_(disclosureIndicator)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      item = self.table_items[indexPath.row()]

      nextResponder = tableView.superview().nextResponder()
      #pdbg.state(nextResponder.navigationController().navigationBar().bounds().size.height)
      #pdbg.state(nextResponder.navigationItem())
      navigationController = nextResponder.navigationController()

      create_kwargs = {
        'name': 'HalfModal',
        'symbol_name': item,
      }

      hmvc = HalfModalViewController.new(**create_kwargs)
      #pdbg.state(hmvc.navigationItem())
      '''
      navigationItem = hmvc.navigationItem()

      label = ObjcLabel.new(text=str(item))
      height = navigationController.navigationBar().bounds().size.height

      NSLayoutConstraint.activateConstraints_([
        label.heightAnchor().constraintEqualToConstant_(height),
        label.widthAnchor().constraintEqualToConstant_(height),
      ])
      '''

      #navigationItem.setTitle_(str(item))
      #navigationItem.setTitleView_(label)
      #pdbg.state(navigationItem)

      sheet = hmvc.sheetPresentationController()
      sheet.setDetents_([mediumDetent, largeDetent])
      sheet.setPrefersGrabberVisible_(True)
      #pdbg.state(sheet)
      #hmvc.navigationItem().setTitle_(str(item))
      #pdbg.state(hmvc.navigationController())

      navigationController.presentViewController_animated_completion_(
        hmvc, True, None)

      #tableView.deselectRowAtIndexPath_animated_(indexPath, True)

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


class HalfModalViewController(_ViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']
    self.symbol = kwargs['symbol_name']

  def override(self):
    pass

  def didLoad(self, this: UIViewController):
    view = this.view()

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)
    #pdbg.state(this.navigationItem())

    # --- view
    #view.setBackgroundColor_(UIColor.systemPinkColor())
    view.setBackgroundColor_(UIColor.systemGray6Color())
    symbol_img = UIImage.systemImageNamed(self.symbol)
    self.symbol_view = ObjcImageView.new(image=symbol_img)
    self.symbol_view.setContentMode_(scaleAspectFit)

    # --- layout
    view.addSubview_(self.symbol_view)
    layoutMarginsGuide = view.layoutMarginsGuide()

    NSLayoutConstraint.activateConstraints_([
      self.symbol_view.leadingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.leadingAnchor()),
      self.symbol_view.trailingAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.trailingAnchor()),
      self.symbol_view.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.5),
    ])

  def didDisappear(self, this: UIViewController, animated):
    pdbg.all(this)


### ### ###
# --- .plist
### ### ###
from pathlib import Path
import plistlib
'''
symbol_categories
symbol_search
legacy_flippable
nofill_to_fill
name_availability
symbol_restrictions
name_aliases
semantic_to_descriptive_name
categories
symbol_order
'''

CoreGlyphs_ROOT = '/System/Library/CoreServices/CoreGlyphs.bundle/'

IGNORE_SUFFIXS = [
  '.car',
]
IGNORE_NAMES = [
  'Info.plist',
]


# xxx: ↓ あんまり意味ないかも
class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self


def get_plistdata(path: Path | str) -> list | dict:
  _data_path = Path(path) if type(path) == 'str' else path
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def is_ignore(path: Path) -> bool:
  return not path.is_file()\
    or path.suffix in IGNORE_SUFFIXS\
    or path.name in IGNORE_NAMES


if __name__ == '__main__':
  IS_LAYOUT_DEBUG = True
  paths = {
    bundle.stem: get_plistdata(bundle)
    for bundle in Path(CoreGlyphs_ROOT).iterdir() if not is_ignore(bundle)
  }

  bundles = DictDotNotation(paths)
  name = 'SF Symbols'
  tvc = TopViewController.new(name=name, _bundles=bundles)
  nvc = NavigationController.new(tvc)
  present_objc(nvc)

