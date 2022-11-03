from pathlib import Path
import ctypes

from objc_util import c, ObjCInstance, ObjCClass, NSData, nsurl, CGSize, CGRect, CGPoint, CGFloat
import ui

import pdbg

VNDetectFaceRectanglesRequest = ObjCClass('VNDetectFaceRectanglesRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')


def _get_sample_img():
  # todo: 事後取得用
  # [ios-vision/multi-face.png at master · googlesamples/ios-vision](https://github.com/googlesamples/ios-vision/blob/master/FaceDetectorDemo/FaceDetector/multi-face.png)
  pass


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


def parseCGRect(cg_rect: CGRect) -> tuple:
  _origin = cg_rect.origin
  _size = cg_rect.size
  origin_x = _origin.x
  origin_y = _origin.y
  size_width = _size.width
  size_height = _size.height
  return (origin_x, origin_y, size_width, size_height)


class RectangleShapeLayer:
  def __init__(self,
               bounds: CGRect,
               frame: CGRect,
               strokeColor=None,
               fillColor=None):

    self.layer = CAShapeLayer.alloc().init()
    self.layer.frame = bounds
    self.rect = UIBezierPath.bezierPathWithRect_(frame)

    # xxx: 書き方良くないけど、取り敢えず、、、
    greenColor = UIColor.greenColor().cgColor()
    clearColor = UIColor.clearColor().CGColor()
    self.strokeColor = strokeColor if strokeColor else greenColor
    self.fillColor = fillColor if fillColor else clearColor

    self.setup()

  def setup(self):
    self.layer.setLineWidth_(2.0)
    self.layer.setStrokeColor_(self.strokeColor)
    self.layer.setFillColor_(self.fillColor)
    self.layer.setPath_(self.rect.CGPath())


  # xxx: sample 通りではなく独自解釈
  # xxx: 無駄にクソデカClass
class ViewController:
  def __init__(self, _previewView):
    self.previewView = _previewView
    self.originalImage = get_UIImage(img_file_path)
    self.imageView = UIImageView.alloc().initWithImage_(self.originalImage)
    self.overlayLayer = CAShapeLayer.alloc().init()
    self.setupOverlay()
    self.faceDetection()

    self.previewView.addSubview_(self.imageView)

  def setupOverlay(self):
    self.overlayLayer.frame = self.imageView.bounds()
    self.imageView.layer().addSublayer_(self.overlayLayer)

  def faceDetection(self):
    cgImage = self.originalImage.CGImage()
    request = VNDetectFaceRectanglesRequest.alloc().init()
    handler = VNImageRequestHandler.alloc().initWithCGImage_options_(
      cgImage, None)

    handler.performRequests_error_([request], None)
    observation_array = request.results()
    self.drawFaceRectangle_observations_(observation_array)

  def drawFaceRectangle_observations_(self, observations):
    bounds = self.overlayLayer.frame()
    _, _, layerWidth, layerHeight = parseCGRect(bounds)

    for observation in observations:
      _x, _y, _width, _height = parseCGRect(observation.boundingBox())
      
      width = _width * layerWidth
      height = _height * layerHeight
      x = _x * layerWidth
      # todo: 左下原点から、右上原点に
      y = (layerHeight - height) - (_y * layerHeight)

      frame = CGRect(CGPoint(x, y), CGSize(width, height))
      rect = RectangleShapeLayer(bounds, frame)
      self.overlayLayer.addSublayer_(rect.layer)


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
  img_file_path = './img/multi-face.png'
  #img_file_path = './img/sample01.png'
  view = View()

