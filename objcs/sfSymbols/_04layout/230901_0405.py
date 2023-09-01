from objc_util import ObjCClass
import ui

import pdbg

UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')

uiview = UIView.new().initWithFrame_(
  ((0.0, 0.0), (200.0, 120.0))).autorelease()
uiview.setAutoresizingMask_((1 << 1) | (1 << 4))
#pdbg.state(uiview)


class ObjcView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.flex = 'WH'
    self.objc_instance.addSubview_(uiview)


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.objc_view: ui.View = ObjcView()
    
    self.add_subview(self.objc_view)


if __name__ == '__main__':

  py_view = PyView()
  py_view.present(style='fullscreen', orientations=['portrait'])
  pdbg.state(uiview)

