from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread

import pdbg

UIApplication = ObjCClass('UIApplication')
UIViewController = ObjCClass('UIViewController')

UIView = ObjCClass('UIView')
UIColor = ObjCClass('UIColor')

class ObjcUIViewController(object):

  def __init__(self):
    # xxx: 名前酷いけど取り急ぎ
    self._this: ObjCInstance
    self.tmp_frame = ((0.0, 0.0), (100.0, 100.0))
    self._override()

  def _override(self):
    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      print('--- viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      #view.setBackgroundColor_
      view.backgroundColor = UIColor.redColor()
      sub_view = UIView.new()
      sub_view.setFrame_(self.tmp_frame)
      sub_view.setAutoresizingMask_((1 << 1) | (1 << 4))
      sub_view.backgroundColor = UIColor.cyanColor()
      
      view.addSubview_(sub_view)
      
      #pdbg.state(view)
      

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
      #'protocols': _protocols,
    }
    _vc = create_objc_class(**create_kwargs)
    #pdbg.state(_vc.new())
    self._this = _vc.new()


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
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  _vc_i = ObjcUIViewController()
  _vc = _vc_i._this
  present_objc(_vc)

