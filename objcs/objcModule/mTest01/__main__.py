from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import sel, CGRect

from objcista import ObjcNavigationController, UINavigationController
from objcista import ObjcViewController, UIViewController
from objcista import ObjcView, ObjcImageView
from objcista import present_run
from objcista.constants import *

UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')


class PlainNavigationController(ObjcNavigationController):

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):
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


class TopNavigationController(PlainNavigationController):

  def __init__(self):
    self.override()

  def override(self):

    @self.add_msg
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):

    appearance = UINavigationBarAppearance.alloc()
    appearance.configureWithDefaultBackground()
    # --- navigationBar
    navigationBar = navigationController.navigationBar()

    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    done_btn = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(0, navigationController,
                                                 sel('doneButtonTapped:'))

    visibleViewController = navigationController.visibleViewController()

    # --- navigationItem
    navigationItem = visibleViewController.navigationItem()

    navigationItem.rightBarButtonItem = done_btn


### ### ###
# --- main
### ### ###
UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')

UIImage = ObjCClass('UIImage')

UISheetPresentationControllerDetent = ObjCClass(
  'UISheetPresentationControllerDetent')

largeDetent = UISheetPresentationControllerDetent.largeDetent()
mediumDetent = UISheetPresentationControllerDetent.mediumDetent()


class ObjcLabel(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UILabel.new()
    self.instance.setText_(kwargs['text'])
    self.instance.sizeToFit()


class TopViewController(ObjcViewController):

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
      _type = UITableViewCell_AccessoryType.disclosureIndicator
      cell.setAccessoryType_(_type)

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


class SecondViewController(ObjcViewController):

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
      nav_con = nextResponder.navigationController()

      create_kwargs = {
        'name': 'HalfModal',
        'symbol_name': item,
      }

      hmvc = HalfModalViewController.new(**create_kwargs)
      sv = PlainNavigationController.new(hmvc)
      sheet = sv.sheetPresentationController()
      sheet.setDetents_([mediumDetent, largeDetent])
      sheet.setPrefersGrabberVisible_(True)
      nav_con.presentViewController_animated_completion_(sv, True, None)

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


class HalfModalViewController(ObjcViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self.nav_title = kwargs['name']
    self.nav_title = kwargs['symbol_name']
    self.symbol = kwargs['symbol_name']

  def override(self):
    pass

  def didLoad(self, this: UIViewController):
    view = this.view()

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    #view.setBackgroundColor_(UIColor.systemGray2Color())
    symbol_img = UIImage.systemImageNamed(self.symbol)
    self.symbol_view = ObjcImageView.new(image=symbol_img, LAYOUT_DEBUG=False)
    _mode = UIView_ContentMode.scaleAspectFit
    self.symbol_view.setContentMode_(_mode)

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
  nvc = TopNavigationController.new(tvc, True)
  present_run(nvc)

