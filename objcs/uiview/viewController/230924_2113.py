# coding: utf-8

#[https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py](https://github.com/tdamdouni/Pythonista/blob/master/viewcontroller/SafariViewControllerAppex.py)

# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/9


from pprint import pprint
from objc_util import ObjCClass, nsurl, on_main_thread
import pdbg

UIApplication = ObjCClass('UIApplication')
SFSafariViewController = ObjCClass('SFSafariViewController')


@on_main_thread
def open_in_safari_vc(vc):
  app = UIApplication.sharedApplication()

  if app.keyWindow():
    #print('t')
    window = app.keyWindow()
  else:
    print('f')
    window = app.windows().firstObject()

  '''
  print('# --- autolayoutTrace')
  pprint(window._autolayoutTrace())
  print('\n'*4)
  '''
  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()

  #pdbg.state(vc.navigationItem())

  root_vc.presentViewController_animated_completion_(vc, True, None)
  #pdbg.state(root_vc.childViewControllers())
  
  #vc.release()


def create_safari_vc(url):
  sfSafariViewController = SFSafariViewController.alloc()
  # xxx: `new` だと取れない
  #sfSafariViewController = SFSafariViewController.new()
  '''
  vc = SFSafariViewController.alloc().initWithURL_entersReaderIfAvailable_(
    nsurl(url), True)
  '''
  #vc = sfSafariViewController.initWithURL_entersReaderIfAvailable_(nsurl(url), True)
  vc = sfSafariViewController.initWithURL_(nsurl(url))
  #pdbg.state(vc.viewIfLoaded())
  return vc

@on_main_thread
def check_vc():
  app = UIApplication.sharedApplication()

  if app.keyWindow():
    #print('t')
    window = app.keyWindow()
  else:
    print('f')
    window = app.windows().firstObject()

  print('# --- autolayoutTrace')
  pprint(window._autolayoutTrace())

#@on_main_thread
def omt(vc):
  #pdbg.all(vc.view())
  #pdbg.state(vc.viewIfLoaded())
  #pdbg.state(vc.view())
  if vc.viewIfLoaded() != None:
    #pdbg.state(vc.childViewControllers())
    #pass
    #print('# --- autolayoutTrace')
    #pprint(vc.view()._autolayoutTrace())
    #pdbg.state(vc.tabBarItem())
    pdbg.state(vc)
    
    #pdbg.state(vc.navigationItem().navigationBar())
    
    #pdbg.state(vc.toolbarItems())
    
    #pdbg.state(vc.storyboard())
    
    
    #pdbg.state(vc.childViewControllersCount())
    
    


if __name__ == '__main__':
  u = 'https://github.com/pome-ta/Pythonista3AdventCalendar2022sampleCode/blob/main/day00_requests/qiitaAPIv2.py'
  _vc = create_safari_vc(u)
  open_in_safari_vc(_vc)
  #check_vc()
  #pdbg.state(_vc.navigationItem().title())
  #pdbg.state(_vc.view())
  #pdbg.all(_vc.view())
  omt(_vc)

