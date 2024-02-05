from objc_util import ObjCInstance, sel, create_objc_class, on_main_thread

from objcista import *
from objcista.objcNavigationController import PlainNavigationController, ObjcNavigationController
from objcista.objcViewController import ObjcViewController

import pdbg


def doneButtonTapped_(_self, _cmd, _sender):
  this = ObjCInstance(_self)
  visibleViewController = this.visibleViewController()
  visibleViewController.dismissViewControllerAnimated_completion_(True, None)


def viewDidLoad(_self, _cmd):
  this = ObjCInstance(_self)
  view = this.view()
  background_color = UIColor.systemBackgroundColor()
  view.setBackgroundColor_(background_color)

  #navigationController = this.navigationController()
  navigationItem = this.navigationItem()
  systemItem = UIBarButtonItem_SystemItem.done
  done_btn = UIBarButtonItem.alloc(
  ).initWithBarButtonSystemItem_target_action_(systemItem,
                                               navigationItem,
                                               sel('doneButtonTapped:'))

  
  
  
  #visibleViewController = navigationController.visibleViewController()

  # --- navigationItem
  #navigationItem = visibleViewController.navigationItem()
  navigationItem.rightBarButtonItem = done_btn
  

  #pdbg.state(navigationItem)


_methods = [
  viewDidLoad,
  doneButtonTapped_,
]

create_kwargs = {
  'name': '_vc',
  'superclass': UISplitViewController,
  'methods': _methods,
}

_vc = create_objc_class(**create_kwargs)

if __name__ == "__main__":
  tvc = _vc.new()

  run_controller(tvc)

