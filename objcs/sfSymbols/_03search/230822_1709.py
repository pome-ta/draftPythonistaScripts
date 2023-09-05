from objc_util import ObjCClass, create_objc_class
import ui

import pdbg

#text_field = ui.TextField()

UISearchBar = ObjCClass('UISearchBar')
#pdbg.state(UISearchBar.new())


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
search_bar_delegate = create_objc_class(name='search_bar_delegate',
                                        methods=_methods,
                                        protocols=_protocols)

delegate = search_bar_delegate.alloc().init()


#pdbg.state(delegate)
class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.update()

  #@ui.in_background
  def update(self):
    _frame = ((0.0, 0.0), (320.0, 128.0))
    #self.sb = UISearchBar.alloc().initWithFrame_(_frame).autorelease()
    self.sb = UISearchBar.new()  #.autorelease()
    frame = ((0.0, 0.0), (100.0, 100.0))
    self.sb.setFrame_(frame)
    self.sb.searchBarStyle = 2
    self.sb.placeholder = 'ほげ☺️'
    self.sb.size = (100.0, 56.0)

    self.sb.setAutoresizingMask_(1 << 1)
    #self.sb.setFrame_(_frame)#.autorelease()

    self.sb.setDelegate_(delegate)
    #pdbg.state(self.sb)
    #self.sb.initWithFrame_(_frame).autorelease()
    #pdbg.state(self.sb)

    self.objc_instance.addSubview_(self.sb)
    #pdbg.state(self.objc_instance)
    #self.present(style='fullscreen', orientations=['portrait'])


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])

