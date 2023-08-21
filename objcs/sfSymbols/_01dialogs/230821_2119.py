from pathlib import Path
import plistlib

import clipboard
from objc_util import ObjCClass, uiimage_to_png
import dialogs
import ui

UIImage = ObjCClass('UIImage')


def get_symbo_icon(symbol_name: str) -> ui.Image:
  ui_image = UIImage.systemImageNamed_(symbol_name)
  png_bytes = uiimage_to_png(ui_image)
  png_img = ui.Image.from_data(png_bytes, 2)
  #png_img = ui.Image.from_data(png_bytes)
  return png_img


def name2symbol(symbol_name: str) -> dict[str, ui.Image]:
  _icon = get_symbo_icon(symbol_name)
  out_dict = {'title': symbol_name, 'image': _icon}
  return out_dict


CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

symbol_order_path = 'symbol_order.plist'
symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

order_list = plistlib.loads(symbol_order_bundle.read_bytes())

dialog_items = [name2symbol(name) for name in order_list]

dialogs_kwargs = {
  'title': f'{len(dialog_items)}',
  'items': dialog_items,
}

select_item = dialogs.list_dialog(**dialogs_kwargs)

if select_item:
  title_str = select_item['title']
  clipboard_result = f'UIImage.systemImageNamed_(\'{title_str}\')'
  clipboard.set(clipboard_result)
  print(clipboard_result)

