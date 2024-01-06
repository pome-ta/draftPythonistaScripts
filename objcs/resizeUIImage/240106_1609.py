from pathlib import Path

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread
from objc_util import sel, CGRect

import pdbg

UIView = ObjCClass('UIView')
UIImage = ObjCClass('UIImage')
UIImageView = ObjCClass('UIImageView')
#[UIView.ContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/contentmode)
scaleAspectFit = 1

UIColor = ObjCClass('UIColor')


class ObjcView:

  def __init__(self, *args, **kwargs):
    self.instance = UIView.alloc()
    CGRectZero = CGRect((0.0, 0.0), (0.0, 0.0))
    self.instance.initWithFrame_(CGRectZero)

  def _init(self):

    if IS_LAYOUT_DEBUG:
      color = UIColor.systemRedColor()
      self.instance.layer().setBorderWidth_(1.0)
      self.instance.layer().setBorderColor_(color.cgColor())
    self.instance.setTranslatesAutoresizingMaskIntoConstraints_(False)

    return self.instance

  @classmethod
  def new(cls, *args, **kwargs) -> ObjCInstance:
    _cls = cls(*args, **kwargs)
    return _cls._init()


class ObjcImageView(ObjcView):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.instance = UIImageView.alloc().initWithImage_(kwargs['image'])


dummy_img_uri = '/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Media/Images/test/Boat@2x.png'

dummy_img_path = Path(dummy_img_uri)
IS_LAYOUT_DEBUG = True

header_icon_img = UIImage.imageWithContentsOfFile_(str(dummy_img_path))
header_icon = ObjcImageView.new(image=header_icon_img)
header_icon.setContentMode_(scaleAspectFit)

import ui


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self.bg_color = 'maroon'
    ObjCInstance(self).addSubview_(header_icon)


if __name__ == '__main__':
  view = View()
  view.present()

