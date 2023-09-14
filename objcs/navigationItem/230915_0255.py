from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    #self.nv = ui.NavigationView()
    #pdbg.state(self.nv.objc_instance)    

  def layout(self):
    pass


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()
  

