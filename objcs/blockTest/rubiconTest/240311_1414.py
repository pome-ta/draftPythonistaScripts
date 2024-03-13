#import inspect
from objc import ObjCClass, ObjCProtocol
from objc.runtime import objc_property_t

from objc_util import ObjCInstance
import pdbr

UINavigationController = ObjCClass('UINavigationController')
#pdbg.all(UINavigationController)
#print(UINavigationController)

#print(inspect.getmembers(UINavigationController, inspect.ismethod))

#print(UINavigationController.partial_methods)

app = ObjCClass('UIApplication').sharedApplication
window = app.keyWindow
#pdbg.state(app)
#print(objc_property_t(app.ptr))
#print(app)
pdbr.state(window)

