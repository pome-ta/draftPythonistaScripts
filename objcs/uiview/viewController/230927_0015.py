from objc_util import ObjCClass, on_main_thread
import ui

import pdbg


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self.bg_color = 'maroon'
    self.bg_color = 'red'

  def will_close(self):
    print('close')

  def layout(self):
    pass


@on_main_thread
def present_objc():
  # xxx: 全体的に改善
  app = ObjCClass('UIApplication').sharedApplication()
  if app.keyWindow():
    #print('t')
    window = app.keyWindow()
  else:
    print('f')
    window = app.windows().firstObject()

  root_vc = window.rootViewController()
  pdbg.state(root_vc.view().subviews())
  #pdbg.all(root_vc.view())

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()


if __name__ == '__main__':
  view = View()

  present_objc()

  view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])

