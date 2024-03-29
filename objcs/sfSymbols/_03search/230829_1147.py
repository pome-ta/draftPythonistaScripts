from pathlib import Path
import plistlib

from objc_util import ObjCClass, uiimage_to_png
import ui

all_items = [
  'Swift',
  'Java',
  'Ruby',
  'C++',
  'C',
  'C#',
  'Python',
  'Perl',
  'JavaScript',
  'PHP',
  'Scratch',
  'Scala',
  'COBOL',
  'Curl',
  'Dart',
  'HTML',
  'CSS',
  'Ruby on Rails',
  'TypeScript',
  'ECMAScript',
  'Jython',
  'CPython',
  'PyPy',
  'IronPython',
]

select_items = []

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


def get_order_list():
  CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

  symbol_order_path = 'symbol_order.plist'
  symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

  order_list = plistlib.loads(symbol_order_bundle.read_bytes())
  return order_list


class SearchTextFieldDelegate(object):

  def __init__(self):
    pass

  def textfield_should_begin_editing(self, textfield):
    print(f'1.should_begin:{textfield}\n')
    return True

  def textfield_did_begin_editing(self, textfield):
    print(f'2.did_begin:{textfield}\n')

  def textfield_did_end_editing(self, textfield):
    print(f'3.did_end:{textfield}\n')

  def textfield_should_return(self, textfield):
    textfield.end_editing()
    print(f'4.should_return:{textfield}\n')
    return True

  def textfield_should_change(self, textfield, range, replacement):
    print(
      f'5.should_change:{textfield}, range:{range}, replacement:{replacement}')
    print(f'text:{textfield.text}\n')
    return True

  def textfield_did_change(self, textfield):
    print(f'6.did_change:{textfield}')
    print(f'text:{textfield.text}\n')


class SearchField(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 1
    self.bar = ui.TextField()
    self.bar.delegate = SearchTextFieldDelegate()
    self.bar.clear_button_mode = 'always'
    self.bar.placeholder = 'search symbol name'
    self.add_subview(self.bar)

  def layout(self):
    _, _, w, h = self.frame
    # xxx: サイズ調整は仮
    self.bar.width = w * 0.88
    self.bar.height = h * 0.64
    self.bar.center = self.center


class IconTableView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.search_field: ui.TextField()
    self.symbol_table: ui.TableView()

    self.set_up()

  def set_up(self):
    self.bg_color = 'cyan'

    self.init_search_field()
    self.add_subview(self.search_field)

  def init_search_field(self):
    self.search_field = ui.TextField()
    self.search_field.flex = 'W'
    self.search_field.height = 48  # xxx: 仮決め打ち

    self.search_field.clear_button_mode = 'always'
    self.search_field.placeholder = 'search symbol name'

  def init_symbol_table(self):
    pass

  def layout(self):
    _, _, w, h = self.frame
    margin = h * 0.01
    self.search_field.y = margin


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'

    self.icon_table = IconTableView()
    self.icon_table.flex = 'W'
    self.add_subview(self.icon_table)

  def layout(self):
    _, _, w, h = self.frame

    self.icon_table.height = h - 48  # `TabView` margin


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])

