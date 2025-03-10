# [https://github.com/pome-ta/pysta-icons/blob/master/sfSymbols4objcUtil.py](https://github.com/pome-ta/pysta-icons/blob/master/sfSymbols4objcUtil.py)

import re
from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg

# --- navigation
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UISearchController = ObjCClass('UISearchController')

# --- table
UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')

# --- viewController
UIViewController = ObjCClass('UIViewController')

# --- view
UIImage = ObjCClass('UIImage')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIColor = ObjCClass('UIColor')


def get_order_list():
  CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

  symbol_order_path = 'symbol_order.plist'
  symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

  order_list = plistlib.loads(symbol_order_bundle.read_bytes())
  return order_list


class ObjcUIViewController:

  def __init__(self):
    self._viewController: UIViewController

    # --- search
    self.searchController = UISearchController.alloc()
    self.search_extensions = self.create_search_extensions()

    self.nav_title = 'SF Symbols tableList 😤'

    # --- table
    self.all_items: list = get_order_list()
    self.all_items.sort()
    self.grep_items: list = []
    self.cell_identifier: str = 'cell'

    self.tableView = UITableView.new()
    self.table_extensions = self.create_table_extensions()

  def reload_items(self, target_text):
    # xxx: `ObjCInstance` で通っちゃってる?
    text = target_text if isinstance(target_text, str) else str(target_text)

    try:
      # xxx: 記号の処理対応
      prog = re.compile(text, flags=re.IGNORECASE)
      self.grep_items = [item for item in self.all_items if prog.search(item)]
    except:
      pass
    self.tableView.reloadData()

  def setup_viewDidLoad(self, this: UIViewController):
    # --- searchController
    self.searchController.initWithSearchResultsController(None)
    self.searchController.setSearchResultsUpdater(self.search_extensions)
    self.searchController.setObscuresBackgroundDuringPresentation(False)

    # --- navigationItem
    navigationItem = this.navigationItem()
    navigationItem.setTitle(self.nav_title)
    navigationItem.setSearchController(self.searchController)
    #navigationItem.setHidesSearchBarWhenScrolling_(True)
    navigationItem.setHidesSearchBarWhenScrolling(False)

    # --- tableView
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    # [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
    '''
    0 : UITableViewStylePlain
    1 : UITableViewStyleGrouped
    2 : UITableViewStyleInsetGrouped
    '''
    self.tableView.initWithFrame_(CGRectZero, style=0)
    self.tableView.registerClass(UITableViewCell,
                                 forCellReuseIdentifier=self.cell_identifier)
    self.tableView.setDataSource(self.table_extensions)
    self.tableView.setDelegate(self.table_extensions)
    # [UIScrollView.KeyboardDismissMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode)
    self.tableView.setKeyboardDismissMode(1)  # onDrag

  def _override_viewController(self):

    # --- `UIViewController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      this.dismissViewControllerAnimated_completion_(True, None)

    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      self.setup_navigation(this)
      self.setup_viewDidLoad(this)
      view = this.view()

      #this.setEdgesForExtendedLayout_(0)
      #this.setExtendedLayoutIncludesOpaqueBars_(True)

      # --- tableView layout
      view.addSubview_(self.tableView)
      self.tableView.translatesAutoresizingMaskIntoConstraints = False

      NSLayoutConstraint.activateConstraints([
        self.tableView.centerXAnchor().constraintEqualToAnchor(
          view.centerXAnchor()),
        self.tableView.centerYAnchor().constraintEqualToAnchor(
          view.centerYAnchor()),
        self.tableView.widthAnchor().constraintEqualToAnchor(
          view.widthAnchor(), multiplier=1.0),
        self.tableView.heightAnchor().constraintEqualToAnchor(
          view.heightAnchor(), multiplier=1.0),
      ])

    def didReceiveMemoryWarning(_self, _cmd):
      print('Dispose of any resources that can be recreated.')
      print('> 再作成可能なリソースは処分する。')

    # --- `UIViewController` set up
    _methods = [
      doneButtonTapped_,
      viewDidLoad,
      didReceiveMemoryWarning,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  def create_search_extensions(self):
    # --- `UISearchResultsUpdating` Methods
    def updateSearchResultsForSearchController_(_self, _cmd,
                                                _searchController):
      searchController = ObjCInstance(_searchController)
      text = searchController.searchBar().text()
      if text:
        self.reload_items(text)

    # --- `UISearchResultsUpdating` set up
    _methods = [
      updateSearchResultsForSearchController_,
    ]
    _protocols = [
      'UISearchResultsUpdating',
    ]

    create_kwargs = {
      'name': 'search_extensions',
      'methods': _methods,
      'protocols': _protocols,
    }

    search_extensions = create_objc_class(**create_kwargs)
    return search_extensions.new()

  def create_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      items = self.grep_items if self.grep_items else self.all_items
      #return len(items)
      return 1

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier(
        self.cell_identifier, forIndexPath=indexPath)

      #pdbg.state(cell.contentView().subviews().objectAtIndexedSubscript_(0))
      pdbg.state(cell.contentView())
      items = self.grep_items if self.grep_items else self.all_items

      cell_text = items[indexPath.row()]
      cell_image = UIImage.systemImageNamed(cell_text)

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines(1)
      content.setText(cell_text)
      content.setImage(cell_image)

      cell.setContentConfiguration_(content)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)
      items = self.grep_items if self.grep_items else self.all_items
      item = items[indexPath.row()]
      print(f'{indexPath}: {item}')

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

  def setup_navigation(self, this: UIViewController):
    # todo: view 閉じる用の実装など
    navigationController = this.navigationController()
    navigationBar = navigationController.navigationBar()

    # --- appearance
    appearance = UINavigationBarAppearance.alloc()
    appearance.configureWithDefaultBackground()
    #appearance.configureWithOpaqueBackground()
    #appearance.configureWithTransparentBackground()

    # --- navigationBar
    navigationBar.standardAppearance = appearance
    navigationBar.scrollEdgeAppearance = appearance
    navigationBar.compactAppearance = appearance
    navigationBar.compactScrollEdgeAppearance = appearance

    navigationBar.prefersLargeTitles = True
    #navigationController.setHidesBarsOnSwipe_(True)

    done_btn = UIBarButtonItem.alloc().initWithBarButtonSystemItem(
      0, target=this, action=sel('doneButtonTapped:'))

    navigationItem = this.navigationItem()
    navigationItem.rightBarButtonItem = done_btn

  @on_main_thread
  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    nv = UINavigationController.alloc()
    nv.initWithRootViewController(vc).autorelease()
    return nv

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
  '''
  case -2 : automatic
  case -1 : none
  case  0 : fullScreen
  case  1 : pageSheet <- default ?
  case  2 : formSheet
  case  3 : currentContext
  case  4 : custom
  case  5 : overFullScreen
  case  6 : overCurrentContext
  case  7 : popover
  case  8 : blurOverFullScreen
  '''
  vc.setModalPresentationStyle(0)
  root_vc.presentViewController(vc, animated=True, completion=None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)


