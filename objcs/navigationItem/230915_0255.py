from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    self.name = 'ほげ☺️'
    self.b = ui.ButtonItem(image=ui.Image('iob:alert_24'))
    self.right_button_items = [self.b]
    
    #self.nv = ui.NavigationView()
    #pdbg.state(self.nv.objc_instance)

  def layout(self):
    pass


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()
  

