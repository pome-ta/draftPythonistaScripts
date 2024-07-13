from pathlib import Path

from objc_util import ObjCClass

import pdbg


NSFileManager = ObjCClass('NSFileManager')

pdbg.state(NSFileManager.defaultManager())
#print(NSFileManager.defaultManager().temporaryDirectory().uri())
#print(NSFileManager.new().temporaryDirectory().uri())
