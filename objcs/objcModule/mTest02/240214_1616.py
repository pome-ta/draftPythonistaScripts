import ctypes
from objc_util import ObjCInstance, create_objc_class, sel, CGRect, c,class_getSuperclass

from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

import pdbg

#objc_msgSendSuper = c.objc_msgSendSuper
#objc_msgSendSuper = c['objc_msgSendSuper']
#pdbg.state(objc_msgSendSuper)


class objc_super(ctypes.Structure):
  _fields_ = [
    ('receiver', ctypes.c_void_p),
    ('super_class', ctypes.c_void_p),
  ]


class CstmUITableViewCell:

  def __init__(self):
    self.tableViewCell_instance: None
    self.is_fast = False

  def _override_tableViewCell(self):

    def initWithStyle_reuseIdentifier_(_self, _cmd, _style, _reuseIdentifier):
      #pdbg.state(ctypes.c_void_p(_cmd))
      this = ObjCInstance(_self)
      style = ObjCInstance(_style)
      reuseIdentifier = ObjCInstance(_reuseIdentifier)

      selector = sel('initWithStyle:reuseIdentifier:')
      '''
      objc_msgSendSuper = c.objc_msgSendSuper
      objc_msgSendSuper.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
      ]
      objc_msgSendSuper.restype = ctypes.c_void_p
      #cell = objc_msgSendSuper(this.ptr, selector, _self, _cmd, style,reuseIdentifier)
      '''

      #selector = sel('contentView')
      '''
      objc_msgSendSuper = c.objc_msgSendSuper
      objc_msgSendSuper.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
      ]
      objc_msgSendSuper.restype = ctypes.c_void_p
      '''
      '''
      objc_msgSend = c.objc_msgSend
      objc_msgSend.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
      ]
      objc_msgSend.restype = ctypes.c_void_p
      '''
      objc_msgSendSuper = c.objc_msgSendSuper
      objc_msgSendSuper.argtypes = [
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_void_p,
      ]
      objc_msgSendSuper.restype = ctypes.c_void_p

      #objc_msgSend
      #a = objc_msgSendSuper(_self, selector, _style, _reuseIdentifier)
      #print(a)
      #pdbg.state((a))
      #a = class_getSuperclass(_self)
      super_cls = class_getSuperclass(self.tableViewCell_instance)
      super_struct = objc_super(_self, super_cls)
      
      a = objc_msgSendSuper(ctypes.byref(super_struct), selector, _style, _reuseIdentifier)
      #print(ObjCInstance(a))

      #pdbg.state(this.isOpaque())
      #pdbg.state(this.contentView())

      super_instance = UITableViewCell.alloc().initWithStyle_reuseIdentifier_(
        style, reuseIdentifier)

      #return super_instance.ptr
      return a

    def initWithCoder_(_self, _cmd, _coder):
      print('initWithCoder')

    def didAddSubview_(_self, _cmd, _subview):
      subview = ObjCInstance(_subview)
      if not (self.is_fast):
        this = ObjCInstance(_self)
        #pdbg.state(this.reuseIdentifier())
        #pdbg.state(this.contentView())
        pdbg.state(this)

        self.is_fast = True
      print('---')

    _methods = [
      initWithStyle_reuseIdentifier_,
      didAddSubview_,
    ]
    #_methods = []
    create_kwargs = {
      'name': 'tvc',
      'superclass': UITableViewCell,
      'methods': _methods,
    }
    tvc = create_objc_class(**create_kwargs)
    #pdbg.state(tvc)
    self.tableViewCell_instance = tvc

  @on_main_thread
  def _init_tableViewCell(self):
    self._override_tableViewCell()
    return self.tableViewCell_instance

  @classmethod
  def this(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_tableViewCell()


#pdbg.state(CstmUITableViewCell.this())
# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['def'] = []  # xxx: 型名ちゃんとやる
    self.cell_identifier = 'customCell'
    #self.cell_identifier = None
    self.controller_instance: ObjCInstance

  def override(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.add_msg`
    pass

  def add_msg(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['def'] = []
    self._msgs.append(msg)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    # if self._msgs: _methods.extend(self._msgs)

    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)
      view = this.view()
      view.registerClass_forCellReuseIdentifier_(CstmUITableViewCell.this(),
                                                 self.cell_identifier)

    # todo: UITableViewDelegate
    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):

      return 1

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)
      cell = tableView.dequeueReusableCellWithIdentifier(
        self.cell_identifier, forIndexPath=indexPath)
      return cell.ptr

    _methods = [
      viewDidLoad,
      tableView_numberOfRowsInSection_,
      tableView_cellForRowAtIndexPath_,
    ]
    #_methods=[]
    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


class TopNavigationController(PlainNavigationController):

  def __init__(self):
    self.override()

  def override(self):

    @self.add_msg
    def doneButtonTapped_(_self, _cmd, _sender):
      this = ObjCInstance(_self)
      visibleViewController = this.visibleViewController()
      visibleViewController.dismissViewControllerAnimated_completion_(
        True, None)

  def willShowViewController(self,
                             navigationController: UINavigationController,
                             viewController: UIViewController, animated: bool):

    super().willShowViewController(navigationController, viewController,
                                   animated)

    systemItem = UIBarButtonItem_SystemItem.done
    done_btn = UIBarButtonItem.alloc(
    ).initWithBarButtonSystemItem_target_action_(systemItem,
                                                 navigationController,
                                                 sel('doneButtonTapped:'))

    visibleViewController = navigationController.visibleViewController()

    # --- navigationItem
    navigationItem = visibleViewController.navigationItem()
    navigationItem.rightBarButtonItem = done_btn


if __name__ == "__main__":
  LAYOUT_DEBUG = True
  #LAYOUT_DEBUG = False
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

