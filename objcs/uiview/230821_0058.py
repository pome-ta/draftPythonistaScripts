# tab ? のやつ出す


from objc_util import ObjCClass

import ui


UITabBar = ObjCClass('UITabBar')

class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)

