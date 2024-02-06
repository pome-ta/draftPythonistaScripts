from dataclasses import dataclass
from objc_util import ObjCInstance, sel, create_objc_class, on_main_thread

from objcista import *
from objcista.objcNavigationController import PlainNavigationController, ObjcNavigationController
from objcista.objcViewController import ObjcViewController

import pdbg

@dataclass
class UISplitViewController_Style:
  doubleColumn = 1
  tripleColumn = 2

class TopNavigationController(PlainNavigationController):

  def __init__(self):
    self.override()
    print('n')

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


def viewDidLoad(_self, _cmd):
  this = ObjCInstance(_self)
  view = this.view()
  background_color = UIColor.systemBackgroundColor()
  view.setBackgroundColor_(background_color)
  pdbg.state(this)

_methods = [
  viewDidLoad,
]

create_kwargs = {
  'name': '_vc',
  'superclass': UISplitViewController,
  'methods': _methods,
}

_vc = create_objc_class(**create_kwargs)

if __name__ == "__main__":
  #tvc = _vc.new()
  doubleColumn = UISplitViewController_Style.doubleColumn
  tvc = _vc.alloc().initWithStyle_(doubleColumn)
  #tnc = TopNavigationController.new(tvc, True)

  run_controller(tvc)
  #run_controller(tnc)

