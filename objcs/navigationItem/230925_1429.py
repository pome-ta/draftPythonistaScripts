from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')
UINavigationController = ObjCClass('UINavigationController')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

UIView = ObjCClass('UIView')
UIColor = ObjCClass('UIColor')

#pdbg.state(UINavigationController)


class ObjcUIViewController(object):

  def __init__(self):
    # xxx: 名前酷いけど取り急ぎ
    self._this: ObjCInstance
    self._override()
    #pdbg.state(self._this)

  def _override(self):
    # --- `UIViewController` Methods

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      #this.viewDidLoad()
      #this.navigationController = UINavigationController.new()
      view = this.view()
      #view.setBackgroundColor_
      view.backgroundColor = UIColor.redColor()
      #pdbg.state(view)
      #print('--- viewDidLoad')
      #pdbg.state(this.navigationController())
      #this.navigationItem().setRightBarButtonItem_

      #pdbg.state(this)
      _close_btn = UIBarButtonItem.new()
      close_btn = _close_btn.initWithBarButtonSystemItem_target_action_(
        0, this, None)
      this.navigationItem().setRightBarButtonItem_(close_btn)
      #pdbg.state(close_btn)
      #this.setTitle_('ほげぇ〜☺️')
      this.navigationItem().setTitle_('ほげぇ〜☺️')
      pdbg.state(this)
      #print(this)

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UINavigationController,
      'methods': _methods,
      #'protocols': _protocols,
    }
    _vc = create_objc_class(**create_kwargs)
    #pdbg.state(_vc.new())
    self._this = _vc.new()

  @classmethod
  def new(cls):
    _cls = cls()
    return _cls._this


@on_main_thread
def present_objc(vc):
  # xxx: 全体的に改善
  app = UIApplication.sharedApplication()
  if app.keyWindow():
    #print('t')
    window = app.keyWindow()
  else:
    #print('f')
    window = app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()
  #pdbg.state(root_vc.modalPresentationStyle())
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

  #vc.setModalPresentationStyle_(8)
  #vc.setModalPresentationStyle_(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  #_vc_i = ObjcUIViewController()
  #_vc = _vc_i._this
  #present_objc(_vc)
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

