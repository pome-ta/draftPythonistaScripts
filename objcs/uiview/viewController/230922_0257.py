# coding: utf-8
from objc_util import *
import ui


def get_view_controller(uiview):
  if isinstance(uiview, ui.View):
    viewobj = ObjCInstance(uiview)
  elif isa(uiview, 'ObjCInstance') and uiview.isKindOfClass_(
      ObjCClass('UIView')):
    viewobj = uiview
  viewResponder = viewobj.nextResponder()
  try:
    while not viewResponder.isKindOfClass_(ObjCClass('UIViewController')):
      viewResponder = viewResponder.nextResponder()
  except AttributeError:
    return None  #if view is not being presented for example
  return viewResponder


root_view = ui.View()
a = get_view_controller(root_view)
