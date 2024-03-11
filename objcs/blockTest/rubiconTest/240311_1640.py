from enum import Enum

import ctypes

from objc_util import ObjCInstance, sel, create_objc_class, ns, ObjCBlock

from objcista import *

from caseElement import CaseElement
from storyboard_MenuButtonViewController import prototypes
from pyLocalizedString import pylocalizedString

import pdbg

_BLOCK_HAS_COPY_DISPOSE = 1 << 25
_BLOCK_HAS_CTOR = 1 << 26
_BLOCK_IS_GLOBAL = 1 << 28
_BLOCK_HAS_STRET = 1 << 29
_BLOCK_HAS_SIGNATURE = 1 << 30


class _BlockDescriptor(ctypes.Structure):
  _fields_ = [
    ('reserved', ctypes.c_ulong),
    ('size', ctypes.c_ulong),
    ('copy_helper', ctypes.c_void_p),  # flags & (1<<25)
    ('dispose_helper', ctypes.c_void_p),  # flags & (1<<25)
    ('signature', ctypes.c_char_p),
  ]  # flags & (1<<30)


class _Block(ctypes.Structure):
  _fields_ = [
    ('isa', ctypes.c_void_p),
    ('flags', ctypes.c_int),
    ('reserved', ctypes.c_int),
    ('invoke', ctypes.c_void_p),
    ('descriptor', _BlockDescriptor),
  ]


class ObjCBlockPointer():

  def __init__(self, block_ptr, restype=None, argtypes=None):
    self._block_ptr = block_ptr
    self._block = ctypes.cast(self._block_ptr, ctypes.POINTER(_Block))

    if not argtypes:
      argtypes = []

    if self._regular_calling_convention():
      # First arg is pointer to block, hide it from user
      argtypes.insert(0, ctypes.c_void_p)

    if self._has_signature():
      # TODO - Validate restype & argtypes against signature
      #      - Signature is not always populated
      pass

    self._func = None

    if self._regular_calling_convention():
      IMPTYPE = ctypes.CFUNCTYPE(restype, *argtypes)
      self._func = IMPTYPE(self._block.contents.invoke)

    if not self._func:
      raise Exception('Not implemented calling convention')

  def _flags(self):
    return self._block.contents.flags

  def _has_signature(self):
    has_signature = {
      (0 << 29): False,
      (1 << 29): False,
      (2 << 29): True,
      (3 << 29): True
    }

    return has_signature.get(self._flags() & (3 << 29), False)

  def _signature(self):
    if not self._has_signature():
      return None

    flags = self._flags()

    if flags & _BLOCK_HAS_COPY_DISPOSE:
      signature = self._block.contents.descriptor.signature
    else:
      signature = self._block.contents.descriptor.copy_helper

    return signature

  def _regular_calling_convention(self):
    flags = self._flags() & (3 << 29)
    return flags == (2 << 29)

  def _stret_calling_convention(self):
    flags = self._flags() & (3 << 29)
    return flags == (3 << 29)

  def __call__(self, *args):
    if self._regular_calling_convention():
      # First arg is pointer to block, hide it from user
      return self._func(self._block_ptr, *args)

    raise Exception('Not implemented calling convention')


class MenuButtonKind(Enum):
  buttonMenuProgrammatic = 'buttonMenuProgrammatic'
  buttonMenuMultiAction = 'buttonMenuMultiAction'
  buttonSubMenu = 'buttonSubMenu'
  buttonMenuSelection = 'buttonMenuSelection'


# todo: まずはここで作りつつ、モジュール化するケアも考慮
#UITableViewController
class ObjcTableViewController:

  def __init__(self, *args, **kwargs):
    self._msgs: list['Callable'] = []  # xxx: 型名ちゃんとやる
    self.controller_instance: ObjCInstance
    self.prototypes = prototypes
    self.testCells = []

  def set_prototypes(self, view: UITableView):
    for proto in self.prototypes:
      cellClass = proto.this()
      identifier = proto.reuseIdentifier_name()
      view.registerClass_forCellReuseIdentifier_(cellClass, identifier)

  def _override_controller(self):
    # todo: 既存method と独自追加method をシュッと持ちたい
    def viewDidLoad(_self, _cmd):
      this = ObjCInstance(_self)

      _view = this.view()
      style = UITableViewStyle.grouped

      view = _view.initWithFrame_style_(_view.frame(), style)
      this.setView_(view)
      self.set_prototypes(view)

      self.testCells.extend([
        # 0
        CaseElement(pylocalizedString('DropDownProgTitle'),
                    MenuButtonKind.buttonMenuProgrammatic.value,
                    this.configureDropDownProgrammaticButton_),
      ])

    # --- UITableViewDelegate

    # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
    '''
    def centeredHeaderView_(_self, _cmd, _title):
      title = ObjCInstance(_title)
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)
      return headerView.ptr
    '''

    # MARK: - UITableViewDataSource
    def tableView_viewForHeaderInSection_(_self, _cmd, _tableView, _section):
      title = self.testCells[_section].title
      alignment = UIListContentTextAlignment.center

      headerView = UITableViewHeaderFooterView.new()
      content = UIListContentConfiguration.groupedHeaderConfiguration()
      content.setText_(title)
      content.textProperties().setAlignment_(alignment)
      headerView.setContentConfiguration_(content)

      # xxx: `return` ができないので、`tableView_viewForHeaderInSection_` で処理
      #return ObjCInstance(_self).centeredHeaderView_(self.testCells[_section].title)

      return headerView.ptr

    def tableView_titleForHeaderInSection_(_self, _cmd, _tableView, _section):
      return ns(self.testCells[_section].title).ptr

    def tableView_numberOfRowsInSection_(_self, _cmd, _tableView, _section):
      return 1

    def numberOfSectionsInTableView_(_self, _cmd, _tableView):
      return len(self.testCells)

    def tableView_cellForRowAtIndexPath_(_self, _cmd, _tableView, _indexPath):
      tableView = ObjCInstance(_tableView)
      indexPath = ObjCInstance(_indexPath)

      cellTest = self.testCells[indexPath.section()]

      cell = tableView.dequeueReusableCellWithIdentifier(
        cellTest.cellID, forIndexPath=indexPath)

      if (view := cellTest.targetView(cell)):
        cellTest.configHandler(view)
      return cell.ptr

    _methods = [
      viewDidLoad,
      #centeredHeaderView_,
      tableView_viewForHeaderInSection_,
      tableView_titleForHeaderInSection_,
      tableView_numberOfRowsInSection_,
      numberOfSectionsInTableView_,
      tableView_cellForRowAtIndexPath_,
    ]

    self.add_extensions()
    if self._msgs: _methods.extend(self._msgs)

    create_kwargs = {
      'name': '_vc',
      'superclass': UITableViewController,
      'methods': _methods,
    }
    _vc = create_objc_class(**create_kwargs)
    self.controller_instance = _vc

  def add_extensions(self):
    # todo: objc で独自にmethod 生やしたいときなど
    # todo: この関数内に関数を作り`@self.extension`

    #@self.extension
    def menuHandler_(_cmd, _action):
      action = ObjCInstance(_action)

    # MARK: - Drop Down Menu Buttons
    @self.extension
    def configureDropDownProgrammaticButton_(_self, _cmd, _button):
      this = ObjCInstance(_self)
      button = ObjCInstance(_button)
      #menu = UIMenu.menuWithChildren_([])
      #actionWithTitle_image_identifier_handler_
      #action=UIAction.actionWithTitle_image_identifier_handler_(pylocalizedString('ItemTitle'), None, ns('item').ptr, this.menuHandler_)
      #button.setMenu_
      #menuWithChildren_
      #pdbg.state(UIMenu)
      #item1
      '''
      def menuHandlerr_(_cmd, _action):
        action = ObjCInstance(_action)
      #pdbg.state(menuHandler_)
      '''
      #_handler = ObjCBlock(this.menuHandler_, restype=None, argtypes=[ctypes.c_void_p, ctypes.c_void_p])
      #pdbg.state(_handler)
      #print(ctypes.POINTER(_handler))
      #handler = _handler

      #pdbg.state(h_b.block)
      print(menuHandler_)
      bp = ObjCBlockPointer(menuHandler_,
                            restype=None,
                            argtypes=[ctypes.c_void_p, ctypes.c_void_p])
      #handler = this.menuHandler_

      #pdbg.state(handler)
      handler = None
      action = UIAction.actionWithTitle_image_identifier_handler_(
        pylocalizedString('ItemTitle'), None, 'item', None)
      #pdbg.state(action.handler())
      '''
      action = UIAction.new()
      action.setTitle_(pylocalizedString('ItemTitle'))
      action.setHandler_(
        ObjCBlock(menuHandler_,
                  argtypes=[
                    ctypes.c_void_p,
                    ctypes.c_void_p,
                    ctypes.c_void_p,
                  ]))
      '''
      menu = UIMenu.menuWithChildren_([action])
      #pdbg.state(action.setHandler_)
      #pdbg.state(menu)
      #pdbg.state(button)
      #pdbg.state(this.tableView_cellForRowAtIndexPath_)
      button.setMenu_(menu)
      button.setShowsMenuAsPrimaryAction_(True)

  def extension(self, msg):
    if not (hasattr(self, '_msgs')):
      self._msgs: list['Callable'] = []
    self._msgs.append(msg)

  def _init_controller(self):
    self._override_controller()
    vc = self.controller_instance.new().autorelease()
    return vc

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init_controller()


if __name__ == "__main__":
  from objcista.objcNavigationController import PlainNavigationController

  class TopNavigationController(PlainNavigationController):

    def __init__(self):
      self.add_extensions()

    def add_extensions(self):

      @self.extension
      def doneButtonTapped_(_self, _cmd, _sender):
        this = ObjCInstance(_self)
        visibleViewController = this.visibleViewController()
        visibleViewController.dismissViewControllerAnimated_completion_(
          True, None)

    def willShowViewController(self,
                               navigationController: UINavigationController,
                               viewController: UIViewController,
                               animated: bool):

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

  vc = ObjcTableViewController.new()
  nv = TopNavigationController.new(vc, True)
  style = UIModalPresentationStyle.pageSheet
  #style = UIModalPresentationStyle.fullScreen

  run_controller(nv, style)

