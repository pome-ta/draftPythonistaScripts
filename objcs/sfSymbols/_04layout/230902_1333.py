from objc_util import ObjCClass
import ui

import pdbg

UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')


class ObjcView(object):

  def __init__(self, parent_frame: tuple[float, float, float, float]):
    _, _, w, h = parent_frame
    _frame = ((0.0, 0.0), (w, h))

    self.view = UIView.alloc()
    self.view.initWithFrame_(_frame)
    self.view.backgroundColor = UIColor.redColor()
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.autorelease()





class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'cyan'
    self.present(style='fullscreen', orientations=['portrait'])

    self.objc_view = ObjcView(self.frame)
    self.objc_instance.addSubview_(self.objc_view.view)
    #self.present(style='fullscreen', orientations=['portrait'])


  def layout(self):
    _, _, w, h = self.frame

    #self.objc_view.width = w
    #self.objc_view.height = h


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  #view.present()

