from pyrubicon.objc.api import ObjCClass
from rbedge.functions import NSStringFromClass

UIViewController = ObjCClass('UIViewController')

if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = UIViewController.new()
  _title = NSStringFromClass(UIViewController)
  main_vc.navigationItem.title = _title

  presentation_style = UIModalPresentationStyle.fullScreen

  app = App(main_vc, presentation_style)
  app.present()
