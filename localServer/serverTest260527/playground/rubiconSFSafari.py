_TOP_DIR_NAME = 'serverTest260527'
_MODULES_DIR_NAME = 'modules'

# todo: `./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME}` にあるpackage のimport 準備
if __name__ == '__main__' and not __file__[:__file__.rfind('/')].endswith(
    _TOP_DIR_NAME):
  import pathlib
  import sys
  __parents = pathlib.Path(__file__).resolve().parents
  for __dir_path in __parents:
    if __dir_path.name == _TOP_DIR_NAME and (__modules_path := __dir_path /
                                             _MODULES_DIR_NAME).exists():
      sys.path.insert(0, str(__modules_path))
      break
  else:
    import warnings
    with warnings.catch_warnings():
      warnings.simplefilter('always', ImportWarning)
      __warning_message = f'./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME} not found in parent directories'
      warnings.warn(__warning_message, ImportWarning)

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, load_library

from rbedge import pdbr

load_library('SafariServices')


class SafariViewController(ObjCClass('SFSafariViewController')):

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')

    self.navigationController.setNavigationBarHidden(
      True,
      animated=True,
    )

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

if __name__ == '__main__':
  from pathlib import Path

  from rbedge.app import App
  from rbedge.utils import nsurl
  from objc_frameworks.UIKit import UIModalPresentationStyle
  
  from localServer import LocalServer


  ROOT_PATH = Path(__file__).parents[0]
  index_path = ROOT_PATH / '../docs/'

  with LocalServer(
      host='127.0.0.1',
      port=8000,
      root_dir=str(index_path),
      verbose=False,
  ) as server:

    url = 'https://github.com/ColdGrub1384/Pyto'
    url = server.url

    main_vc = SafariViewController.alloc().initWithURL_(nsurl(url))

    presentation_style = UIModalPresentationStyle.fullScreen
    #presentation_style = UIModalPresentationStyle.pageSheet

    app = App(main_vc, presentation_style)
    app.present()

