from objc import ObjCClass

import pdbr

app = ObjCClass('UIApplication').sharedApplication
window = app.keyWindow if app.keyWindow else app.windows[0]
root_vc = window.rootViewController

while root_vc.presentedViewController:
  root_vc = root_vc.presentedViewController
pdbr.state(root_vc)

