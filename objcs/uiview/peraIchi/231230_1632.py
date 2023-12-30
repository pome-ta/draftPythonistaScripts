from objc_util import ObjCClass, nsurl
import ui

from pathlib import Path

import pdbg
#/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/emj/Airplane.png
def create_icons():
  Catalog = ObjCClass('CUICatalog').alloc()
  NSBundle = ObjCClass('NSBundle')
  path = nsurl(str(NSBundle.mainBundle().bundlePath()) + '/Assets.car')
  assets = Catalog.initWithURL_error_(path, None)
  print(assets)
  pdbg.state(assets.appearanceNames())
  all_names = assets.allImageNames()
  #print(all_names)
  named = ui.Image.named
  return [named(str(i)) for i in all_names]

#icons = create_icons()

dummy_pngimg_path = '/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/emj/Airplane.png'

dummy = Path(dummy_pngimg_path)
print(dummy.exists())
