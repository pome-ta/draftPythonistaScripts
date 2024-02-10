from objc_util import ObjCClass

import pdbg

UIStoryboard = ObjCClass('UIStoryboard')
NSBundle = ObjCClass('NSBundle')
pdbg.state(UIStoryboard.new())
#pdbg.state(NSBundle.mainBundle())
