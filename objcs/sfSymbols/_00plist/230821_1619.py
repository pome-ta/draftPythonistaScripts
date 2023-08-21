from pathlib import Path
import plistlib

#from objc_util import ObjCClass, uiimage_to_png

#UIImage = ObjCClass('UIImage')

CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

symbol_order_path = 'symbol_order.plist'
symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

order_list = plistlib.loads(symbol_order_bundle.read_bytes())

