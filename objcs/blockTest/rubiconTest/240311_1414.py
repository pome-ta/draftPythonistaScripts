from objc import ObjCClass
from objc_util import on_main_thread

import pdbr

UIViewController = ObjCClass('UIViewController')


@on_main_thread
def main():
  app = ObjCClass('UIApplication').sharedApplication
  window = app.keyWindow if app.keyWindow else app.windows[0]
  root_vc = window.rootViewController

  while root_vc.presentedViewController:
    root_vc = root_vc.presentedViewController

  vc = UIViewController.new()
  vc.setModalPresentationStyle_(1)
  root_vc.presentViewController_animated_completion_(vc, True, None)


main()

