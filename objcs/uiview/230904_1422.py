from objc_util import ObjCClass, ObjCInstance, on_main_thread
import ui

import pdbg

UIView = ObjCClass('UIView')
UISearchBar = ObjCClass('UISearchBar')
UIColor = ObjCClass('UIColor')


class ObjcUI(object):

  def __init__(self):
    self.view = UIView.new()
    self.viewDidLoad()

  def viewDidLoad(self):
    frame = ((0.0, 0.0), (100.0, 100.0))
    self.view.setFrame_(frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    #self.view.setAutoresizingMask_(1 << 1)
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()

    self.sb = UISearchBar.new()
    self.sb.setFrame_(frame)
    # [UISearchBarStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uisearchbarstyle?language=objc)
    '''
    0 : UISearchBarStyleDefault
    1 : UISearchBarStyleProminent
    2 : UISearchBarStyleMinimal
    '''
    # xxx: `UISearchBarStyleMinimal` 以外落ちる
    self.sb.searchBarStyle = 2
    self.sb.placeholder = 'ほげ☺️'
    self.sb.size = (100.0, 48.0)
    self.sb.backgroundColor = UIColor.cyanColor()
    self.sb.setAutoresizingMask_(1 << 1)
    self.sb.autorelease()

    pdbg.state(self.sb)

    self.view_w = UIView.new()
    self.view_w.setFrame_(frame)

    self.view_w.setAutoresizingMask_(1 << 1)
    self.view_w.backgroundColor = UIColor.cyanColor()
    self.view_w.autorelease()

    #self.view.addSubview_(self.view_w)
    self.view.addSubview_(self.sb)


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
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present()

