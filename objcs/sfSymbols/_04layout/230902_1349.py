from objc_util import ObjCClass,ObjCInstance
import ui

import pdbg

UIColor = ObjCClass('UIColor')
UIView = ObjCClass('UIView')
UIViewController = ObjCClass('UIViewController')


#pdbg.state(UIViewController.new())
view = ui.View()
#pdbg.state(ObjCInstance(view))
pdbg.state(UIView.new())
