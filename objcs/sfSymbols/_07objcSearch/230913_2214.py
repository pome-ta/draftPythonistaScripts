from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

UIView = ObjCClass('UIView')
UISearchBar = ObjCClass('UISearchBar')
UITableView = ObjCClass('UITableView')
UIColor = ObjCClass('UIColor')

# xxx: 検索時のcell 選択も視野に`delegate` を作っていく
# xxx: まずは、通常の入力検知


class ObjcControllers(object):

  def __init__(self):
    self._searchBar_delegate: 'UISearchBarDelegate'
    self._init_searchBar()

  @property
  def searchBar_delegate(self):
    return self._searchBar_delegate

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
    self.view = UIView.new()
    self.search_bar = UISearchBar.new()

    self.table_view: 'UITableView'
    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))

    self.controllers = ObjcControllers()
    self.viewDidLoad()

    self.view.addSubview_(self.search_bar)

  def _init_UISearchBar(self):
    self.search_bar.setFrame_(self.tmp_frame)
    self.search_bar.backgroundColor = UIColor.cyanColor()
    # [UISearchBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbarstyle?language=objc)
    '''
    0 : UISearchBarStyleDefault
    1 : UISearchBarStyleProminent
    2 : UISearchBarStyleMinimal
    '''
    # xxx: `UISearchBarStyleMinimal=2` 以外落ちる
    self.search_bar.searchBarStyle = 2
    self.search_bar.placeholder = 'ほげ☺️'
    self.search_bar.size = (100.0, 56.0)

    self.search_bar.setAutoresizingMask_(1 << 1)
    self.search_bar.delegate = self.controllers.searchBar_delegate
    self.search_bar.autorelease()

  def init_UITableView(self):
    self.table_view = UITableView.new()

  def viewDidLoad(self):
    self.view.setFrame_(self.tmp_frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self._init_UISearchBar()
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
    size = self.objc_view.view.frame().size

    width = size.width
    height = size.height
    #pdbg.state(size)
    #print(width, height)


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()

