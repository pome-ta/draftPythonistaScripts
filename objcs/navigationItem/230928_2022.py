from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UIColor = ObjCClass('UIColor')


#pdbg.state(UINavigationController.alloc())

class ObjcUIViewController:

  def __init__(self):
    self._this: UIViewController
    self._override()

  def _override(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      #view.backgroundColor = UIColor.cyanColor()
      #this.navigationItem().setTitle_('ほげ')
      #this.navigationItem().title = 'h'
      #pdbg.state(this.navigationItem())
      #this.title = 'ほげ'
      #pdbg.state(this)

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.state(this)
      #pdbg.state(this.navigationItem().title())

    def viewWillDisappear_(_self, _cmd, _animated):
      #print('viewWillDisappear')
      pass

    def viewDidDisappear_(_self, _cmd, _animated):
      #print('viewDidDisappear')
      pass

    def viewWillLayoutSubviews(_self, _cmd):
      #print('viewWillLayoutSubviews')
      pass

    def viewDidLayoutSubviews(_self, _cmd):
      #print('viewDidLayoutSubviews')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()
      #pdbg.all(window)
      #this.dismissViewControllerAnimated_completion_(True, None)
      #pass

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      #'superclass': UINavigationController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._this = _vc.new()

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._this


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()
  pdbg.state(root_vc)
  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()

  #pdbg.state(vc)
  # [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
  '''
  case -2 : automatic
  case -1 : none
  case  0 : fullScreen
  case  1 : pageSheet <- default ?
  case  2 : formSheet
  case  3 : currentContext
  case  4 : custom
  case  5 : overFullScreen
  case  6 : overCurrentContext
  case  7 : popover
  case  8 : blurOverFullScreen
  '''
  
  #nvc = UINavigationController.alloc().initWithRootViewController_(root_vc)
  #vc.setModalPresentationStyle_(0)
  #pdbg.state(root_vc)
  #nvc = UINavigationController.alloc().initWithRootViewController_(vc)
  #pdbg.state(nvc)
  #pdbg.state(vc)
  
  #root_vc.presentViewController_animated_completion_(vc, True, None)
  
  #root_vc.presentViewController_animated_completion_(nvc, True, None)
  
  #root_vc.didMoveToParentViewController_(vc)

  
  
  #nvc.presentViewController_animated_completion_(vc, True, None)
  #pdbg.state(root_vc)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

