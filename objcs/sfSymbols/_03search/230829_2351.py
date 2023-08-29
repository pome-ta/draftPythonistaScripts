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
    # xxx: あとでサイズとかやる
    x_margin = h * 0.5
    y_margin = x_margin / 2

    icon_size = h - x_margin

    img_frame = (x_margin, y_margin, icon_size, icon_size)
    image_view = ui.ImageView(frame=img_frame)
    image_view.image = item.get('image', None)
    image_view.content_mode = 1
    image_view.bg_color = 'maroon'

    label_frame = (x_margin + h, y_margin, w, icon_size)

    label = ui.Label(frame=label_frame)
    label.text = item.get('title', '')
    #label.font = ('.SFUI-Regular', 14.0)  #xxx: from `ui.ListDataSource` font
    label.bg_color = 'cyan'
    label.number_of_lines = self.number_of_lines

    cell.content_view.add_subview(image_view)
    cell.content_view.add_subview(label)
    #self.cell = cell
    return cell





class SearchTextFieldDelegate(object):

  def __init__(self, data_source:SymbolListDataSource):
    self.data_source = data_source
    self.all_items = self.data_source.items[:]
    

  def textfield_should_begin_editing(self, textfield):
    #print(f'1.should_begin:{textfield}\n')
    return True

  def textfield_did_begin_editing(self, textfield):
    #print(f'2.did_begin:{textfield}\n')
    pass

  def textfield_did_end_editing(self, textfield):
    #print(f'3.did_end:{textfield}\n')
    pass

  def textfield_should_return(self, textfield):
    textfield.end_editing()
    #print(f'4.should_return:{textfield}\n')
    return True

  def textfield_should_change(self, textfield, range, replacement):
    '''
    print(
      f'5.should_change:{textfield}, range:{range}, replacement:{replacement}')
    print(f'text:{textfield.text}\n')
    '''
    return True

  def textfield_did_change(self, textfield):
    # xxx: ここ使う
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
    self.search_field: ui.TextField
    self.search_wrap: ui.View
    self.symbol_table: ui.TableView
    self.set_up()

  def set_up(self):
    self.bg_color = 'cyan'

    self.search_field = self.create_search_field()
    self.symbol_table = self.create_symbol_table()

    self.order_list = get_order_list()
    self.order_list.sort()
    self.icons = self.order_list[:len(all_items)]
    self.source_items = [{
      'title': _name,
      'image': get_symbo_icon(_icon)
    } for _name, _icon in zip(all_items, self.icons)]

    self.symbol_data_source = SymbolListDataSource(self.source_items)
    
    
    self.search_field.delegate = SearchTextFieldDelegate(self.symbol_data_source)
    
    self.symbol_table.data_source = self.symbol_data_source
    

    self.add_subview(self.search_field)
    self.add_subview(self.symbol_table)

  def create_search_field(self) -> ui.TextField:
    _search_field = ui.TextField()
    #self.search_field.flex = 'W'
    _search_field.height = 32  # xxx: 仮決め打ち

    _search_field.clear_button_mode = 'always'
    _search_field.placeholder = 'search symbol name'
    return _search_field

  def create_symbol_table(self) -> ui.TableView:

    _symbol_table = ui.TableView()
    _symbol_table.flex = 'W'
    return _symbol_table

  def layout(self):
    _, _, w, h = self.frame
    # xxx: あとでサイズとかやる
    self.search_field.width = w * 0.92
    self.search_field.x = (w - self.search_field.width) / 2

    margin = h * 0.01

    table_margin = self.search_field.height + margin
    self.symbol_table.y = table_margin
    self.symbol_table.height = h - table_margin

    #self.search_field.y = margin


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
  #view.present(style='fullscreen', orientations=['portrait'])
  view.present(style='fullscreen')

