import math

from objc_util import ObjCClass, CGRect, CGPoint
import ui

import pdbg

# xxx: Vision framework のload は不要？
VNDetectHumanHandPoseRequest = ObjCClass('VNDetectHumanHandPoseRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')
'''
frame = CGRect((0, 0), (100, 100))
flex_w, flex_h = (1 << 1), (1 << 4)
'''


class CameraView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.flex = 'WH'
    self.bg_color = 'green'

    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().init()
    #self.previewLayer.setFrame_(frame)
    #pdbg.state(self._overlayLayer)

    # [Swift, Objective-C を Xamarin.iOS に移植する際のポイント（2）　UIView.Layerの差し替え - 個人的なメモ](https://hiro128.hatenablog.jp/entry/2017/09/30/234916)
    self.objc_instance.layer().addSublayer_(self.previewLayer)

    self._overlayLayer = CAShapeLayer.alloc().init()
    self.setCAShapeLayer()

  def layout(self):
    self.previewLayer.frame = self.objc_instance.bounds()

    self._overlayLayer.frame = self.previewLayer.bounds()
    
    self.showPoints(self._overlayLayer.frame().size)

  def showPoints(self, size):
    height = size.height
    width = size.width

    center = CGPoint(width / 2, height / 2)
    radius = 100.0
    startAngle = 0.125 * math.pi
    endAngle = 1.875 * math.pi

    arc = UIBezierPath.alloc().init()
    arc.addArcWithCenter_radius_startAngle_endAngle_clockwise_(
      center, radius, startAngle, endAngle, True)

    #pdbg.state(arc.CGPath())
    self._overlayLayer.setPath_(arc.CGPath())

  def setCAShapeLayer(self):
    self._overlayLayer.setLineWidth_(20.0)
    blueColor = UIColor.blueColor().cgColor()
    cyanColor = UIColor.cyanColor().cgColor()
    self._overlayLayer.setStrokeColor_(blueColor)
    self._overlayLayer.setFillColor_(cyanColor)
    self.previewLayer.addSublayer_(self._overlayLayer)


class CameraViewController:
  def __init__(self):
    self._cameraFeedSession = None

  def viewDidAppear(self):
    pass


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    cm = CameraView()
    self.add_subview(cm)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

