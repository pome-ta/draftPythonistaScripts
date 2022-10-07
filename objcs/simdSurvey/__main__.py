from pathlib import Path
import webbrowser

from objc_util import ObjCClass

NSBundle = ObjCClass("NSBundle")

p = 'Frameworks'

obj_lib = NSBundle.bundleWithPath_(f'/System/Library/{p}').bundlePath()
root_dir = Path.expanduser(Path(str(obj_lib)))

f = 'Accelerate'
root_list = sorted(list(root_dir.iterdir()))
for i in root_list:
  if f in f'{i.name}':
    print(i)

