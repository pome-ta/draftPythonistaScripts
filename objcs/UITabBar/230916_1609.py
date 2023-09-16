from objc_util import ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

UIView = ObjCClass('UIView')
UITabBar = ObjCClass('UITabBar')

UIColor = ObjCClass('UIColor')


class ObjcController(object):

  def __init__(self):
    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self.view = UIView.new().autorelease()
    self.tab_bar = UITabBar.new().autorelease()

    self._init_UITabBar()

    self.viewDidLoad()

  def viewDidLoad(self):
    self.view.setFrame_(self.tmp_frame)
    self.view.setAutoresizingMask_((1 << 1) | (1 << 4))
    self.view.backgroundColor = UIColor.redColor()

    self.view.addSubview_(self.tab_bar)
    #pdbg.state(self.view.window())

  def _init_UITabBar(self):
    #pdbg.state(self.tab_bar.standardAppearance())
    #pdbg.state(self.tab_bar)
    appearance = self.tab_bar.standardAppearance()
    #self.tab_bar.setFrame_(self.tmp_frame)
    #self.tab_bar.size = (100.0, 89.0)
    #self.tab_bar.setTranslatesAutoresizingMaskIntoConstraints_(False)
    #self.tab_bar.setAutoresizingMask_((1 << 5)|(1 << 5))
    #self.tab_bar.setContentMode_(6)
    #pdbg.state(self.tab_bar.translatesAutoresizingMaskIntoConstraints())
    #pdbg.state(self.tab_bar)
    #pdbg.state(self.view.autoresizesSubviews())


class PyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.objc_controller = ObjcController()
    self.objc_instance.addSubview_(self.objc_controller.view)
    pdbg.state(self.objc_instance.window())

  def layout(self):
    pass


if __name__ == '__main__':
  view = PyView()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')
  #view.present()

