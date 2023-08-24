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
    #print(dir(tableview))
    #print(f'tableview:{tableview}\nsection:{section}\nrow:{row}')
    source = tableview.data_source.items[row]
    title = source['title']
    print(title)


class IconListDataSourceList(list):

  def __init__(self, seq, datasource):
    list.__init__(self, seq)
    self.datasource = datasource

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


class IconListDataSource(object):

  def __init__(self, items=None):
    self.tableview = None
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
      self.items = IconListDataSourceList([])
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
    self._items = IconListDataSourceList(value, self)
    self.reload()

  def tableview_number_of_sections(self, tv):
    self.tableview = tv
    return 1

  def tableview_number_of_rows(self, tv, section):
    return len(self.items)

  def tableview_can_delete(self, tv, section, row):
    return self.delete_enabled

  def tableview_can_move(self, tv, section, row):
    return self.move_enabled

  def tableview_accessory_button_tapped(self, tv, section, row):
    self.tapped_accessory_row = row
    if self.accessory_action:
      self.accessory_action(self)

  def tableview_did_select(self, tv, section, row):
    self.selected_row = row
    if self.action:
      self.action(self)

  def tableview_move_row(self, tv, from_section, from_row, to_section, to_row):
    if from_row == to_row:
      return
    moved_item = self.items[from_row]
    self.reload_disabled = True
    del self.items[from_row]
    self.items[to_row:to_row] = [moved_item]
    self.reload_disabled = False
    if self.edit_action:
      self.edit_action(self)

  def tableview_delete(self, tv, section, row):
    self.reload_disabled = True
    del self.items[row]
    self.reload_disabled = False
    tv.delete_rows([row])
    if self.edit_action:
      self.edit_action(self)

  def tableview_cell_for_row(self, tv, section, row):
    item = self.items[row]
    cell = ui.TableViewCell()
    cell.text_label.number_of_lines = self.number_of_lines
    if isinstance(item, dict):
      cell.text_label.text = item.get('title', '')
      img = item.get('image', None)
      if img:
        if isinstance(img, str):
          cell.image_view.image = ui.Image.named(img)
        elif isinstance(img, ui.Image):
          cell.image_view.image = img
      accessory = item.get('accessory_type', 'none')
      cell.accessory_type = accessory
    else:
      cell.text_label.text = str(item)
    if self.text_color:
      cell.text_label.text_color = self.text_color
    if self.highlight_color:
      bg_view = View(background_color=self.highlight_color)
      cell.selected_background_view = bg_view
    if self.font:
      cell.text_label.font = self.font
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
    self.source_items = [name2symbol(name) for name in self.order_list[:64]]

    self.table_view = ui.TableView()
    self.table_view.delegate = MyTableViewDelegate()
    #self.table_view.data_source = ui.ListDataSource(self.source_items)
    #self.data_source = MyTableViewDataSource()
    self.data_source = IconListDataSource(self.source_items)
    self.table_view.data_source = self.data_source
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

