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
  def __init__(self, size: CGSize, strokeColor=None, fillColor=None):
    
    self.layer = CAShapeLayer.alloc().init()
    frame  = CGRect(CGPoint(0.0, 0.0), size)
    self.layer.frame = frame
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
    self.setCAShapeLayer()

    self.previewView.addSubview_(self.imageView)

  def setupOverlay(self):
    self.overlayLayer.frame = self.imageView.bounds()
    #pdbg.state(self.overlayLayer)
    self.imageView.layer().addSublayer_(self.overlayLayer)
    rect = RectangleShapeLayer(CGSize(100.0, 100.0))
    #pdbg.state(rect.layer)
    self.overlayLayer.addSublayer_(rect.layer)
    #self.imageView.layer().addSublayer_(rect.layer)
    self.drawPath()
    #pdbg.state(self.overlayLayer)

  def setCAShapeLayer(self):
    self.overlayLayer.setLineWidth_(20.0)
    blueColor = UIColor.blueColor().cgColor()
    cyanColor = UIColor.cyanColor().cgColor()
    self.overlayLayer.setStrokeColor_(blueColor)
    self.overlayLayer.setFillColor_(cyanColor)
    #self.imageView.layer().addSublayer_(self.overlayLayer)

  def drawPath(self):
    height = 500
    width = 500

    center = CGPoint(width / 2, height / 2)
    radius = 100.0
    startAngle = 0.125 * math.pi
    endAngle = 1.875 * math.pi

    arc = UIBezierPath.alloc().init()
    #pdbg.state(UIBezierPath)
    arc.addArcWithCenter_radius_startAngle_endAngle_clockwise_(
      center, radius, startAngle, endAngle, True)

    
    rect = RectangleShapeLayer(CGSize(100.0, 100.0))
    self.overlayLayer.setPath_(arc.CGPath())
    #self.overlayLayer.setPath_(rect.rect.CGPath())


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

