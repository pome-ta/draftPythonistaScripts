from objc_util import ObjCClass, ObjCInstance,on_main_thread
import ui

import pdbg

UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')

#@on_main_thread
class ObjcUI(object):

  def __init__(self):
    self.view = UIView.new()
    self.viewDidLoad()

  def viewDidLoad(self):
    frame = ((0.0, 0.0), (256.0, 256.0))
    self.view.initWithFrame_(frame)
    self.view.backgroundColor = UIColor.redColor()
    self.view.autorelease()
    self.layout()

  def layout(self):
    #self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.setAutoresizingMask_(18)




class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'cyan'
    self.ground = ui.View()
    self.ground.bg_color = 'yellow'
    self.ground.flex = 'WH'
    #self.add_subview(self.ground)
    #pdbg.state(self.ground.objc_instance)

    #print(self.ground.objc_instance.autoresizingMask())
    #print(self.ground.objc_instance.autoresizesSubviews())
    #self.objc_instance.addSubview_(self.ground.objc_instance)
    self.objc_view = ObjcUI()
    #pdbg.state(ObjCInstance(self.objc_view))
    self.objc_instance.addSubview_(self.objc_view.view)
    pdbg.state(self.objc_view.view)

  def layout(self):
    self.objc_view.layout()
    #pdbg.state(self.objc_view.view)


if __name__ == '__main__':
  view = PyView()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present()

