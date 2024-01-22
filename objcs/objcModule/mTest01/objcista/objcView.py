from objc_util import ObjCClass
from .metaClasses.objcMetaView import ObjcMetaView

UIView = ObjCClass('UIView')


class ObjcView(ObjcMetaView):

  def __init__(self, *args, **kwargs):

    super().__init__(*args, **kwargs)
    self.instance = UIView.alloc()
    self.instance.initWithFrame_(self.CGRectZero)

