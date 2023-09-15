from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

UITabBar = ObjCClass('UITabBar')


class ObjcControl(object):

  def __init__(self):
    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self.view = UIView.new()


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

  def layout(self):
    pass


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()

