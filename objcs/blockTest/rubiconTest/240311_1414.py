from objc import ObjCClass, ObjCProtocol

import pdbr

UINavigationController = ObjCClass('UINavigationController')

app = ObjCClass('UIApplication').sharedApplication
window = app.keyWindow if app.keyWindow else app.windows[0]
root_vc = window.rootViewController
#pdbg.state(app)
#print(objc_property_t(app.ptr))
#print(app)
#pdbr.state(app.windows[0])
pdbr.state(root_vc.presentedViewController)

