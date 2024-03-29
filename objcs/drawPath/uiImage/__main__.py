import math
from pathlib import Path

from objc_util import ObjCClass, nsurl, NSData, CGRect, CGPoint, CGSize
import ui

import pdbg

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')


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


class RectangleShapeLayer:
  def __init__(self,
               bounds: CGRect,
               frame: CGRect,
               strokeColor=None,
               fillColor=None):

    self.layer = CAShapeLayer.alloc().init()
    self.layer.frame = bounds
    self.rect = UIBezierPath.bezierPathWithRect_(frame)
    #self.size = size

    # xxx: 書き方良くないけど、取り敢えず、、、
    blueColor = UIColor.blueColor().cgColor()
    cyanColor = UIColor.cyanColor().cgColor()
    self.strokeColor = strokeColor if strokeColor else blueColor
    self.fillColor = fillColor if fillColor else cyanColor
    self.setup()

  def setup(self):
    self.layer.setLineWidth_(20.0)
    self.layer.setStrokeColor_(self.strokeColor)
    self.layer.setFillColor_(self.fillColor)
    self.layer.setPath_(self.rect.CGPath())


class ViewController:
  def __init__(self, _previewView):
    self.previewView = _previewView
    self.originalImage = get_UIImage(img_file_path)

    self.imageView = UIImageView.alloc().initWithImage_(self.originalImage)
    self.overlayLayer = CAShapeLayer.alloc().init()
    self.setupOverlay()
    self.previewView.addSubview_(self.imageView)

  def setupOverlay(self):
    bounds = self.imageView.bounds()
    self.overlayLayer.frame = bounds
    self.imageView.layer().addSublayer_(self.overlayLayer)
    _width = bounds.size.width
    _height = bounds.size.height

    count = 10
    base = _width / count
    x = 0

    for _ in range(count):
      _point = CGPoint(x, 0.0)
      _size = CGSize(base, base)
      frame = CGRect(_point, _size)
      rect = RectangleShapeLayer(bounds, frame)
      self.overlayLayer.addSublayer_(rect.layer)
      x += base


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
  #img_file_path = '../../CoreML/VisionFramework/face/img/sample01.png'
  img_file_path = '../../CoreML/VisionFramework/face/img/multi-face.png'

  view = View()

