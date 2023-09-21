from objc_util import ObjCClass, ObjCInstance
import ui

import pdbg


def get_view_controller(view):
  viewObj: ObjCInstance
  if isinstance(view, ui.View):
    viewObj = view.objc_instance
  elif isa(view, 'ObjCInstance') and view.isKindOfClass_(ObjCClass('UIView')):
    viewObj = view
  viewResponder = viewObj.nextResponder()


