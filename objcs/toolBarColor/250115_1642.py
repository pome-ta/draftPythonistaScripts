'''
tintedToolbarViewController
[pystaUIKitCatalogChallenge/tintedToolbarViewController.py at main · pome-ta/pystaUIKitCatalogChallenge · GitHub](https://github.com/pome-ta/pystaUIKitCatalogChallenge/blob/main/tintedToolbarViewController.py)
'''

from objc_util import (
  ObjCClass,
  ObjCInstance,
  create_objc_class,
  on_main_thread,
  sel,
  CGRect,
)

import pdbg

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

UIBarButtonItem = ObjCClass('UIBarButtonItem')


class CustomViewController:

  def __init__(self):
    self._viewController: UIViewController
    self.nav_title = 'title'
    self.sub_view = UIView.alloc()

  def setup_viewDidLoad(self, this: UIViewController):
    # xxx: `viewDidLoad` が肥大化しそうなので、レイアウト関係以外はこっちで処理

    navigationItem = this.navigationItem()
    navigationItem.setTitle_(self.nav_title)

    # --- view
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.sub_view.initWithFrame_(CGRectZero)
    self.sub_view.setBackgroundColor_(UIColor.systemRedColor())

    #pdbg.state(this.navigationController().toolbar())
    #pdbg.state(this)

    this.navigationController().setToolbarHidden_(False)
    this.navigationController().toolbar().setBarStyle_(1)
    this.navigationController().toolbar().setTranslucent_(False)
    this.navigationController().toolbar().setTintColor_(
      UIColor.systemGreenColor())
    this.navigationController().toolbar().setBackgroundColor_(
      UIColor.systemBlueColor())

    trashBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(16, None, None)
    flexibleSpaceBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(5, None, None)
    doneBarButtonItem = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(0, None, None)

    toolbarButtonItems = [
      trashBarButtonItem,
      flexibleSpaceBarButtonItem,
      doneBarButtonItem,
    ]

    this.setToolbarItems_animated_(toolbarButtonItems, True)
    #this.navigationController().setToolbarHidden_(False)
    #pdbg.all(this)

  def _override_viewController(self):

    # --- `UIViewController` Methods
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      self.setup_viewDidLoad(this)
      view = this.view()

      # --- layout
      #safeAreaLayoutGuide = view.safeAreaLayoutGuide()
      safeAreaLayoutGuide = this.navigationController().safeAreaLayoutGuide()
      toolBar = this.navigationController().toolbar()
      #pdbg.state(this.navigationController())

      #pdbg.state(toolBar)
      
      
      NSLayoutConstraint.activateConstraints_([
        toolBar.bottomAnchor().constraintEqualToAnchor_(
          safeAreaLayoutGuide.bottomAnchor()),
      ])
      
      

      view.addSubview_(self.sub_view)
      self.sub_view.translatesAutoresizingMaskIntoConstraints = False

      NSLayoutConstraint.activateConstraints_([
        self.sub_view.centerXAnchor().constraintEqualToAnchor_(
          view.centerXAnchor()),
        self.sub_view.centerYAnchor().constraintEqualToAnchor_(
          view.centerYAnchor()),
        self.sub_view.widthAnchor().constraintEqualToAnchor_multiplier_(
          view.widthAnchor(), 0.9),
        self.sub_view.heightAnchor().constraintEqualToAnchor_multiplier_(
          view.heightAnchor(), 1.05),
      ])

    def viewDidAppear_(_self, _cmd, _animated):
      #print('viewDidAppear')
      this = ObjCInstance(_self)
      view = this.view()
      #pdbg.state(this.navigationController().toolbar())

    # --- `UIViewController` set up
    _methods = [
      viewDidLoad,
      viewDidAppear_,
    ]

    create_kwargs = {
      'name': '_vc',
      'superclass': UIViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self._viewController = _vc

  #@on_main_thread
  def _init(self):
    self._override_viewController()
    vc = self._viewController.new().autorelease()
    return vc

  @classmethod
  def new(cls) -> ObjCInstance:
    _cls = cls()
    return _cls._init()


class ObjcUIViewController:

  def __init__(self):
    self._navigationController: UINavigationController

  def _override_navigationController(self):
    # --- `UINavigationController` Methods
    def closeButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

    # --- `UINavigationController` set up
    _methods = [
      closeButtonTapped_,
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
      #appearance.configureWithOpaqueBackground()
      #appearance.configureWithTransparentBackground()
      #appearance.backgroundColor = sc.systemExtraLightGrayColor

      # --- navigationBar

      navigationBar = navigationController.navigationBar()
      '''
      navigationBar.standardAppearance = appearance
      navigationBar.scrollEdgeAppearance = appearance
      navigationBar.compactAppearance = appearance
      navigationBar.compactScrollEdgeAppearance = appearance
      '''

      #navigationBar.prefersLargeTitles = True

      viewController.setEdgesForExtendedLayout_(0)
      #viewController.setExtendedLayoutIncludesOpaqueBars_(True)

      _close_btn = UIBarButtonItem.alloc()
      '''
      BarButtonSystemItem
        case  0 : done 
        case  1 : cancel 
        case  2 : edit 
        case  4 : add 
        case  5 : flexibleSpace 
        case  6 : fixedSpace 
        case  7 : compose 
        case  8 : reply 
        case  9 : action 
        case 10 : organize
        case 11 : bookmarks
        case 12 : search
        case 13 : refresh
        case 17 : stop
        case 16 : trash
        case 17 : play
        case 18 : pause
        case 19 : rewind
        case 20 : fastForward
        case 21 : undo
        case 22 : redo
        case 23 : pageCurl  # Deprecated
        case 24 : close
      '''
      close_btn = _close_btn.initWithBarButtonSystemItem_target_action_(
        24, navigationController, sel('closeButtonTapped:'))

      visibleViewController = navigationController.visibleViewController()

      # --- navigationItem
      navigationItem = visibleViewController.navigationItem()

      #navigationItem.setTitle_('nv')
      navigationItem.rightBarButtonItem = close_btn

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
  '''
  ModalPresentationStyle
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
  vc.setModalPresentationStyle(0)
  root_vc.presentViewController_animated_completion_(vc, True, None)


if __name__ == '__main__':
  cvc = CustomViewController.new()
  ovc = ObjcUIViewController.new(cvc)
  present_objc(ovc)

