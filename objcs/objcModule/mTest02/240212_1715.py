from ctypes import c_void_p,POINTER
from objc_util import ObjCInstance, sel, create_objc_class, class_getSuperclass, class_getInstanceMethod, objc_allocateClassPair, objc_registerClassPair, objc_getClass, on_main_thread, CGRect,c,ObjCInstanceMethod,method_getTypeEncoding

from objcista import *
#from objcista._controller import _Controller
from objcista.objcNavigationController import PlainNavigationController
from objcista.objcViewController import ObjcViewController
from objcista.objcLabel import ObjcLabel

import pdbg
'''
selector = sel('initWithStyle:reuseIdentifier:')
super_function = UITableViewCell.instanceMethodForSelector_(selector)
pdbg.state(c_void_p(super_function))
'''
MTLCreateSystemDefaultDevice = c.MTLCreateSystemDefaultDevice
#print(MTLCreateSystemDefaultDevice)
#pdbg.state(MTLCreateSystemDefaultDevice)

class CstmUITableViewCell:

  def __init__(self):
    self.tableViewCell_instance: None
    self.is_fast = False

  def _override_tableViewCell(self):

    def _tvc_initWithFrame_reuseIdentifier_(_self, _cmd, _frame,
                                            _reuseIdentifier):
      # xxx: ここは呼ばれない
      this = ObjCInstance(_self)
      frame = ObjCInstance(_frame)
      reuseIdentifier = ObjCInstance(_reuseIdentifier)
      this.initWithFrame_(frame)
      this.initWithStyle_reuseIdentifier_(0, reuseIdentifier)
      print('h')
      return this

    def _tvc_initWithStyle_reuseIdentifier_(_self, _cmd, _style,
                                            _reuseIdentifier):

      style = ObjCInstance(_style)
      reuseIdentifier = ObjCInstance(_reuseIdentifier)

      #this.initWithFrame_reuseIdentifier_(frame, _reuseIdentifier)
      print('iiii')

      this = ObjCInstance(_self)
      #this.initWithStyle_reuseIdentifier_(style,reuseIdentifier)
      super().initWithStyle_reuseIdentifier_(style, reuseIdentifier)
      #this.addSubview_(ObjcLabel.new('hoge'))

      #selector = sel('initWithStyle:reuseIdentifier:')
      #super_function = UITableViewCell.instanceMethodForSelector_(selector)
      #super_function(_self, selector, _style, _reuseIdentifier)

      return _self
      #return this

    def initWithCoder_(_self, _cmd, _coder):
      print('c')
      
    def didAddSubview_(_self, _cmd, _subview):
      subview = ObjCInstance(_subview)
      if not (self.is_fast):
        this = ObjCInstance(_self)
        selector = sel('initWithStyle:reuseIdentifier:')
        #super_function = UITableViewCell.instanceMethodForSelector_(selector)
        
        #print(ObjCInstance(super_function))
        #print(bool(super_function))
        #pdbg.state(super_function)
        
        #print(subview)
        #pdbg.state(ObjCInstance(_self))
        
        #f = this.setFrame_
        #pdbg.state(f)
        #class_getSuperclass
        #print(self.tableViewCell_instance)
        #pdbg.state(self.tableViewCell_instance)
        #sc = class_getSuperclass(self.tableViewCell_instance)
        sc = ObjCInstance(class_getSuperclass(tvc))
        superclass_method = class_getInstanceMethod(sc, selector)
        enc = method_getTypeEncoding(superclass_method)
        #sm = class_getInstanceMethod(ObjCInstance(sc), selector)
        #m=ObjCInstanceMethod(ObjCInstance(sc), 'initWithStyle_reuseIdentifier_')
        print(enc)
        pdbg.state(superclass_method)
        #pdbg.state(sm)
        self.is_fast = True
      print('---')

    #_methods=[initWithStyle_reuseIdentifier_,initWithCoder_,]
    _methods = [
      #_tvc_initWithStyle_reuseIdentifier_,
      #initWithFrame_reuseIdentifier_,
      #initWithCoder_,
      didAddSubview_,
    ]
    #_methods =[initWithCoder_]
    #_methods = []
    create_kwargs = {
      'name': 'tvc',
      'superclass': UITableViewCell,
      'methods': _methods,
    }
    tvc = create_objc_class(**create_kwargs)
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
    self.cell_identifier = 'cell'
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
      #objc_registerClassPair(_self)
      #objc_registerClassPair(this)
      #sc = class_getSuperclass(this)
      #objc_getClass(_self)
      #sc=class_getInstanceMethod(_self)
      #sc=objc_allocateClassPair(_self)
      #pdbg.state(class_getSuperclass(_self))
      #CstmUITableViewCell
      #print(_self)
      #print(this.ptr)
      #pdbg.state(sc)
      #view.registerClass_forCellReuseIdentifier_(UITableViewCell, self.cell_identifier)
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

      #pdbg.state(cell.contentView().subviews().objectAtIndexedSubscript_(0))
      #pdbg.state(cell)
      #print(class_getSuperclass(cell.ptr))

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
    #UITableViewCell
    #registerClass_forCellReuseIdentifier_

    #CstmUITableViewCell
    #vc.view().registerClass_forCellReuseIdentifier_(UITableViewCell,self.cell_identifier)
    #vc.view().registerClass_forCellReuseIdentifier_(CstmUITableViewCell.this(),self.cell_identifier)

    #pdbg.state(vc.view())
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
  #vc = ButtonViewController.new()
  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)
  #ctv = CstmUITableViewCell.this()
  #sc = class_getSuperclass(ctv.ptr)
  #print(ObjCInstance(sc))

