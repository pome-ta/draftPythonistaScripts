# coding: utf-8

#[https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py](https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py)

# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/9

from objc_util import ObjCClass, nsurl, on_main_thread, ObjCInstance, create_objc_class
import pdbg

SFSafariViewController = ObjCClass('SFSafariViewController')


class CustomSFSafariViewController:

  def __init__(self, url: str | ObjCInstance):
    self._this: ObjCInstance
    # xxx: ちゃんとガードしてない
    self.target_url = url if isinstance(url, ObjCInstance) else nsurl(str(url))

    self._override()

  def _override(self):
    # --- `SFSafariViewController` Methods
    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(window)

    # --- `SFSafariViewController` set up
    _methods = [
      viewDidAppear_,
    ]

    create_kwargs = {
      'name': '_vc',
      #'superclass': UIViewController,
      'superclass': SFSafariViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._this = _vc.alloc().initWithURL_(self.target_url).autorelease()

  @classmethod
  def new(cls, url) -> ObjCInstance:
    _cls = cls(url)
    return _cls._this


@on_main_thread
def open_in_safari_vc(url):
  ns_url = nsurl(url)
  _sf = SFSafariViewController.alloc()
  sf_vc = _sf.initWithURL_(ns_url).autorelease()

  sf_vc = CustomSFSafariViewController.new(url)
  pdbg.state(sf_vc)

  #pdbg.state(sf_vc)
  #print(type(ns_url))
  #print(isinstance(url, ObjCInstance))
  #isinstance

  app = ObjCClass('UIApplication').sharedApplication()

  if app.keyWindow():
    #print('t')
    window = app.keyWindow()
  else:
    print('f')
    window = app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()
  root_vc.presentViewController_animated_completion_(sf_vc, True, None)
  #sf_vc.release()


if __name__ == '__main__':
  u = 'https://github.com/pome-ta/Pythonista3AdventCalendar2022sampleCode/blob/main/day00_requests/qiitaAPIv2.py'
  open_in_safari_vc(u)

