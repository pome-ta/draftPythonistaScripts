# [[iOS 11] iOS 11で追加されたUINavigationItemのsearchControllerプロパティを使ってSearchBarをナビゲーションインターフェースに統合する | DevelopersIO](https://dev.classmethod.jp/articles/ios-11-uinavigationitem-searchcontroller/)

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
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIColor = ObjCClass('UIColor')

all_items = [
  'Swift',
  'Java',
  'Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,Java,',
  'Ruby',
  'C++',
  'C',
  'C#',
  'Python',
  'Perl',
  'JavaScript',
  'PHP',
  'Scratch',
  'Scala',
  'COBOL',
  'Curl',
  'Dart',
  'HTML',
  'CSS',
  'Ruby on Rails',
  'TypeScript',
  'ECMAScript',
  'Jython',
  'CPython',
  'PyPy',
  'IronPython',
]


class ObjcUIViewController:

  def __init__(self):
    self.items: list = all_items
    self.cell_identifier: str = 'cell'

    self._this: ObjCInstance
    self._viewController: UIViewController
    self._table_extensions: 'Protocol'
    self.searchController: UISearchController

  @on_main_thread
  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    nv = UINavigationController.alloc()
    nv.initWithRootViewController_(vc).autorelease()
    self._this = nv

  def _override_viewController(self):
    self.searchController = UISearchController.alloc()
    self.tableView = UITableView.new()

    # --- `UIViewController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      this.dismissViewControllerAnimated_completion_(True, None)

    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      self.nav_setup(this)
      view = this.view()

      #view.backgroundColor = systemDarkBlueColor
      #view.backgroundColor = systemDarkMidGrayColor
      
      CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
      

    def didReceiveMemoryWarning(_self, _cmd):
      # Dispose of any resources that can be recreated.
      print('Dispose of any resources that can be recreated.')

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

  @property
  def table_extensions(self):
    return self._table_extensions.new()

  def _init_table_extensions(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return len(self.items)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      # xxx: `dequeueReusableCellWithIdentifier_forIndexPath_` は、落ちる? -> `numberOfSectionsInTableView_` 定義しないと落ちる
      #cell = tableView.dequeueReusableCellWithIdentifier_(self.cell_identifier)

      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      cell_text = self.items[indexPath.row()]
      cell.textLabel().setText_(cell_text)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
      return 1

    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)
      item = self.items[indexPath.row()]

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
    self._table_extensions = table_extensions

  def nav_setup(self, this: UIViewController):
    # todo: navigation 系を外出し
    navigationController = this.navigationController()
    navigationBar = navigationController.navigationBar()
    navigationItem = this.navigationItem()
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

    #navigationBar.prefersLargeTitles = True
    #navigationController.setHidesBarsOnSwipe_(True)

    _done_btn = UIBarButtonItem.alloc()
    done_btn = _done_btn.initWithBarButtonSystemItem_target_action_(
      0, this, sel('doneButtonTapped:'))

    self.searchController.initWithSearchResultsController_(None)
    #self.searchController.setSearchResultsUpdater_(this)
    self.searchController.setObscuresBackgroundDuringPresentation_(False)

    navigationItem.setTitle_('searchController Sample')
    navigationItem.rightBarButtonItem = done_btn
    navigationItem.setSearchController_(self.searchController)
    navigationItem.setHidesSearchBarWhenScrolling_(True)

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    _cls._init()
    return _cls._this


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
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

