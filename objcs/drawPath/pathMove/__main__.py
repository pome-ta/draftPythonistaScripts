from pathlib import Path

from objc_util import ObjCClass, nsurl, NSData, CGRect, CGPoint, CGSize
import ui

import pdbg


class ViewController:
  def __init__(self):
    pass


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'

    #self.view_controller = ViewController(self.objc_instance)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

