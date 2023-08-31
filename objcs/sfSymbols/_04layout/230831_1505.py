from objc_util import ObjCClass
import ui

import pdbg

UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')


uiview = UIView.new().initWithFrame_(((0.0, 0.0), (200.0, 120.0))).autorelease()
uiview.setAutoresizingMask_((1 << 1) | (1 << 4))
#pdbg.state(uiview)


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.objc_instance.addSubview_(uiview)


if __name__ == '__main__':
  py_view = PyView()
  py_view.present(style='fullscreen', orientations=['portrait'])
  pdbg.state(uiview)

