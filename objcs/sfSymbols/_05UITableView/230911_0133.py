from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

UIView = ObjCClass('UIView')
UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')
UIColor = ObjCClass('UIColor')

all_items = [
  'Swift',
  'Java',
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


class TableViewController(object):

  def __init__(self, items: list = []):
    self.items = items
    self._table_dataSource: 'UITableViewDataSource'
    self._table_delegate: 'UITableViewDelegate'

    self.init_table_dataSource()
    self.init_table_delegate()

  @property
  def table_dataSource(self):
    return self._table_dataSource

  @property
  def table_delegate(self):
    return self._table_delegate

  def init_table_dataSource(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      #tableView = ObjCInstance(_tableView)
      return 1

    #

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      #_cell = UITableViewCell.new()
      #cell = _cell.initWithStyle_reuseIdentifier_(0, 'cell')
      #cell.textLabel().text = 'hoge'
      cell = UITableViewCell.alloc().initWithStyle_reuseIdentifier_(0, 'cell')

      return cell

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      pass

    # --- `UITableViewDataSource` set up
    _methods = [
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
    ]
    _protocols = ['UITableViewDataSource', 'UITableViewController']

    table_dataSource = create_objc_class(name='table_dataSource',
                                         methods=_methods,
                                         protocols=_protocols)
    self._table_dataSource = table_dataSource.new()

  def init_table_delegate(self):
    # --- `UITableViewDelegate` Methods
    def tableView_willDisplayCell_forRowAtIndexPath_(_self, _cmd, _tableView,
                                                     _cell, _indexPath):
      pass

    def tableView_indentationLevelForRowAtIndexPath_(_self, _cmd, _tableView,
                                                     _indexPath):
      return 0

    def tableView_shouldSpringLoadRowAtIndexPath_withContext_(
        _self, _cmd, _tableView, _indexPath, _context):
      return False

    # --- `UITableViewDelegate` set up
    _methods = [
      tableView_willDisplayCell_forRowAtIndexPath_,
      tableView_indentationLevelForRowAtIndexPath_,
      tableView_shouldSpringLoadRowAtIndexPath_withContext_,
    ]
    _protocols = ['UITableViewDelegate']

    table_delegate = create_objc_class(name='table_delegate',
                                       methods=_methods,
                                       protocols=_protocols)
    self._table_delegate = table_delegate.new()


class ObjcControlView(object):

  def __init__(self):
    self.view = UIView.new()

    self.table_view: 'UITableView'
    self.controllers = TableViewController(all_items)

    self.viewDidLoad()
    self.view.addSubview_(self.table_view)

  def init_UITableView(self):
    frame = ((0.0, 0.0), (100.0, 100.0))
    #self.table_view = UITableView.new()

    # [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
    '''
    0 : UITableViewStylePlain
    1 : UITableViewStyleGrouped
    2 : UITableViewStyleInsetGrouped
    '''
    #self.table_view.initWithFrame_style_(frame, 0)
    self.table_view = UITableView.alloc().initWithFrame_style_(frame, 0)

    # xxx: 2度`frame` 指定している。`init` からは`frame` が反映されないため
    self.table_view.setFrame_(frame)
    #self.table_view.dataSource = self.controllers.tableData_source
    #pdbg.state(self.table_view)
    self.table_view.registerClass_forCellReuseIdentifier_(
      UITableViewCell, 'cell')

    #on_main_thread(self.table_view.registerClass_forCellReuseIdentifier_)(UITableViewCell, 'cell')
    self.table_view.setDataSource_(self.controllers.table_dataSource)
    self.table_view.setDelegate_(self.controllers.table_delegate)

    self.table_view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.table_view.autorelease()

  def viewDidLoad(self):
    frame = ((0.0, 0.0), (100.0, 100.0))
    self.view.setFrame_(frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self.init_UITableView()

  def layout(self):
    pass


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.objc_view = ObjcControlView()
    self.objc_instance.addSubview_(self.objc_view.view)

  def layout(self):
    #size = self.objc_view.view.frame().size
    size = self.objc_view.table_view.frame().size

    width = size.width
    height = size.height
    #pdbg.state(size)
    #print(width, height)


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()

