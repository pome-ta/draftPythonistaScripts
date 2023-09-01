from objc_util import ObjCClass
import ui

import pdbg

UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')


class ObjcView(ui.View):

  def __init__(self, parent_frame: tuple[float, float, float, float], *args,
               **kwargs):
    super().__init__(self, *args, **kwargs)
    self.flex = 'WH'
    _, _, w, h = parent_frame
    print(w)
    _frame = ((0.0, 0.0), (w, h))

    self.ground_view = UIView.new()
    self.ground_view.initWithFrame_(_frame).autorelease()

    #self.ground_view = UIView.new().initWithFrame_(_gf).autorelease()
    self.ground_view.backgroundColor = UIColor.redColor()
    #self.ground_view.setAutoresizingMask_((1 << 1) | (1 << 4))
    #pdbg.state(self.ground_view)

    self.objc_instance.addSubview_(self.ground_view)


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self.present(style='fullscreen', orientations=['portrait'])

    self.objc_view: ui.View = ObjcView(self.frame)
    #self.objc_view.flex = 'WH'

    self.add_subview(self.objc_view)
    #self.present()

  def layout(self):
    #pdbg.state(self.objc_view.ground_view)
    _, _, w, h = self.frame

    #self.objc_view.width = w
    #self.objc_view.height = h


if __name__ == '__main__':
  view = PyView()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present()

