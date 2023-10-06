from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg

file_name = Path(__file__).name
#file_name = 'searchController'

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIView = ObjCClass('UIView')

UIColor = ObjCClass('UIColor')

systemDarkBlueColor = UIColor.systemDarkBlueColor()
systemDarkOrangeColor = UIColor.systemDarkOrangeColor()


class ObjcUIViewController:

  def __init__(self):
    self._this: ObjCInstance
    self._viewController: UIViewController

  @on_main_thread
  def _init(self):
    self._override_viewController()

    vc = self._viewController.new().autorelease()

    self._this = vc

  def _override_viewController(self):

    self.redView = UIView.alloc()

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      #print('viewDidLoad')
      this = ObjCInstance(_self)
      view = this.view()
      view.backgroundColor = systemDarkBlueColor

      CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
      self.redView.initWithFrame_(CGRectZero).autorelease()
      #self.redView.initWithFrame_(view.frame())
      self.redView.backgroundColor = systemDarkOrangeColor
      self.redView.translatesAutoresizingMaskIntoConstraints = False

      view.addSubview_(self.redView)
      '''
      bottomAnchor
      centerXAnchor
      centerYAnchor
      firstBaselineAnchor
      heightAnchor
      lastBaselineAnchor
      leadingAnchor
      leftAnchor
      rightAnchor
      topAnchor
      trailingAnchor
      widthAnchor
      '''

      NSLayoutConstraint.activateConstraints_([
        self.redView.centerXAnchor().constraintEqualToAnchor_(
          view.centerXAnchor()),
        self.redView.centerYAnchor().constraintEqualToAnchor_(
          view.centerYAnchor()),
        self.redView.widthAnchor().constraintEqualToAnchor_multiplier_(
          view.widthAnchor(), 0.9),
        self.redView.heightAnchor().constraintEqualToAnchor_multiplier_(
          view.heightAnchor(), 0.9),
      ])

    def viewWillAppear_(_self, _cmd, _animated):
      #print('viewWillAppear')
      pass

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      window = view.window()

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

    def didReceiveMemoryWarning(_self, _cmd):
      # Dispose of any resources that can be recreated.
      print('Dispose of any resources that can be recreated.')

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewWillAppear_,
      viewDidAppear_,
      viewWillDisappear_,
      viewDidDisappear_,
      viewWillLayoutSubviews,
      viewDidLayoutSubviews,
      didReceiveMemoryWarning,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    _cls._init()
    return _cls._this


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()
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
  #vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  ovc = ObjcUIViewController.new()
  present_objc(ovc)

