from objc_util import ObjCClass

import pdbg

import ui

UIApplication = ObjCClass('UIApplication')
class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

  def will_close(self):
    pass

  def layout(self):
    pass


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])
  #addChildViewController_
  #nextResponder = view.objc_instance.nextResponder()
  #pdbg.state(nextResponder)
  #pdbg.state(view.objc_instance)
  app = UIApplication.sharedApplication()
  keyWindow = app.keyWindow()
  #windows = app.windows()
  pdbg.state(keyWindow)
  #pdbg.state(windows)
  #rootViewController = keyWindow.rootViewController()
  #pdbg.state(rootViewController)

