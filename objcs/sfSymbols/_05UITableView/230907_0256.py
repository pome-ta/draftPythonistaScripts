from objc_util import ObjCInstance
import ui

import pdbg

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
    print(self.count)
    self.count += 1


if __name__ == '__main__':
  view = MainView()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.present(style='fullscreen')

