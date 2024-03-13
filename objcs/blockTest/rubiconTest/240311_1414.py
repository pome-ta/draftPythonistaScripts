import inspect
from objc import ObjCClass
import pdbg

UINavigationController = ObjCClass('UINavigationController')
#pdbg.all(UINavigationController)
#print(UINavigationController)

#print(inspect.getmembers(UINavigationController, inspect.ismethod))

#print(UINavigationController.partial_methods)

app = ObjCClass('UIApplication')
pdbg.state(app)
