from objc_util import ObjCClass
import ui

import pdbg

UIView = ObjCClass('UIView')
UISearchBar = ObjCClass('UISearchBar')
UIColor = ObjCClass('UIColor')


class ObjcUI(object):

  def __init__(self):
    self.view = UIView.new()
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
    self.sb.autorelease()

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

