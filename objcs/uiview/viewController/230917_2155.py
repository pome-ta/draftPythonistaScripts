#[https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py](https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py)

#from __future__ import print_function
# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/9

# coding: utf-8

from objc_util import *
import appex

SFSafariViewController = ObjCClass('SFSafariViewController')


@on_main_thread
def open_in_safari_vc(url):
  sfSafariViewController = SFSafariViewController.alloc()
  '''
  vc = SFSafariViewController.alloc().initWithURL_entersReaderIfAvailable_(
    nsurl(url), True)
  '''
  #vc = sfSafariViewController.initWithURL_entersReaderIfAvailable_(nsurl(url), True)
  vc = sfSafariViewController.initWithURL_(nsurl(url))

  app = UIApplication.sharedApplication()

  if app.keyWindow():
    window = app.keyWindow()
  else:
    window = app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()
  root_vc.presentViewController_animated_completion_(vc, True, None)
  #vc.release()


def main():
  if not appex.is_running_extension():
    print('This script is intended to be run from the sharing extension.')
    return
  url = appex.get_url()
  if not url:
    print('No input url')
    return
  open_in_safari_vc(url)


if __name__ == '__main__':
  #main()
  u = 'https://github.com/pome-ta/Pythonista3AdventCalendar2022sampleCode/blob/main/day00_requests/qiitaAPIv2.py'
  open_in_safari_vc(u)

