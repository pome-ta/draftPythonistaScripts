from objc_util import ObjCClass
import ui

import pdbg

UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')

uiview = UIView.new()
pdbg.state(uiview)

class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    


if __name__ == '__main__':
  py_view = PyView()
  #py_view.present(style='fullscreen', orientations=['portrait'])

