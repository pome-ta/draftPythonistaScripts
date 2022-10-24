from pathlib import Path

from objc_util import ObjCClass, NSData, nsurl

import pdbg

VNDetectFaceRectanglesRequest = ObjCClass('VNDetectFaceRectanglesRequest')

UIImage = ObjCClass('UIImage')


# todo: 事前取得
# [ios-vision/multi-face.png at master · googlesamples/ios-vision](https://github.com/googlesamples/ios-vision/blob/master/FaceDetectorDemo/FaceDetector/multi-face.png)
def get_image_absolutepath(path):
  _img_path = Path(path)
  if (_img_path.exists()):
    return str(_img_path.absolute())
  else:
    print('画像が見つかりません')
    raise


def faceDetection():
  request = VNDetectFaceRectanglesRequest.alloc().init()  


if __name__ == '__main__':
  img_file_path = './img/multi-face.png'
  img_nsurl = nsurl(get_image_absolutepath(img_file_path))
  img_data = NSData.dataWithContentsOfURL_(img_nsurl)
  originalImage = UIImage.alloc().initWithData_(img_data)

