# coding: utf-8

#[https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py](https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py)

# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/9

from objc_util import ObjCClass, ObjCInstance, create_objc_class
from objc_util import on_main_thread, nsurl

import pdbg

UIView = ObjCClass('UIView')
UIColor = ObjCClass('UIColor')
SFSafariViewController = ObjCClass('SFSafariViewController')


class CustomSFSafariViewController:

  def __init__(self):
    self._this: ObjCInstance
    self._override()

  def _override(self):
    # --- `SFSafariViewController` Methods

    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      #view = this.view()
      uiview = UIView.new()
      frame = ((0.0, 0.0), (100.0, 100.0))
      uiview.setFrame_(frame)
      uiview.setAutoresizingMask_(1 << 1)
      uiview.backgroundColor = UIColor.cyanColor()
      #this.view = uiview

      #pdbg.state(view.window())
      #print('--- viewDidLoad')
      #pdbg.state(view)

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      uiview = UIView.new()
      frame = ((0.0, 0.0), (100.0, 100.0))
      uiview.setFrame_(frame)
      uiview.setAutoresizingMask_(1 << 1)
      uiview.backgroundColor = UIColor.cyanColor()
      #this.view = uiview
      #view = this.view()
      #window = view.window()
      #pdbg.state(this.navigationController())
      #pdbg.state(this.navigationItem())
      #pdbg.state(this.navigationItem().leftBarButtonItems())
      #pdbg.state(window)
      #pdbg.state(view)

    # --- `SFSafariViewController` set up
    _methods = [
      viewDidLoad,
      viewDidAppear_,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': SFSafariViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._this = _vc.alloc()

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._this


@on_main_thread
def open_in_safari_vc(url):
  ns_url = nsurl(url)
  _sf = CustomSFSafariViewController.new()
  sf_vc = _sf.initWithURL_(ns_url).autorelease()

  app = ObjCClass('UIApplication').sharedApplication()

  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()
  root_vc.presentViewController_animated_completion_(sf_vc, True, None)
  #pdbg.state(root_vc.presentedViewController().navigationController())
  #sf_vc.release()


if __name__ == '__main__':
  u = 'https://github.com/pome-ta/Pythonista3AdventCalendar2022sampleCode/blob/main/day00_requests/qiitaAPIv2.py'
  open_in_safari_vc(u)

