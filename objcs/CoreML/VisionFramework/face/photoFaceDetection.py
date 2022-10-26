from pathlib import Path
import ctypes

from objc_util import c, ObjCInstance, ObjCClass, NSData, nsurl, CGSize, CGRect, CGPoint, CGFloat
import ui

import pdbg

VNDetectFaceRectanglesRequest = ObjCClass('VNDetectFaceRectanglesRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')

UIImageView = ObjCClass('UIImageView')
UIImage = ObjCClass('UIImage')

#UIColor = ObjCClass('UIColor')

UIGraphicsBeginImageContextWithOptions = c.UIGraphicsBeginImageContextWithOptions

UIGraphicsBeginImageContextWithOptions.argtypes = [
  CGSize, ctypes.c_bool, CGFloat
]
UIGraphicsBeginImageContextWithOptions.restype = None

UIGraphicsEndImageContext = c.UIGraphicsBeginImageContext
UIGraphicsEndImageContext.argtypes = []
UIGraphicsEndImageContext.restype = None

UIGraphicsGetCurrentContext = c.UIGraphicsGetCurrentContext
UIGraphicsGetCurrentContext.argtypes = []
UIGraphicsGetCurrentContext.restype = ctypes.c_void_p

UIGraphicsGetImageFromCurrentImageContext = c.UIGraphicsGetImageFromCurrentImageContext
UIGraphicsGetImageFromCurrentImageContext.argtypes = []
UIGraphicsGetImageFromCurrentImageContext.restype = ctypes.c_void_p

CGContextSetLineWidth = c.CGContextSetLineWidth
CGContextSetLineWidth.argtypes = [ctypes.c_void_p, CGFloat]
CGContextSetLineWidth.restype = None

CGContextSetRGBStrokeColor = c.CGContextSetRGBStrokeColor
CGContextSetRGBStrokeColor.argtypes = [
  ctypes.c_void_p, CGFloat, CGFloat, CGFloat, CGFloat
]
CGContextSetRGBStrokeColor.restype = None

CGContextStrokeRect = c.CGContextStrokeRect
CGContextStrokeRect.argtypes = [ctypes.c_void_p, CGRect]
CGContextStrokeRect.restype = None


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


# xxx: sample 通りではなく独自解釈
class ViewController:
  def __init__(self, _previewView):
    self.previewView = _previewView
    self.originalImage = get_UIImage(img_file_path)
    self.imageView = None
    self.faceDetection()

    self.previewView.addSubview_(self.imageView)

  def faceDetection(self):
    cgImage = self.originalImage.CGImage()
    request = VNDetectFaceRectanglesRequest.alloc().init()
    handler = VNImageRequestHandler.alloc().initWithCGImage_options_(
      cgImage, None)

    handler.performRequests_error_([request], None)

    observation = request.results()

    image = self.drawFaceRectangle_image_observation_(self.originalImage,
                                                      observation)
    #self.imageView = UIImageView.alloc().initWithImage_(self.originalImage)
    self.imageView = UIImageView.alloc().initWithImage_(image)

    #pdbg.state(observation)
    #print(observation)
    #pdbg.state(ObjCInstance(image))

  def drawFaceRectangle_image_observation_(self, image,
                                           observation) -> UIImage:
    _height = image.size().height
    _width = image.size().width
    #imageSize = [_width, _height]  # xxx: 順番合ってる？
    imageSize = image.size()
    #pdbg.state(imageSize)
    UIGraphicsBeginImageContextWithOptions(imageSize, False, 0.0)
    context = UIGraphicsGetCurrentContext()
    image.drawInRect_(CGRect(CGPoint(0.0), imageSize))
    CGContextSetLineWidth(context, 4.0)
    CGContextSetRGBStrokeColor(
      context, 0.0, 0.5, 1.0, 1.0)
    #pdbg.state(observation)
    for ob in observation:
      CGContextStrokeRect(context, ob.boundingBox())
      
    drawnImage = UIGraphicsGetImageFromCurrentImageContext()
    #pdbg.state(image)
    #pdbg.state(ObjCInstance(context).init())
    #pdbg.state(ObjCInstance(context))
    UIGraphicsEndImageContext()
    return ObjCInstance(drawnImage)


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
  #faceDetection(img_file_path)
  view = View()

