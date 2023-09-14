# xxx: 望ましくないlayout でやる

from pathlib import Path
import plistlib

from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

UIView = ObjCClass('UIView')
UITableView = ObjCClass('UITableView')
UITableViewCell = ObjCClass('UITableViewCell')
UIImage = ObjCClass('UIImage')
UISearchBar = ObjCClass('UISearchBar')
UIColor = ObjCClass('UIColor')


def get_order_list():
  CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

  symbol_order_path = 'symbol_order.plist'
  symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

  order_list = plistlib.loads(symbol_order_bundle.read_bytes())
  return order_list


all_items = get_order_list()
#all_items.sort()


class ObjcControllers(object):

  def __init__(self, items: list = [], cell_identifier: str = 'cell'):
    self.all_items = items
    self.grep_items = []
    self.cell_identifier = cell_identifier

    self._table_dataSource: 'UITableViewDataSource'
    self._table_delegate: 'UITableViewDelegate'
    self._searchBar_delegate: 'UISearchBarDelegate'

    self._init_table_dataSource()
    self._init_table_delegate()
    self._init_searchBar()

  @property
  def table_dataSource(self):
    return self._table_dataSource

  @property
  def table_delegate(self):
    return self._table_delegate

  @property
  def searchBar_delegate(self):
    return self._searchBar_delegate

  def _init_table_dataSource(self):
    # --- `UITableViewDataSource` Methods
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      items = self.grep_items if self.grep_items else self.all_items
      return len(items)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier_forIndexPath_(
        self.cell_identifier, indexPath)

      items = self.grep_items if self.grep_items else self.all_items
      
      cell_text = items[indexPath.row()]
      cell_image = UIImage.systemImageNamed_(cell_text)

      content = cell.defaultContentConfiguration()
      content.textProperties().setNumberOfLines_(1)
      content.setText_(cell_text)
      content.setImage_(cell_image)

      cell.setContentConfiguration_(content)

      return cell.ptr

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      # xxx: とりあえずの`1`
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

  def _init_table_delegate(self):
    # --- `UITableViewDelegate` Methods
    def tableView_didSelectRowAtIndexPath_(_self, _cmd, _tableView,
                                           _indexPath):
      indexPath = ObjCInstance(_indexPath)
      print(indexPath)
      item = self.items[indexPath.row()]
      print(item)

    # --- `UITableViewDelegate` set uo
    _methods = [
      tableView_didSelectRowAtIndexPath_,
    ]
    _protocols = [
      'UITableViewDelegate',
    ]

    create_kwargs = {
      'name': 'table_delegate',
      'methods': _methods,
      'protocols': _protocols,
    }

    table_delegate = create_objc_class(**create_kwargs)
    self._table_delegate = table_delegate.new()

  def _init_searchBar(self):
    # --- `UISearchBarDelegate` Methods
    def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText):
      #print(f'01 : searchBar_textDidChange_')
      # xxx: 変更通知は`1` か`2` といったところか？
      pass

    def searchBar_shouldChangeTextInRange_replacementText_(
        _self, _cmd, _searchBar, _range, _text):
      #print(f'02 : searchBar_shouldChangeTextInRange_replacementText_')
      searchBar = ObjCInstance(_searchBar)
      text = searchBar.text()
      print(f'02: {text}')
      return True

    def searchBarShouldBeginEditing_(_self, _cmd, _searchBar):
      #print(f'03 : searchBarShouldBeginEditing_')
      return True

    def searchBarTextDidBeginEditing_(_self, _cmd, _searchBar):
      #print(f'04 : searchBarTextDidBeginEditing_')
      pass

    def searchBarShouldEndEditing_(_self, _cmd, _searchBar):
      #print(f'05 : searchBarShouldEndEditing_')
      return True

    def searchBarTextDidEndEditing_(_self, _cmd, _searchBar):
      #print(f'06 : searchBarTextDidEndEditing_')
      pass

    def searchBarSearchButtonClicked_(_self, _cmd, _searchBar):
      #print(f'07 : searchBarSearchButtonClicked_')
      searchBar = ObjCInstance(_searchBar)
      text = searchBar.text()
      print(f'07: {text}')
      ObjCInstance(_searchBar).resignFirstResponder()

    # --- `UISearchBarDelegate` set up
    _methods = [
      searchBar_textDidChange_,
      searchBar_shouldChangeTextInRange_replacementText_,
      searchBarShouldBeginEditing_,
      searchBarTextDidBeginEditing_,
      searchBarShouldEndEditing_,
      searchBarTextDidEndEditing_,
      searchBarSearchButtonClicked_,
    ]
    _protocols = ['UISearchBarDelegate']

    create_kwargs = {
      'name': 'searchBar_delegate',
      'methods': _methods,
      'protocols': _protocols
    }

    searchBar_delegate = create_objc_class(**create_kwargs)

    self._searchBar_delegate = searchBar_delegate.new()


class ObjcControlView(object):

  def __init__(self):
    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self.view = UIView.new()
    self.search_bar = UISearchBar.new()
    self.table_view = UITableView.new()

    self.cell_identifier = 'cell'

    self.controllers = ObjcControllers(all_items, self.cell_identifier)
    self._init_UISearchBar()
    self._init_UITableView()

    #self.viewDidLoad()

  def _init_UISearchBar(self):
    height = 56.0
    self.search_bar.setFrame_(self.tmp_frame)

    #self.search_bar.backgroundColor = UIColor.cyanColor()

    self.search_bar.backgroundColor = UIColor.systemWhiteColor()
    #self.search_bar.backgroundColor = UIColor.systemDarkLightGrayColor()

    # [UISearchBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbarstyle?language=objc)
    '''
    0 : UISearchBarStyleDefault
    1 : UISearchBarStyleProminent
    2 : UISearchBarStyleMinimal
    '''
    # xxx: `UISearchBarStyleMinimal=2` 以外落ちる
    self.search_bar.searchBarStyle = 2
    self.search_bar.placeholder = 'ほげ☺️'
    self.search_bar.size = (100.0, height)

    self.search_bar.setAutoresizingMask_(1 << 1)
    self.search_bar.delegate = self.controllers.searchBar_delegate
    self.search_bar.autorelease()

    self.search = ui.View()
    self.search.flex = 'W'
    self.search.height = height
    self.search.objc_instance.addSubview_(self.search_bar)

  def _init_UITableView(self):
    # [UITableViewStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewstyle?language=objc)
    '''
    0 : UITableViewStylePlain
    1 : UITableViewStyleGrouped
    2 : UITableViewStyleInsetGrouped
    '''
    self.table_view.initWithFrame_style_(self.tmp_frame, 0)

    # xxx: 2度`frame` 指定している。`init` からは`frame` が反映されないため -> `setAutoresizingMask_` がいい感じにならない
    self.table_view.setFrame_(self.tmp_frame)
    self.table_view.registerClass_forCellReuseIdentifier_(
      UITableViewCell, self.cell_identifier)
    self.table_view.setDataSource_(self.controllers.table_dataSource)
    self.table_view.setDelegate_(self.controllers.table_delegate)

    self.table_view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.table_view.autorelease()

    self.table = ui.View()
    self.table.flex = 'W'
    self.table.objc_instance.addSubview_(self.table_view)

  def viewDidLoad(self):
    self.view.setFrame_(self.tmp_frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self.view.addSubview_(self.search_bar)

  def layout(self):
    pass


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.objc_view = ObjcControlView()
    #self.objc_instance.addSubview_(self.objc_view.view)
    self.add_subview(self.objc_view.search)
    self.add_subview(self.objc_view.table)

  def layout(self):
    '''
    size = self.objc_view.view.frame().size

    width = size.width
    height = size.height
    #pdbg.state(size)
    #print(width, height)
    '''
    _, _, w, h = self.frame
    buffer = 64
    s_height = self.objc_view.search.height
    t_height = h - s_height - buffer

    self.objc_view.table.height = t_height
    self.objc_view.table.y = s_height


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()

