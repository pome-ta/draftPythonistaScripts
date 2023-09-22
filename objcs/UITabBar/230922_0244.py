# coding: utf-8

# [pythonistaでUITabBarController](https://gist.github.com/shntn/dc9e1b1086bcda88c49ff72c1fcd546f)

from objc_util import ObjCClass, on_main_thread
import ui

import pdbg

UIApplication = ObjCClass('UIApplication')
UIColor = ObjCClass('UIColor')

UIViewController = ObjCClass('UIViewController')
UIView = ObjCClass('UIView')
UILabel = ObjCClass('UILabel')

UITabBarController = ObjCClass('UITabBarController')
UITabBarItem = ObjCClass('UITabBarItem')
UITabBar = ObjCClass('UITabBar')


class RootView:

  def __init__(self):
    rootVC = UIApplication.sharedApplication().keyWindow().rootViewController()
    #pdbg.state(rootVC)
    self.tabviewcontroller = rootVC.detailViewController()

  def add(self, viewcontroller):
    self.tabviewcontroller.addTabWithViewController_(viewcontroller)


def makeViewController(item, tag, view):
  tab_bar_item = UITabBarItem.alloc().initWithTabBarSystemItem_tag_(
    item, tag).autorelease()
  viewctrl = UIViewController.new().autorelease()
  viewctrl.tabBarItem = tab_bar_item
  viewctrl.view = view
  return viewctrl


@on_main_thread
def main():
  # tabbaritem 1
  tab_frame = ((50.0, 50.0), (200.0, 50.0))
  '''
  label = UILabel.alloc().initWithFrame_(
    CGRect(CGPoint(50, 50), CGSize(200, 50)))
  '''
  label = UILabel.alloc().initWithFrame_(tab_frame)
  label.text = 'TAB1'
  view = UIView.new().autorelease()
  view.backgroundColor = UIColor.color(red=0.5, green=1.0, blue=0.7, alpha=1.0)
  view.addSubview(label)
  vc1 = makeViewController(7, 0, view)

  # tabbaritem 2
  '''
  label = UILabel.alloc().initWithFrame_(
    CGRect(CGPoint(50, 50), CGSize(200, 50)))
  '''
  label = UILabel.alloc().initWithFrame_(tab_frame)
  label.text = 'TAB2'
  view = UIView.new().autorelease()
  view.backgroundColor = UIColor.color(red=0.5, green=0.7, blue=1.0, alpha=1.0)
  view.addSubview(label)
  vc2 = makeViewController(8, 1, view)

  # TabBarController
  tbc = UITabBarController.alloc().init().autorelease()
  #tbc.setViewControllers_animated_(ns([vc1, vc2]), False)
  #pdbg.state(tbc)
  #tbc.setViewControllers_animated_([vc1, vc2], False)
  tbc.setViewControllers_animated_([vc1, vc2], True)
  tbc.title = 'TabBarControll'

  rootview = RootView()
  rootview.add(tbc)


if __name__ == '__main__':
  main()

