import ctypes
from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread, class_getSuperclass, nsurl, c
from objc_util import sel, CGRect

import pdbg


# wip: 今後引数サイズを考慮する
def objc_msgSendSuper(super, selector):
  _objc_msgSendSuper = c.objc_msgSendSuper
  _objc_msgSendSuper.argtypes = [
    ctypes.c_void_p,  # super
    ctypes.c_void_p,  # selector
  ]
  _objc_msgSendSuper.restype = ctypes.c_void_p
  return _objc_msgSendSuper(super, selector)


class objc_super(ctypes.Structure):
  #ref: [id | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/id?language=objc)
  # ref: [Class | Apple Developer Documentation](https://developer.apple.com/documentation/objectivec/class?language=objc)
  _fields_ = [
    ('receiver', ctypes.c_void_p),  # encoding(b"@")
    ('super_class', ctypes.c_void_p),  # encoding(b"#")
  ]


# --- navigation
UINavigationController = ObjCClass('UINavigationController')
UINavigationBarAppearance = ObjCClass('UINavigationBarAppearance')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

# --- viewController
UIViewController = ObjCClass('UIViewController')

# --- view
UIView = ObjCClass('UIView')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

UIColor = ObjCClass('UIColor')
NSURL = ObjCClass('NSURL')
NSURLRequest = ObjCClass('NSURLRequest')

# --- WKWebView
WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')
WKWebsiteDataStore = ObjCClass('WKWebsiteDataStore')

UIRefreshControl = ObjCClass('UIRefreshControl')


class WebViewController:

  def __init__(self):
    self._viewController: UIViewController
    self.webView: WKWebView
    self.targetURL: Path | str = 'https://yahoo.co.jp'
    self.nav_title: str = 'nav_title'

  def _override_viewController(self):

    # --- `UIViewController` Methods
    def loadView(_self, _cmd):
      this = ObjCInstance(_self)
      # todo: loadView override
      super_cls = class_getSuperclass(self._viewController)
      super_struct = objc_super(_self, super_cls)
      objc_msgSendSuper(ctypes.byref(super_struct), sel('loadView'))

      webConfiguration = WKWebViewConfiguration.new()
      websiteDataStore = WKWebsiteDataStore.nonPersistentDataStore()
      webConfiguration.websiteDataStore = websiteDataStore
      webConfiguration.preferences().setValue_forKey_(
        True, 'allowFileAccessFromFileURLs')

      CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
      self.webView = WKWebView.alloc().initWithFrame_configuration_(
        CGRectZero, webConfiguration)

      self.webView.navigationDelegate = this

      self.webView.scrollView().bounces = True
      refreshControl = UIRefreshControl.new()
      valueChanged = 1 << 12
      refreshControl.addTarget_action_forControlEvents_(
        this, sel('refreshWebView:'), valueChanged)

      self.webView.scrollView().refreshControl = refreshControl
      this.view = self.webView

    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()

      #view.backgroundColor = UIColor.systemDarkRedColor()
      navigationItem = this.navigationItem()
      navigationItem.title = self.nav_title

      # --- load url
      if (Path(self.targetURL).exists()):
        target_path = Path(self.targetURL)
        fileURLWithPath = NSURL.fileURLWithPath_isDirectory_
        folder_path = fileURLWithPath(str(target_path.parent), True)
        index_path = fileURLWithPath(str(target_path), False)
        self.webView.loadFileURL_allowingReadAccessToURL_(
          index_path, folder_path)
      else:
        url = NSURL.URLWithString_(self.targetURL)
        reloadIgnoringLocalCacheData = 1
        timeoutInterval = 10
        request = NSURLRequest.requestWithURL_cachePolicy_timeoutInterval_(
          url, reloadIgnoringLocalCacheData, timeoutInterval)
        self.webView.loadRequest_(request)

    def refreshWebView_(_self, _cmd, _sender):
      sender = ObjCInstance(_sender)
      self.webView.reload()
      sender.endRefreshing()

    # --- `WKNavigationDelegate` Methods
    def webView_didFinishNavigation_(_self, _cmd, _webView, _navigation):
      this = ObjCInstance(_self)
      webView = ObjCInstance(_webView)

      title = webView.title()
      this.navigationItem().title = str(title)

    # --- `UIViewController` set up
    _methods = [
      loadView,
      viewDidLoad,
      refreshWebView_,
      webView_didFinishNavigation_,
    ]

    _protocols = [
      'WKNavigationDelegate',
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
      'protocols': _protocols,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  @on_main_thread
  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    return vc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._init()

  @classmethod
  def load_url(cls, targetURL: Path | str) -> ObjCInstance:
    _cls = cls()
    _cls.targetURL = url
    return _cls._init()


class NavigationController:

  def __init__(self):
    self._navigationController: UINavigationController

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

    # --- `UINavigationController` set up
    _methods = [
      doneButtonTapped_,
    ]

    create_kwargs = {
      'name': '_nv',
      'superclass': UINavigationController,
      'methods': _methods,
    }
    _nv = create_objc_class(**create_kwargs)
    self._navigationController = _nv

  def create_navigationControllerDelegate(self):
    # --- `UINavigationControllerDelegate` Methods
    def navigationController_willShowViewController_animated_(
        _self, _cmd, _navigationController, _viewController, _animated):

      navigationController = ObjCInstance(_navigationController)
      viewController = ObjCInstance(_viewController)

      # --- appearance
      appearance = UINavigationBarAppearance.alloc()
      appearance.configureWithDefaultBackground()

      # --- navigationBar
      navigationBar = navigationController.navigationBar()

      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance

      viewController.setEdgesForExtendedLayout_(0)

      done_btn = UIBarButtonItem.alloc(
      ).initWithBarButtonSystemItem_target_action_(0, navigationController,
                                                   sel('doneButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()
      navigationItem.rightBarButtonItem = done_btn

    # --- `UINavigationControllerDelegate` set up
    _methods = [
      navigationController_willShowViewController_animated_,
    ]
    _protocols = [
      'UINavigationControllerDelegate',
    ]

    create_kwargs = {
      'name': '_nvDelegate',
      'methods': _methods,
      'protocols': _protocols,
    }
    _nvDelegate = create_objc_class(**create_kwargs)
    return _nvDelegate.new()

  @on_main_thread
  def _init(self, vc: UIViewController):
    self._override_navigationController()
    _delegate = self.create_navigationControllerDelegate()
    nv = self._navigationController.alloc()
    nv.initWithRootViewController_(vc).autorelease()
    nv.setDelegate_(_delegate)
    return nv

  @classmethod
  def new(cls, vc: UIViewController) -> ObjCInstance:
    _cls = cls()
    return _cls._init(vc)


@on_main_thread
def present_objc(vc):
  app = ObjCClass('UIApplication').sharedApplication()
  window = app.keyWindow() if app.keyWindow() else app.windows().firstObject()

  root_vc = window.rootViewController()

  while root_vc.presentedViewController():
    root_vc = root_vc.presentedViewController()
  vc.setModalPresentationStyle(1)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  #m_vc = WebViewController.new()
  url = 'https://www.apple.com'
  m_vc = WebViewController.load_url(url)
  n_vc = NavigationController.new(m_vc)
  present_objc(n_vc)

