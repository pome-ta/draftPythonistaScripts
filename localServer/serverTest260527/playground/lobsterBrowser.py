_TOP_DIR_NAME = 'serverTest260527'
_MODULES_DIR_NAME = 'modules'

# todo: `./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME}` にあるpackage のimport 準備
if __name__ == '__main__' and not __file__[:__file__.rfind('/')].endswith(
    _TOP_DIR_NAME):
  import pathlib
  import sys
  __parents = pathlib.Path(__file__).resolve().parents
  for __dir_path in __parents:
    if __dir_path.name == _TOP_DIR_NAME and (__modules_path := __dir_path /
                                             _MODULES_DIR_NAME).exists():
      sys.path.insert(0, str(__modules_path))
      break
  else:
    import warnings
    with warnings.catch_warnings():
      warnings.simplefilter('always', ImportWarning)
      __warning_message = f'./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME} not found in parent directories'
      warnings.warn(__warning_message, ImportWarning)

import ctypes
from pathlib import Path

from pyrubicon.objc.api import ObjCClass, ObjCProtocol
from pyrubicon.objc.api import ObjCInstance, NSObject, Block
from pyrubicon.objc.api import objc_method, objc_property
from pyrubicon.objc.runtime import send_super, objc_id, SEL

from objc_frameworks.CoreGraphics import CGRectZero
from objc_frameworks.Foundation import (
  NSStringFromClass,
  NSURLRequestCachePolicy,
  NSKeyValueObservingOptions,
)
from objc_frameworks.UIKit import (
  UIControlEvents,
  UIBarButtonItemStyle,
  NSNotificationName,
  UIScrollViewKeyboardDismissMode,
  UIMenuElementAttributes,
)

from rbedge.lifeCycle import loop
from rbedge.utils import nsurl
from rbedge import pdbr

UINavigationController = ObjCClass('UINavigationController')
UIViewController = ObjCClass('UIViewController')

WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')
WKWebsiteDataStore = ObjCClass('WKWebsiteDataStore')
WKContentView = ObjCClass('WKContentView')
NSURL = ObjCClass('NSURL')
NSURLRequest = ObjCClass('NSURLRequest')

WKNavigationDelegate = ObjCProtocol('WKNavigationDelegate')
WKUIDelegate = ObjCProtocol('WKUIDelegate')

UIRefreshControl = ObjCClass('UIRefreshControl')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UIImage = ObjCClass('UIImage')
UIMenu = ObjCClass('UIMenu')
UIAction = ObjCClass('UIAction')
UIColor = ObjCClass('UIColor')

NSNotificationCenter = ObjCClass('NSNotificationCenter')


class NavigationController(UINavigationController):

  @objc_method
  def initWithRootViewController_(self, rootViewController):
    send_super(__class__,
               self,
               'initWithRootViewController:',
               rootViewController,
               argtypes=[
                 objc_id,
               ])

    return self

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'- {NSStringFromClass(__class__)}: dealloc')
    loop.stop()

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  @objc_method
  def doneButtonTapped_(self, sender):
    self.dismissViewControllerAnimated_completion_(True, None)


class WebDelegate(
    NSObject,
    protocols=[
      WKNavigationDelegate,
      #WKUIDelegate,
    ]):

  @objc_method
  def init(self):
    send_super(__class__, self, 'init')
    return self

  # --- WKUIDelegate
  # --- WKNavigationDelegate
  @objc_method
  def webView_didCommitNavigation_(self, webView, navigation):
    # 遷移開始時
    pass

  @objc_method
  def webView_didFailNavigation_withError_(
    self,
    webView,
    navigation,
    error,
  ):  # xxx: 未確認
    # 遷移中にエラーが発生した時
    print('didFailNavigation_withError')
    print(error)

  @objc_method
  def webView_didFailProvisionalNavigation_withError_(
    self,
    webView,
    navigation,
    error,
  ):
    # ページ読み込み時にエラーが発生した時
    print('didFailProvisionalNavigation_withError')
    print(error)

  @objc_method
  def webView_didFinishNavigation_(self, webView, navigation):
    # ページ読み込みが完了した時

    pass

  @objc_method
  def webView_didReceiveServerRedirectForProvisionalNavigation_(
    self,
    webView,
    navigation,
  ):  # xxx: 未確認
    # リダイレクトされた時
    print('didReceiveServerRedirectForProvisionalNavigation')

  @objc_method
  def webView_didStartProvisionalNavigation_(self, webView, navigation):
    # ページ読み込みが開始された時
    pass


class WebViewController(UIViewController):

  locationResource: Path | str = objc_property(object)

  webView: WKWebView = objc_property()
  webDelegate: WebDelegate = objc_property()

  isKeyboardVisible: bool = objc_property(object)

  showKeyboardRightBarButtonItems: list = objc_property(object)
  hideKeyboardRightBarButtonItems: list = objc_property(object)
  leftBarButtonItems: list = objc_property(object)

  titleIdentifier: str = objc_property(object)

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'- {NSStringFromClass(__class__)}: dealloc')
    pass

  @objc_method
  def initWithLocationResource_(self, locationResource: object):
    send_super(__class__, self, 'init')

    if not (locationResource.exists()):
      raise FileNotFoundError(f'{indexPath}')

    self.locationResource = locationResource
    self.titleIdentifier = 'title'
    return self

  @objc_method
  def makeWeblView(self) -> ObjCInstance:
    websiteDataStore = WKWebsiteDataStore.nonPersistentDataStore()
    webConfiguration = WKWebViewConfiguration.new()
    webConfiguration.websiteDataStore = websiteDataStore
    webConfiguration.preferences.setValue_forKey_(
      True, 'allowFileAccessFromFileURLs')

    webView = WKWebView.alloc().initWithFrame_configuration_(
      CGRectZero, webConfiguration)

    webView.scrollView.bounces = True
    webView.scrollView.keyboardDismissMode = UIScrollViewKeyboardDismissMode.interactive

    refreshControl = UIRefreshControl.new()
    refreshControl.addTarget_action_forControlEvents_(
      self, SEL('refreshWebView:'), UIControlEvents.valueChanged)
    webView.scrollView.refreshControl = refreshControl

    # todo: (.js 操作等での) `title` 変化を監視
    webView.addObserver_forKeyPath_options_context_(
      self, self.titleIdentifier, NSKeyValueObservingOptions.new, None)

    return webView

  @objc_method
  def setupBarButtonItems(self):

    closeButtonItem = UIBarButtonItem.alloc().initWithImage(
      UIImage.systemImageNamed_('xmark'),
      style=UIBarButtonItemStyle.plain,
      target=self.navigationController,
      action=SEL('doneButtonTapped:'),
    )

    refreshButtonItem = UIBarButtonItem.alloc().initWithImage(
      UIImage.systemImageNamed_('arrow.clockwise.circle'),
      style=UIBarButtonItemStyle.plain,
      target=self,
      action=SEL('reLoadWebView:'),
    )

    checkmarkButtonItem = UIBarButtonItem.alloc().initWithImage(
      UIImage.systemImageNamed_('checkmark'),
      style=UIBarButtonItemStyle.plain,
      target=self,
      action=SEL('webViewResignFirstResponder'),
    )
    checkmarkButtonItem.tintColor = UIColor.tintColor()
    checkmarkButtonItem.style = UIBarButtonItemStyle.prominent

    superReloadAction = UIAction.actionWithTitle(
      'superReload',
      image=UIImage.systemImageNamed_('arrow.trianglehead.clockwise'),
      identifier=None,
      handler=Block(self.reloadFromOrigin_, None, ctypes.c_void_p),
    )

    buttonMenu = UIMenu.menuWithChildren_([
      superReloadAction,
    ])

    ellipsisButtonItem = UIBarButtonItem.alloc().initWithImage(
      UIImage.systemImageNamed_('ellipsis'),
      menu=buttonMenu,
    )

    flexibleSpaceItem = UIBarButtonItem.flexibleSpaceItem()
    fixedSpaceItem = UIBarButtonItem.fixedSpaceItem()

    self.showKeyboardRightBarButtonItems = [
      checkmarkButtonItem,
      flexibleSpaceItem,
      closeButtonItem,
    ]

    self.hideKeyboardRightBarButtonItems = [
      closeButtonItem,
    ]

    self.leftBarButtonItems = [
      refreshButtonItem,
      ellipsisButtonItem,
    ]

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')

    webDelegate = WebDelegate.new()
    webView = self.makeWeblView()

    webView.navigationDelegate = webDelegate
    #webView.scrollView.delegate = webDelegate
    #webView.uiDelegate = webDelegate  # xxx: ?

    self.webView = webView
    self.webDelegate = webDelegate
    self.isKeyboardVisible = False

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    #self.navigationItem.title = NSStringFromClass(__class__)
    self.navigationItem.subtitle = NSStringFromClass(__class__)
    #self.navigationItem.prompt = NSStringFromClass(__class__)

    # --- load
    _fileURLWithPath = NSURL.fileURLWithPath_isDirectory_
    _path = str(self.locationResource)

    tmp1 = nsurl(_path)
    tmp2 = nsurl(
      'https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/textarea'
    )

    #print(tmp1)
    #print(tmp2)
    pdbr.state(tmp1)
    print(tmp1.isFileURL())

    _parent = str(self.locationResource.parent)
    loadFileURL = _fileURLWithPath(_path, False)
    allowingReadAccessToURL = _fileURLWithPath(_parent, True)
    #print(loadFileURL)

    request = NSURLRequest.requestWithURL_(loadFileURL)

    self.webView.loadFileRequest(
      request, allowingReadAccessToURL=allowingReadAccessToURL)
    '''
    self.webView.loadFileURL(
      loadFileURL,
      allowingReadAccessToURL=allowingReadAccessToURL,
    )
    '''

    self.view.backgroundColor = UIColor.systemBackgroundColor()

    self.setupBarButtonItems()
    self.setupLayoutConstraint()

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

    self.navigationItem.setLeftBarButtonItems_animated_(
      self.leftBarButtonItems, animated)
    self.navigationItem.setRightBarButtonItems_animated_(
      self.hideKeyboardRightBarButtonItems, animated)

    notificationCenter = NSNotificationCenter.defaultCenter
    notificationCenter.addObserver_selector_name_object_(
      self, SEL('keyboardWillShow:'),
      NSNotificationName.keyboardWillShowNotification, None)
    notificationCenter.addObserver_selector_name_object_(
      self, SEL('keyboardWillHide:'),
      NSNotificationName.keyboardWillHideNotification, None)

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    self.webView.removeObserver_forKeyPath_(self, self.titleIdentifier)
    self.webView.reloadFromOrigin()

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    notificationCenter = NSNotificationCenter.defaultCenter

    notificationCenter.removeObserver_name_object_(
      self, NSNotificationName.keyboardWillShowNotification, None)
    notificationCenter.removeObserver_name_object_(
      self, NSNotificationName.keyboardWillHideNotification, None)

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'	{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  @objc_method
  def observeValueForKeyPath_ofObject_change_context_(
    self,
    keyPath,
    obj,
    change,
    context,
  ):

    if (webView := obj) is not None and keyPath.isEqualToString_(
        self.titleIdentifier):
      self.navigationItem.title = webView.title

  # --- private
  # --- keyboard
  @objc_method
  def keyboardWillShow_(self, notification):
    self.removeWebViewInputAccessoryView()
    if not self.isKeyboardVisible:
      self.navigationItem.setRightBarButtonItems_animated_(
        self.showKeyboardRightBarButtonItems, True)
      self.isKeyboardVisible = True

  @objc_method
  def keyboardWillHide_(self, notification):
    if self.isKeyboardVisible:
      self.navigationItem.setRightBarButtonItems_animated_(
        self.hideKeyboardRightBarButtonItems, True)
      self.isKeyboardVisible = False

  # --- buttons action
  @objc_method
  def webViewResignFirstResponder(self):
    js = 'document.activeElement?.blur();'
    self.webView.evaluateJavaScript_completionHandler_(js, None)

  @objc_method
  def reLoadWebView_(self, sender):
    self.webView.reload()

  @objc_method
  def refreshWebView_(self, sender):
    self.reLoadWebView_(sender)
    sender.endRefreshing()

  @objc_method
  def reloadFromOrigin_(self, _action: ctypes.c_void_p) -> None:
    self.webView.reloadFromOrigin()

  @objc_method
  def removeWebViewInputAccessoryView(self):
    # ref: [Objective-Cの黒魔術がよくわからなかったので覗いてみた👻 #Swift - Qiita](https://qiita.com/mopiemon/items/8d0dd7d678c4dadeadd4)
    #candidateView
    for subview in self.webView.scrollView.subviews():
      if subview.isMemberOfClass_(WKContentView) and (
          inputAccessoryView := subview.inputAccessoryView) is not None:
        inputAccessoryView.removeFromSuperview()

  # --- layout
  @objc_method
  def setupLayoutConstraint(self):
    NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

    self.view.addSubview_(self.webView)

    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    #safeAreaLayoutGuide = self.view

    self.webView.translatesAutoresizingMaskIntoConstraints = False

    centerXAnchor = self.webView.centerXAnchor.constraintEqualToAnchor_(
      safeAreaLayoutGuide.centerXAnchor)
    centerYAnchor = self.webView.centerYAnchor.constraintEqualToAnchor_(
      safeAreaLayoutGuide.centerYAnchor)

    widthAnchor = self.webView.widthAnchor.constraintEqualToAnchor_multiplier_(
      safeAreaLayoutGuide.widthAnchor,
      1.0,
    )
    heightAnchor = self.webView.heightAnchor.constraintEqualToAnchor_multiplier_(
      safeAreaLayoutGuide.heightAnchor,
      1.0,
    )

    NSLayoutConstraint.activateConstraints_([
      centerXAnchor,
      centerYAnchor,
      widthAnchor,
      heightAnchor,
    ])


if __name__ == '__main__':
  from rbedge.app import App
  from objc_frameworks.UIKit import UIModalPresentationStyle

  ROOT_PATH = Path(__file__).parents[0]

  index_path = ROOT_PATH / '../docs/index.html'

  main_vc = WebViewController.alloc().initWithLocationResource_(index_path)

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present(NavigationController)


