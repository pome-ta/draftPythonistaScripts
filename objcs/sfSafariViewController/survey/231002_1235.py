# coding: utf-8

#[https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py](https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py)

# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/9

from objc_util import ObjCClass, nsurl, on_main_thread
import pdbg


SFSafariViewController = ObjCClass('SFSafariViewController')



@on_main_thread
def open_in_safari_vc(url):
  sfSafariViewController = SFSafariViewController.alloc()
  # xxx: `new` だと取れない
  #sfSafariViewController = SFSafariViewController.new()
  '''
  vc = SFSafariViewController.alloc().initWithURL_entersReaderIfAvailable_(
    nsurl(url), True)
  '''
  #vc = sfSafariViewController.initWithURL_entersReaderIfAvailable_(nsurl(url), True)
  vc = sfSafariViewController.initWithURL_(nsurl(url))

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
  root_vc.presentViewController_animated_completion_(vc, True, None)
  vc.release()


if __name__ == '__main__':
  u = 'https://github.com/pome-ta/Pythonista3AdventCalendar2022sampleCode/blob/main/day00_requests/qiitaAPIv2.py'
  u = 'https://pome-ta.github.io/codeMirror6PlaySandBox/'
  open_in_safari_vc(u)

