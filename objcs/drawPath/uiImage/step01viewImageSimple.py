# ディレクトリから、画像を持ち出し表示
# サイズとか気にせずにやる
from pathlib import Path

from objc_util import ObjCClass, nsurl, NSData
import ui

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')


def get_image_absolutepath(path):
  _img_path = Path(path)
  if (_img_path.exists()):
    return str(_img_path.absolute())
  else:
    print('画像が見つかりません')
    raise


def get_UIImage(path: str) -> UIImage:
  _nsurl = nsurl(get_image_absolutepath(path))
  _data = NSData.dataWithContentsOfURL_(_nsurl)
  _uiImage = UIImage.alloc().initWithData_(_data)
  return _uiImage


class ViewController:
  def __init__(self, _previewView):
    self.previewView = _previewView
    self.originalImage = get_UIImage(img_file_path)
    self.imageView = None
    self.imageView = UIImageView.alloc().initWithImage_(self.originalImage)
    self.previewView.addSubview_(self.imageView)


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    # xxx: 先に呼ぶ？
    self.present(style='fullscreen', orientations=['portrait'])
    self.view_controller = ViewController(self.objc_instance)

  def will_close(self):
    pass


if __name__ == '__main__':
  img_file_path = '../../CoreML/VisionFramework/face/img/sample01.png'
  view = View()

