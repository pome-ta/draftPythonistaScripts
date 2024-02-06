from dataclasses import dataclass
from objc_util import ObjCInstance, sel, create_objc_class, on_main_thread

from objcista import *
from objcista.objcNavigationController import PlainNavigationController, ObjcNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

import pdbg


@dataclass
class UISplitViewController_Style:
  doubleColumn = 1
  tripleColumn = 2


@dataclass
class UISplitViewController_Column:
  primary = 0
  supplementary = 1
  secondary = 2
  compact = 3


class TopNavigationController(PlainNavigationController):

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
    self.main_text = 'UIKitCatalog'

  def didLoad(self, this: UIViewController):
    view = this.view()
    background_color = UIColor.systemBackgroundColor()
    view.setBackgroundColor_(background_color)

    label_kwargs = {
      'text': self.main_text,
      'LAYOUT_DEBUG': LAYOUT_DEBUG,
    }
    self.main_label = ObjcLabel.new(**label_kwargs)
    self.main_label.setFont_(UIFont.systemFontOfSize_(26.0))

    view.addSubview(self.main_label)

    # --- layout
    layoutMarginsGuide = view.layoutMarginsGuide()

    NSLayoutConstraint.activateConstraints_([
      self.main_label.centerXAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.centerXAnchor()),
      self.main_label.centerYAnchor().constraintEqualToAnchor_(
        layoutMarginsGuide.centerYAnchor()),
    ])


def viewDidLoad(_self, _cmd):
  this = ObjCInstance(_self)
  view = this.view()
  background_color = UIColor.systemBackgroundColor()
  view.setBackgroundColor_(background_color)

  vc = TopViewController.new()
  nvc = TopNavigationController.new(vc, True)

  secondary = UISplitViewController_Column.secondary

  this.setViewController_forColumn_(nvc, secondary)
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
  LAYOUT_DEBUG = True
  #tvc = _vc.new()
  doubleColumn = UISplitViewController_Style.doubleColumn
  tvc = _vc.alloc().initWithStyle_(doubleColumn)
  #tnc = TopNavigationController.new(tvc, True)

  run_controller(tvc)
  #run_controller(tnc)

