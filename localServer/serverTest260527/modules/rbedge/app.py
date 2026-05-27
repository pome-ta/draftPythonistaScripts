from typing import Union

from pyrubicon.objc.api import ObjCClass

from objc_frameworks.UIKit import UIModalPresentationStyle

from .lifeCycle import loop
from .objcMainThread import onMainThread
from .rootNavigationController import RootNavigationController

from rbedge import pdbr

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')  # todo: アノテーション用


class App:

  def __init__(
    self,
    viewController: UIViewController,
    modalPresentationStyle: Union[UIModalPresentationStyle,
                                  int] = UIModalPresentationStyle.pageSheet):
    self.viewController = viewController
    # xxx: style 指定を力技で確認
    _automatic = UIModalPresentationStyle.automatic  # -2
    _blurOverFullScreen = UIModalPresentationStyle.blurOverFullScreen  # 8
    _pageSheet = UIModalPresentationStyle.pageSheet  # 1

    self.modalPresentationStyle = modalPresentationStyle if isinstance(
      modalPresentationStyle, int
    ) and _automatic <= modalPresentationStyle <= _blurOverFullScreen else _pageSheet

    self.set_rootViewController()

  def set_rootViewController(self) -> None:
    sharedApplication = UIApplication.sharedApplication
    objectEnumerator = sharedApplication.connectedScenes.objectEnumerator()

    while (windowScene := objectEnumerator.nextObject()):

      if windowScene.activationState == 0:
        break
    rootViewController = windowScene.keyWindow.rootViewController
    self.rootViewController = rootViewController

  def present(self, NavigationController=RootNavigationController) -> None:

    @onMainThread(sync=False)
    def present_viewController(viewController: UIViewController,
                               style: int) -> None:

      presentViewController = NavigationController.alloc(
      ).initWithRootViewController_(viewController)

      presentViewController.setModalPresentationStyle_(style)

      self.rootViewController.presentViewController_animated_completion_(
        presentViewController, True, None)

    present_viewController(self.viewController, self.modalPresentationStyle)
    self.main_loop()

  def main_loop(self) -> None:
    try:
      loop.run_forever()
    except Exception as e:
      loop.stop()
    finally:
      loop.close()

