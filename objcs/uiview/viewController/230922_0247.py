from objc_util import ObjCClass
import ui


def get_view_controller(view):
  if isinstance(view, ui.View):
    view_obj = ObjCInstance(uiview)

