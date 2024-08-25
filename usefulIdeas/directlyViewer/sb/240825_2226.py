from pathlib import Path
import ui


class MyTableViewDataSource(object):

  def tableview_number_of_sections(self, tableview):
    # Return the number of sections (defaults to 1)
    return 1

  def tableview_number_of_rows(self, tableview, section):
    # Return the number of rows in the section
    return 0

  def tableview_cell_for_row(self, tableview, section, row):
    # Create and return a cell for the given section/row
    cell = ui.TableViewCell()
    cell.text_label.text = 'Foo Bar'
    return cell

  def tableview_title_for_header(self, tableview, section):
    # Return a title for the given section.
    # If this is not implemented, no section headers will be shown.
    return 'Some Section'

  def tableview_can_delete(self, tableview, section, row):
    # Return True if the user should be able to delete the given row.
    return True

  def tableview_can_move(self, tableview, section, row):
    # Return True if a reordering control should be shown for the given row (in editing mode).
    return True

  def tableview_delete(self, tableview, section, row):
    # Called when the user confirms deletion of the given row.
    pass

  def tableview_move_row(self, tableview, from_section, from_row, to_section,
                         to_row):
    # Called when the user moves a row with the reordering control (in editing mode).
    pass



class MyView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'


  def will_close(self):
    pass

  def layout(self):
    pass


root = Path()
t_path = root / Path('../' * 3)

for f in t_path.iterdir():
  print(f.name)

if __name__ == '__main__':
  v = MyView()
  #view.present(style='fullscreen', orientations=['portrait'])


