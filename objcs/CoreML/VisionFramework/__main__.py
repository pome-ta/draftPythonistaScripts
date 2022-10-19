import math

from objc_util import create_objc_class, ObjCClass, CGRect, CGPoint, ns
import ui

import pdbg

# xxx: Vision framework のload は不要？
VNDetectHumanHandPoseRequest = ObjCClass('VNDetectHumanHandPoseRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')


def captureOutput_didOutputSampleBuffer_fromConnection_(
    _self, _cmd, _output, _sample_buffer, _conn):
  global processed_frames
  # サンプルバッファを読み込む
  _imageBuffer = CMSampleBufferGetImageBuffer(_sample_buffer)
  # サンプルバッファをロック
  CVPixelBufferLockBaseAddress(_imageBuffer, 0)
  # サンプルバッファを使った処理
  processPixelBuffer(_imageBuffer)
  # サンプルバッファをアンロック
  CVPixelBufferUnlockBaseAddress(_imageBuffer, 0)
  processed_frames = processed_frames + 1


sampleBufferDelegate = create_objc_class(
  'sampleBufferDelegate',
  methods=[captureOutput_didOutputSampleBuffer_fromConnection_],
  protocols=['AVCaptureVideoDataOutputSampleBufferDelegate'])


class CameraView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.flex = 'WH'
    self.bg_color = 'green'

    self.init()
    self.setupOverlay()
    self.setCAShapeLayer()

  def init(self):
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().init()
    self._overlayLayer = CAShapeLayer.alloc().init()

  def setupOverlay(self):
    # [Swift, Objective-C を Xamarin.iOS に移植する際のポイント（2）　UIView.Layerの差し替え - 個人的なメモ](https://hiro128.hatenablog.jp/entry/2017/09/30/234916)
    self.objc_instance.layer().addSublayer_(self.previewLayer)

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
    self._cameraView = CameraView()
    self._cameraFeedSession = None
    self.viewDidAppear()

  def viewDidAppear(self):
    # xxx: エラーハンドリング飛ばしてる
    self._cameraView.previewLayer.setVideoGravity_(
      'AVLayerVideoGravityResizeAspectFill')
    self.setupAVSession()
    self._cameraView.previewLayer.setSession_(self._cameraFeedSession)
    self._cameraFeedSession.startRunning()

  def viewWillDisappear(self):
    self._cameraFeedSession.stopRunning()

  def setupAVSession(self):
    # xxx: 
    _videoDevice = AVCaptureDevice.devices()
    videoDevice = _videoDevice[0]
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      videoDevice, None)

    session = AVCaptureSession.alloc().init()
    session.beginConfiguration()
    high = 'AVCaptureSessionPresetHigh'
    session.setSessionPreset_(high)
    if session.canAddInput_(deviceInput):
      session.addInput_(deviceInput)
    else:
      # xxx: 他のエラーも探す
      print('Could not add video device input to the session')

    dataOutput = AVCaptureVideoDataOutput.alloc().init()
    dataOutput.alwaysDiscardsLateVideoFrames = True
    #dataOutput.setVideoSettings_()
    # todo: 後で調査調整
    dataOutput.videoSettings = {
      ns('kCVPixelBufferPixelFormatTypeKey'): int(1111970369)
    }

    session.commitConfiguration()
    self._cameraFeedSession = session


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.cameraViewController = CameraViewController()
    self.add_subview(self.cameraViewController._cameraView)

  def will_close(self):
    self.cameraViewController.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

