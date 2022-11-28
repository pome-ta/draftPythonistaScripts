from pathlib import Path
import os
from objc_util import ObjCClass, nsurl
import ui

NSBundle = ObjCClass('NSBundle')


class FolderBrowser:
  def __init__(self, path):
    self.root_dir = path
    # todo: 繰り返し防止考える
    self.btn_done = ui.ButtonItem(title='Done')
    self.btn_done.action = self.get_done
    init_table = ui.TableView()
    list_source = ui.ListDataSource(self.create_list(self.root_dir))
    list_source.action = self.select_cell
    init_table.data_source = list_source
    init_table.delegate = list_source
    init_table.name = self.call_dir.name
    self.activ_table = init_table
    self.activ_table.right_button_items = [self.btn_done]
    self.nav = ui.NavigationView(self.activ_table)

    # todo: Home に戻る
    home = ui.ButtonItem()
    home.image = ui.Image.named('Home')
    home.action = self.goto_home
    self.nav.left_button_items = [home]

  def create_list(self, root_path):
    self.call_dir = root_path
    dirs = sorted([d for d in self.call_dir.iterdir()])
    set_items = []
    for dir in dirs:

      if dir.suffix:
        f_img = ui.Image.named('FileOther')
      else:
        f_img = ui.Image.named('Folder')
      set_items.append({'title': dir.name, 'image': f_img, 'path': dir})
    return set_items

  def select_cell(self, sender):
    selection = sender.items[sender.selected_row]
    # todo: 繰り返し防止考える
    slct_dir = selection['path']
    slct_list_source = ui.ListDataSource(self.create_list(slct_dir))
    slct_table = ui.TableView()
    slct_list_source.action = self.select_cell
    slct_table.data_source = slct_list_source
    slct_table.delegate = slct_list_source
    slct_table.name = selection['title']
    self.activ_table = slct_table
    self.activ_table.right_button_items = [self.btn_done]
    self.nav.push_view(self.activ_table)

  def goto_home(self, sender):
    # todo: この戻り方でええのか？
    home_list_source = ui.ListDataSource(self.create_list(self.root_dir))
    home_table = ui.TableView()
    home_list_source.action = self.select_cell
    home_table.data_source = home_list_source
    home_table.delegate = home_list_source
    home_table.name = self.root_dir.name
    self.activ_table = home_table
    self.activ_table.right_button_items = [self.btn_done]
    self.nav.push_view(self.activ_table)

  def get_done(self, sender):
    print(self.call_dir)

  def show_browser(self):
    #self.nav.name = 'Choose directly ...'
    self.nav.present()  #hide_title_bar=True)


def get_bundle_path(path=None):
  obj_lib = NSBundle.bundleWithPath_(path).bundlePath() if (
    path) else NSBundle.mainBundle().resourcePath()
  root_dir = Path.expanduser(Path(str(obj_lib)))
  return root_dir


if __name__ == '__main__':
  uri = '/System/Library'
  uri = '/'
  '''
  uri = None
  uri = os.getcwd() + '/../../../..'
  PA2UITheme = ObjCClass('PA2UITheme')
  theme_dict = PA2UITheme.sharedTheme().userThemesPath()
  uri = str(theme_dict) + '/../../..'
  '''

  bundle_path = get_bundle_path(uri)
  fb = FolderBrowser(bundle_path)
  fb.show_browser()
