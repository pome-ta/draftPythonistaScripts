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

from objc_frameworks.UIKit import UIModalPresentationStyle

from rbedge.lifeCycle import loop
from rbedge.objcMainThread import onMainThread
from rbedge.utils import nsurl

SFSafariViewController = ObjCClass('SFSafariViewController')
UIApplication = ObjCClass('UIApplication')
NSURL = ObjCClass('NSURL')


def get_rootViewController() -> None:
  sharedApplication = UIApplication.sharedApplication
  objectEnumerator = sharedApplication.connectedScenes.objectEnumerator()

  while (windowScene := objectEnumerator.nextObject()):

    if windowScene.activationState == 0:
      break
  rootViewController = windowScene.keyWindow.rootViewController
  return rootViewController


def main_loop() -> None:
  try:
    loop.run_forever()
  except Exception as e:
    loop.stop()
  finally:
    loop.close()


def main(url, modalPresentationStyle):

  rootViewController = get_rootViewController()

  @onMainThread(sync=False)
  def present_viewController(url, style: int) -> None:

    presentViewController = SFSafariViewController.alloc().initWithURL_(nsurl(url))
    #presentViewController = SFSafariViewController.alloc().initWithURL_(url)
    presentViewController.setModalPresentationStyle_(style)

    rootViewController.presentViewController(
      presentViewController,
      animated=True,
      completion=None,
    )
    #rootViewController.release()

  present_viewController(url, modalPresentationStyle)
  main_loop()


if __name__ == '__main__':

  from pathlib import Path
  ROOT_PATH = Path(__file__).parents[0]

  index_path = ROOT_PATH / '../docs/'


  url = NSURL.fileURLWithPath_isDirectory_(str(index_path.resolve()), False)
  print(url)

  #url = 'https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/textarea'
  presentation_style = UIModalPresentationStyle.fullScreen

  main(url, presentation_style)

