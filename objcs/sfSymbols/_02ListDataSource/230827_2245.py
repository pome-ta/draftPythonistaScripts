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

  def tableview_did_select(self, tv: ui.TableView, section: int, row: int):
    #print(dir(tableview))
    #print(f'tableview:{tableview}\nsection:{section}\nrow:{row}')
    source = tv.data_source.items[row]
    title = source['title']
    print(title)


class SymbolListDataSourceList(list):

  def __init__(self, seq, datasource):
    list.__init__(self, seq)
    self.datasource: SymbolListDataSource = datasource

  def append(self, item):
    list.append(self, item)
    self.datasource.reload()

  def __setitem__(self, key, value):
    list.__setitem__(self, key, value)
    self.datasource.reload()

  def __delitem__(self, key):
    list.__delitem__(self, key)
    self.datasource.reload()

  def __setslice__(self, i, j, seq):
    list.__setslice__(self, i, j, seq)
    self.datasource.reload()

  def __delslice__(self, i, j):
    list.__delslice__(self, i, j)
    self.datasource.reload()


class SymbolListDataSource(object):

  def __init__(self, items=None):
    self.tableview: ui.TableView = None
    self.reload_disabled = False
    self.delete_enabled = True
    self.move_enabled = False

    self.action = None
    self.edit_action = None
    self.accessory_action = None

    self.tapped_accessory_row = -1
    self.selected_row = -1

    if items is not None:
      self.items = items
    else:
      self.items = SymbolListDataSourceList([])
    self.text_color = None
    self.highlight_color = None
    self.font = None
    self.number_of_lines = 1

  def reload(self):
    if self.tableview and not self.reload_disabled:
      self.tableview.reload()

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, value):
    self._items = SymbolListDataSourceList(value, self)
    self.reload()

  def tableview_number_of_sections(self, tv):
    self.tableview = tv
    return 1

  def tableview_number_of_rows(self, tv, section):
    return len(self.items)

  def tableview_accessory_button_tapped(self, tv, section, row):
    self.tapped_accessory_row = row
    if self.accessory_action:
      self.accessory_action(self)

  def tableview_did_select(self, tv, section, row):
    self.selected_row = row
    if self.action:
      self.action(self)

  def tableview_cell_for_row(self, tv, section, row):
    item = self.items[row]
    # xxx: `dict` type で決め打ち

    cell = ui.TableViewCell()
    x, y, w, h = cell.content_view.frame
    center_x, center_y = cell.content_view.center
    x_margin = h * 0.5
    y_margin = x_margin / 2

    icon_size = h - x_margin

    img_frame = (x_margin, y_margin, icon_size, icon_size)
    image_view = ui.ImageView(frame=img_frame)
    image_view.image = item.get('image', None)
    image_view.content_mode = 1
    #image_view.bg_color ='maroon'

    label_frame = (x_margin + h, y_margin, w, icon_size)

    label = ui.Label(frame=label_frame)
    label.text = item.get('title', '')
    #label.font = ('.SFUI-Regular', 14.0)  #xxx: from `ui.ListDataSource`

    label.bg_color = 'cyan'
    label.number_of_lines = self.number_of_lines

    cell.text_label.text = item.get('title', '')
    #cell.text_label.flex=''
    #cell.text_label.x = x_margin + h
    #print(cell.text_label.x)

    cell.content_view.add_subview(image_view)
    cell.content_view.add_subview(label)

    self.cell = cell

    return cell


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    self.search_field = SearchField()
    self.search_field.flex = 'W'
    self.add_subview(self.search_field)

    self.order_list = get_order_list()
    self.order_list.sort()

    #self.source_items = [name2symbol(name) for name in self.order_list]
    self.source_items = [name2symbol(name) for name in self.order_list[:52]]

    self.table_view = ui.TableView()
    self.table_view.delegate = MyTableViewDelegate()
    #self.table_view.data_source = ui.ListDataSource(self.source_items)
    #self.data_source = MyTableViewDataSource()
    self.symbol_data_source = SymbolListDataSource(self.source_items)
    self.table_view.data_source = self.symbol_data_source
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

