from objc_util import ObjCClass
import pdbg

app = ObjCClass('UIApplication').sharedApplication()
window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

root_vc = window.rootViewController()
while root_vc.presentedViewController():
  root_vc = root_vc.presentedViewController()

pdbg.state(root_vc)

