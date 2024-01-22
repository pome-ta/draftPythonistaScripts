from objc_util import ObjCClass
from .metaClasses.objcMetaView import ObjcMetaView

UIImageView = ObjCClass('UIImageView')


class ObjcImageView(ObjcMetaView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UIImageView.alloc().initWithImage_(kwargs['image'])

