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
    #view.setBackgroundColor_(background_color)

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


UIButton = ObjCClass('UIButton')
UIButtonConfiguration = ObjCClass('UIButtonConfiguration')
UIControlEventTouchUpInside = 1 << 6


class FirstViewController(ObjcViewController):

  def __init__(self):
    super().__init__()
    self.nav_title = 'FirstViewController'
    self.sub_view = UIView.alloc()
    self.btn = UIButton.new()

  def override(self):

    @self.add_msg
    def btnClick_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      sender = ObjCInstance(_sender)
      svc = SecondViewController.new(name='SecondViewController')
      navigationController = this.navigationController()
      navigationController.pushViewController_animated_(svc, True)

  def didLoad(self, this: UIViewController):
    view = this.view()
    view.setBackgroundColor_(UIColor.systemBlueColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_('tap')
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemGreenColor())

    self.btn.setConfiguration_(config)

    self.btn.addTarget_action_forControlEvents_(this, sel('btnClick:'),
                                                UIControlEventTouchUpInside)

    # --- layout
    view.addSubview_(self.btn)

    self.btn.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.btn.centerXAnchor().constraintEqualToAnchor_(view.centerXAnchor()),
      self.btn.centerYAnchor().constraintEqualToAnchor_(view.centerYAnchor()),
      self.btn.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.4),
      self.btn.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.1),
    ])


class SecondViewController(ObjcViewController):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.nav_title = kwargs['name']
    self.sub_view = UIView.alloc()
    self.btn = UIButton.new()

  def override(self):

    @self.add_msg
    def btnClick_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      sender = ObjCInstance(_sender)
      tvc = ThirdViewController.new()
      navigationController = this.navigationController()
      navigationController.pushViewController_animated_(tvc, True)

  def didLoad(self, this: UIViewController):
    view = this.view()
    view.setBackgroundColor_(UIColor.systemGreenColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_('tap')
    config.setBaseBackgroundColor_(UIColor.systemPinkColor())
    config.setBaseForegroundColor_(UIColor.systemBlueColor())

    self.btn.setConfiguration_(config)

    self.btn.addTarget_action_forControlEvents_(this, sel('btnClick:'),
                                                UIControlEventTouchUpInside)

    # --- layout
    view.addSubview_(self.btn)

    self.btn.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.btn.centerXAnchor().constraintEqualToAnchor_(view.centerXAnchor()),
      self.btn.centerYAnchor().constraintEqualToAnchor_(view.centerYAnchor()),
      self.btn.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.4),
      self.btn.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.1),
    ])


class ThirdViewController(ObjcViewController):

  def __init__(self):
    super().__init__()
    self.nav_title = 'ThirdViewController'
    self.sub_view = UIView.alloc()
    self.btn = UIButton.new()

  def override(self):

    def btnClick_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      navigationController = this.navigationController()
      visibleViewController = navigationController.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

    self.add_msg(btnClick_)

  def didLoad(self, this: UIViewController):
    view = this.view()
    view.setBackgroundColor_(UIColor.systemPinkColor())

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    config = UIButtonConfiguration.tintedButtonConfiguration()
    config.setTitle_('tap')
    config.setBaseBackgroundColor_(UIColor.systemGreenColor())
    config.setBaseForegroundColor_(UIColor.systemPinkColor())

    self.btn.setConfiguration_(config)

    self.btn.addTarget_action_forControlEvents_(this, sel('btnClick:'),
                                                UIControlEventTouchUpInside)

    # --- layout
    view.addSubview_(self.btn)

    self.btn.translatesAutoresizingMaskIntoConstraints = False

    NSLayoutConstraint.activateConstraints_([
      self.btn.centerXAnchor().constraintEqualToAnchor_(view.centerXAnchor()),
      self.btn.centerYAnchor().constraintEqualToAnchor_(view.centerYAnchor()),
      self.btn.widthAnchor().constraintEqualToAnchor_multiplier_(
        view.widthAnchor(), 0.4),
      self.btn.heightAnchor().constraintEqualToAnchor_multiplier_(
        view.heightAnchor(), 0.1),
    ])


def viewDidLoad(_self, _cmd):
  this = ObjCInstance(_self)
  view = this.view()
  background_color = UIColor.systemBackgroundColor()
  systemRedColor = UIColor.systemRedColor()
  #view.setBackgroundColor_(background_color)
  view.setBackgroundColor_(systemRedColor)

  vc = TopViewController.new()
  nvc = TopNavigationController.new(vc,True)
  #ObjcNavigationController

  fvc = FirstViewController.new()
  fnv = TopNavigationController.new(fvc,True)
  #fnv.setTitle_('h')
  #pdbg.state(fnv.navigationBar())

  secondary = UISplitViewController_Column.secondary
  primary = UISplitViewController_Column.primary

  this.setViewController_forColumn_(nvc, primary)
  this.setViewController_forColumn_(fnv, secondary)
  #pdbg.state(this.presentsWithGesture())


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

