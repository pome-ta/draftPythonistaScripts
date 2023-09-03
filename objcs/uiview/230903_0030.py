from objc_util import ObjCClass, ObjCInstance
import ui

import pdbg

UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')

#pdbg.state(UIView.new())


class ObjcUI(object):

  def __init__(self):
    self.view = UIView.new()

  def viewDidLoad(self):
    pass


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'cyan'
    self.ground = ui.View()
    self.ground.bg_color = 'yellow'
    self.ground.flex = 'WH'
    #self.add_subview(self.ground)
    #pdbg.state(self.ground.objc_instance)

    print(self.ground.objc_instance.autoresizingMask())
    print(self.ground.objc_instance.autoresizesSubviews())
    self.objc_instance.addSubview_(self.ground.objc_instance)
    self.objc_view = ObjcUI()
    #pdbg.state(ObjCInstance(self.objc_view))


if __name__ == '__main__':
  view = PyView()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present()

