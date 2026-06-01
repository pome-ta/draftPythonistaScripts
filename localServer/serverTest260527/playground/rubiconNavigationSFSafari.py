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
from pyrubicon.objc.runtime import send_super, objc_id, load_library

from rbedge.lifeCycle import loop
from rbedge import pdbr

load_library('SafariServices')

UINavigationController = ObjCClass('UINavigationController')
SFSafariViewController = ObjCClass('SFSafariViewController')


class NavigationController(UINavigationController):

  @objc_method
  def initWithRootViewController_(self, rootViewController):
    send_super(__class__,
               self,
               'initWithRootViewController:',
               rootViewController,
               argtypes=[
                 objc_id,
               ])

    self.setNavigationBarHidden_animated_(True, True)
    return self

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    loop.stop()

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

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

    url = server.url

    main_vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))

    presentation_style = UIModalPresentationStyle.fullScreen
    #presentation_style = UIModalPresentationStyle.pageSheet

    app = App(main_vc, presentation_style)
    app.present(NavigationController)

