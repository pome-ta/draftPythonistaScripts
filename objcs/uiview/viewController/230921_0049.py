from objc_util import ObjCClass

import pdbg

import ui


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
  view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])

  UIApplication = ObjCClass('UIApplication')
  app = UIApplication.sharedApplication()

  windows = app.windows()

  #pdbg.state(windows)
  print(windows)

