from objc_util import ObjCClass
import ui

import pdbg

#text_field = ui.TextField()

UISearchBar = ObjCClass('UISearchBar')
#pdbg.state(UISearchBar)


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    _frame = ((0.0, 0.0), (320.0, 64.0))
    self.sb = UISearchBar.alloc().initWithFrame_(_frame).autorelease()
    #self.sb.initWithFrame_(_frame).autorelease()
    #pdbg.state(self.sb)

    self.objc_instance.addSubview_(self.sb)
    #pdbg.state(self.objc_instance)
    #self.present(style='fullscreen', orientations=['portrait'])


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])

