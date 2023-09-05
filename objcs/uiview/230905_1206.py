from objc_util import ObjCClass, create_objc_class
import ui

import pdbg

UIView = ObjCClass('UIView')
UISearchBar = ObjCClass('UISearchBar')
UIColor = ObjCClass('UIColor')

# xxx: 検索時のcell 選択も視野に`delegate` を作っていく
# xxx: まずは、通常の入力検知


class SearchTableViewController(object):

  def __init__(self):
    self._searchBar_delegate: 'UISearchBarDelegate'
    self.searchBar()

  @property
  def searchBar_delegate(self):
    return self._searchBar_delegate

  def searchBar(self):
    # --- `UISearchBarDelegate` Methods
    '''
    def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText) -> None:
      print(f'01 : searchBar_textDidChange_')
      pass

    def searchBar_shouldChangeTextInRange_replacementText_(
        _self, _cmd, _searchBar, _range, _text) -> bool:
      print(f'02 : searchBar_shouldChangeTextInRange_replacementText_')
      return True

    def searchBarShouldBeginEditing_(_self, _cmd, _searchBar) -> bool:
      print(f'03 : searchBarShouldBeginEditing_')
      return True

    def searchBarTextDidBeginEditing_(_self, _cmd, _searchBar) -> None:
      print(f'04 : searchBarTextDidBeginEditing_')
      pass

    def searchBarShouldEndEditing_(_self, _cmd, _searchBar) -> bool:
      print(f'05 : searchBarShouldEndEditing_')
      return True

    def searchBarTextDidEndEditing_(_self, _cmd, _searchBar) -> None:
      print(f'06 : searchBarTextDidEndEditing_')
      pass
    '''

    def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText):
      print('h')
      pass
    
    
    def searchBar_shouldChangeTextInRange_replacementText_(_self, _cmd, _searchBar,
                                                           _range, _text):
      print('h')
      return 1
    
    
    def searchBarShouldBeginEditing_(_self, _cmd, _searchBar):
      print('h')
      return 1
    
    
    def searchBarTextDidBeginEditing_(_self, _cmd, _searchBar):
      print('h')
      pass
    
    
    def searchBarShouldEndEditing_(_self, _cmd, _searchBar):
      print('h')
      return 1
    
    
    def searchBarTextDidEndEditing_(_self, _cmd, _searchBar):
      pass
    
    
    _methods = [
      searchBar_textDidChange_,
      searchBar_shouldChangeTextInRange_replacementText_,
      searchBarShouldBeginEditing_,
      searchBarTextDidBeginEditing_,
      searchBarShouldEndEditing_,
      searchBarTextDidEndEditing_,
    ]
    _protocols = ['UISearchBarDelegate']

    SearchBarDelegate = create_objc_class(name='SearchBarDelegate',
                                          methods=_methods,
                                          protocols=_protocols)
    self._searchBar_delegate = SearchBarDelegate.new()


class ObjcUI(object):

  def __init__(self):
    self.view = UIView.new()
    self.controllers = SearchTableViewController()
    self.viewDidLoad()
    #self.view.addSubview_(self.view_w)
    self.view.addSubview_(self.sb)

  def viewDidLoad(self):
    frame = ((0.0, 0.0), (100.0, 100.0))
    self.view.setFrame_(frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self.sb = UISearchBar.new()
    self.sb.setFrame_(frame)
    self.sb.backgroundColor = UIColor.cyanColor()
    # [UISearchBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbarstyle?language=objc)
    '''
    0 : UISearchBarStyleDefault
    1 : UISearchBarStyleProminent
    2 : UISearchBarStyleMinimal
    '''
    # xxx: `UISearchBarStyleMinimal` 以外落ちる
    self.sb.searchBarStyle = 2
    self.sb.placeholder = 'ほげ☺️'
    self.sb.size = (100.0, 56.0)

    self.sb.setAutoresizingMask_(1 << 1)
    self.sb.delegate = self.controllers.searchBar_delegate

    #self.sb_SearchTableViewController()

    self.sb.autorelease()
    #pdbg.state(self.sb)

    self.view_w = UIView.new()
    self.view_w.setFrame_(frame)
    self.view_w.setAutoresizingMask_(1 << 1)
    self.view_w.backgroundColor = UIColor.cyanColor()
    self.view_w.autorelease()

  def layout(self):
    pass


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.objc_view = ObjcUI()
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

