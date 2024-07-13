from pathlib import Path

from objc_util import ObjCClass

import pdbg


NSFileManager = ObjCClass('NSFileManager')

pdbg.state(NSFileManager.new())
