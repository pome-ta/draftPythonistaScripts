# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller
# https://github.com/tdamdouni/Pythonista/blob/master/omz/SafariViewController.py
# coding: utf-8

from objc_util import ObjCClass, UIApplication, on_main_thread, UIColor, nsurl
import ui

SFSafariViewController = ObjCClass('SFSafariViewController')

view = ui.View()#frame=(0,0,600,600))

@on_main_thread
def open_in_safari_vc(url, tint_color=None):
  vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))
  if tint_color is not None:
    vc.view().tintColor = tint_color
  '''
  app = UIApplication.sharedApplication()
  root_vc = app.keyWindow().rootViewController()
  root_vc.presentViewController_animated_completion_(vc, True, None)
  vc.release()
  '''
  
  view.present(style='fullscreen') #must be presented for nextResponder to work
  
  
  view.objc_instance.nextResponder().addChildViewController_(vc)
  #view.objc_instance.addSubview_(vc)
  
  


if __name__ == '__main__':
  open_in_safari_vc(
    'https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller?language=objc',
    UIColor.orangeColor())

