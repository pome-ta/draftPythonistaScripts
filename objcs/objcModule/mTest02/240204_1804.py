from objc_util import ObjCInstance, sel

from objcista import *
from objcista.objcNavigationController import PlainNavigationController, ObjcNavigationController
from objcista.objcViewController import ObjcViewController

import pdbg


#class TopNavigationController(PlainNavigationController):
class TopNavigationController(ObjcNavigationController):

  def __init__(self):
    self.override()

  def override(self):

    @self.add_msg
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):

    super().willShowViewController(navigationController, viewController,
                                   animated)

    systemItem = UIBarButtonItem_SystemItem.done
    done_btn = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                 navigationController,
                                                 sel('doneButtonTapped:'))

    visibleViewController = navigationController.visibleViewController()

    # --- navigationItem
    navigationItem = visibleViewController.navigationItem()
    navigationItem.rightBarButtonItem = done_btn


class TopViewController(ObjcViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def didLoad(self, this: UIViewController):
    view = this.view()
    background_color = UIColor.systemBackgroundColor()
    view.setBackgroundColor_(background_color)
    navigationItem = this.navigationItem()
    navigationItem.setTitle_('あ')


if __name__ == "__main__":
  LAYOUT_DEBUG = True
  tvc = TopViewController.new()
  tnc = TopNavigationController.new(tvc, True)
  run_controller(tnc)

