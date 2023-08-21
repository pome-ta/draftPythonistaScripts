from pathlib import Path
import plistlib

symbol_order_path = '/System/Library/CoreServices/CoreGlyphs.bundle/symbol_order.plist'
symbol_order_bundle = Path(symbol_order_path)

order_list = plistlib.loads(symbol_order_bundle.read_bytes())

