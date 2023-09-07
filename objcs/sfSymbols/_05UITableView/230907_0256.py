from objc_util import ObjCClass, ObjCInstance
import ui

import pdbg

NSIndexPath = ObjCClass('NSIndexPath')
idx = NSIndexPath.indexPathForRow_inSection_(0, 0)

#pdbg.state(idx)

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


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.data = ui.ListDataSource(all_items)
    self.table = ui.TableView()
    self.table.flex = 'WH'
    self.table.data_source = self.data
    self.add_subview(self.table)

    self.count = 0

  def layout(self):
    _, _, w, h = self.frame
    if self.count:
      tbl = self.table.objc_instance
      cell = tbl.tableView_cellForRowAtIndexPath_(tbl, idx)
      #tableView_cellForRowAtIndexPath_
      #pdbg.state(self.table.objc_instance)
      #pdbg.all(cell)
      pdbg.state(cell)
    self.count += 1


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present(style='fullscreen')

