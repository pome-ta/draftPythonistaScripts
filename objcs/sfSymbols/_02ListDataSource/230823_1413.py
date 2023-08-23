from pathlib import Path
import plistlib

from objc_util import ObjCClass, uiimage_to_png
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


def get_order_list():
  CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

  symbol_order_path = 'symbol_order.plist'
  symbol_order_bundle = Path(CoreGlyphs_path, symbol_order_path)

  order_list = plistlib.loads(symbol_order_bundle.read_bytes())
  return order_list


class SearchField(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 1
    self.bar = ui.TextField()
    # xxx: 検索はまだ先
    #self.bar.delegate = SearchTextFieldDelegate()
    self.bar.clear_button_mode = 'always'
    self.bar.placeholder = 'search symbol name'
    self.add_subview(self.bar)

  def layout(self):
    _, _, w, h = self.frame
    self.bar.width = w * 0.88
    self.bar.height = h * 0.64
    self.bar.center = self.center


class MyTableViewDelegate(object):

  def tableview_did_select(self, tableview: ui.TableView, section: int,
                           row: int):
    print(dir(tableview))
    print(f'tableview:{tableview}\nsection:{section}\nrow:{row}')


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    self.search_field = SearchField()
    self.search_field.flex = 'W'
    self.add_subview(self.search_field)

    self.order_list = get_order_list()
    self.order_list.sort()
    self.source_items = [name2symbol(name) for name in self.order_list]
    #self.source_items = [name2symbol(name) for name in self.order_list[:64]]

    self.table_view = ui.TableView()
    self.table_view.delegate = MyTableViewDelegate()
    self.table_view.data_source = ui.ListDataSource(self.source_items)
    self.table_view.flex = 'W'

    self.add_subview(self.table_view)

  def layout(self):
    _, _, w, h = self.frame
    #self.search_field.width = w
    self.search_field.height = 48

    self.table_view.y = self.search_field.height
    self.table_view.height = h - self.search_field.height - 64  # xxx: tabView マージン


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])

