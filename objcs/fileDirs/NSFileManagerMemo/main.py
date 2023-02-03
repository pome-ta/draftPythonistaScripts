from pathlib import Path
from objc_util import ObjCClass, ObjCInstance

import pdbg

NSFileManager = ObjCClass('NSFileManager')

fileManager = NSFileManager.defaultManager()

pdbg.state(fileManager.temporaryDirectory())
