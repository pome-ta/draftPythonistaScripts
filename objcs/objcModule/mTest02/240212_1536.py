from pathlib import Path
from objc_util import ObjCClass, nsurl
import pdbg

NSBundle = ObjCClass('NSBundle')
mainBundle = NSBundle.mainBundle()
root_path = Path('./')
nsurl_root = nsurl(str(root_path.resolve()))
root_bundle = NSBundle.alloc().initWithURL_(nsurl_root)
root_bundle.load()


#pdbg.state(root_bundle)
#print(nsurl(str(root_path.resolve())))
