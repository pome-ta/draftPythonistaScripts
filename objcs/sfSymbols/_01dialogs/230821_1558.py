from pathlib import Path
import plistlib

from objc_util import ObjCClass, uiimage_to_png
import dialogs
import ui

UIImage = ObjCClass('UIImage')
UIColor = ObjCClass('UIColor')
UIImageSymbolConfiguration = ObjCClass('UIImageSymbolConfiguration')


def __configuration_by_applying_configuration(
    applys: list) -> UIImageSymbolConfiguration:
  _conf = UIImageSymbolConfiguration.defaultConfiguration()
  for apply in applys:
    _conf = _conf.configurationByApplyingConfiguration_(apply)
  return _conf


def get_symbo_icon(symbol_name: str, point_size: float = 64.0) -> ui.Image:
  '''
  size = UIImageSymbolConfiguration.configurationWithPointSize_(point_size)
  color = UIImageSymbolConfiguration.configurationPreferringMonochrome()

  conf = __configuration_by_applying_configuration([size, color])
  '''

  # `scene.Texture` で着色するため白色を指定
  #tint_color = UIColor.whiteColor()
  tint_color = UIColor.redColor()
  '''
  case automatic = 0
  case alwaysOriginal = 1
  case alwaysTemplate = 2
  '''

  ui_image = UIImage.systemImageNamed_(symbol_name)
  '''
  ui_image = UIImage.systemImageNamed_withConfiguration_(
    symbol_name, conf).imageWithTintColor_renderingMode_(tint_color, 1)
  '''
  png_bytes = uiimage_to_png(ui_image)
  png_img = ui.Image.from_data(png_bytes, 2)
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

dialogs.list_dialog(title=f'{len(dialog_items)}', items=dialog_items)

