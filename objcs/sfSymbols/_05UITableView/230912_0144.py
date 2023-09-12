import ctypes

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


class TableViewController(object):

  def __init__(self, items: list = [], cell_identifier: str = 'cell'):
    self.items = items
    self.cell_identifier = cell_identifier
    self._table_dataSource: 'UITableViewDataSource'

    self.init_table_dataSource()

  @property
  def table_dataSource(self):
    return self._table_dataSource

  def init_table_dataSource(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return len(self.items)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      # xxx: `dequeueReusableCellWithIdentifier_forIndexPath_` は、落ちる？
      #cell = tableView.dequeueReusableCellWithIdentifier_(self.cell_identifier)

      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      cell_text = self.items[indexPath.row()]
      cell.textLabel().setText_(cell_text)
      #pdbg.state(cell)
      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return 1

    # --- `UITableViewDataSource` set up
    _methods = [
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
      numberOfSectionsInTableView_,
    ]
    _protocols = [
      'UITableViewDataSource',
    ]

    create_kwargs = {
      'name': 'table_dataSource',
      'methods': _methods,
      'protocols': _protocols,
    }

    table_dataSource = create_objc_class(**create_kwargs)
    self._table_dataSource = table_dataSource.new()


class ObjcControlView(object):

  def __init__(self):
    self.view = UIView.new()
    self.table_view = UITableView.new()

    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self.cell_identifier = 'cell'

    self.controllers = TableViewController(all_items, self.cell_identifier)

    self.viewDidLoad()
    self.view.addSubview_(self.table_view)

  def init_UITableView(self):
    # [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
    '''
    0 : UITableViewStylePlain
    1 : UITableViewStyleGrouped
    2 : UITableViewStyleInsetGrouped
    '''
    self.table_view.initWithFrame_style_(self.tmp_frame, 0)

    # xxx: 2度`frame` 指定している。`init` からは`frame` が反映されないため
    self.table_view.setFrame_(self.tmp_frame)
    self.table_view.registerClass_forCellReuseIdentifier_(
      UITableViewCell, self.cell_identifier)

    self.table_view.setDataSource_(self.controllers.table_dataSource)

    self.table_view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.table_view.autorelease()

  def viewDidLoad(self):
    self.view.setFrame_(self.tmp_frame)
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

