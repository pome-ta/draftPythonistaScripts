from objc_util import ObjCClass

import pdbg

UIApplication = ObjCClass('UIApplication')
app = UIApplication.sharedApplication()
keyWindow = app.keyWindow()
#windows = app.windows()
rootViewController = keyWindow.rootViewController()
pdbg.state(rootViewController)
