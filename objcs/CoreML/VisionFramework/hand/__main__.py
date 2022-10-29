import math
import ctypes
from objc_util import c, create_objc_class, ObjCClass, ObjCInstance, CGRect, CGPoint
import ui

import pdbg

# xxx: Vision framework のload は不要？
#from objc_util import load_framework
#load_framework('Vision')

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

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p


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
    self._videoDataOutputQueue = ObjCInstance(dispatch_get_current_queue())
    self._cameraFeedSession = None
    self._handPoseRequest = VNDetectHumanHandPoseRequest.alloc().init(
    )  #.autorelease()

    self.viewDidLoad()
    self.viewDidAppear()

  def viewDidLoad(self):
    self._handPoseRequest.maximumHandCount = 1

  def viewDidAppear(self):
    # xxx: エラーハンドリング飛ばしてる
    _resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self._cameraView.previewLayer.setVideoGravity_(_resizeAspectFill)
    self.setupAVSession()
    self._cameraView.previewLayer.setSession_(self._cameraFeedSession)
    self._cameraFeedSession.startRunning()

  def viewWillDisappear(self):
    self._cameraFeedSession.stopRunning()

  def setupAVSession(self):
    # xxx: sample の初期呼び出しを飛ばしてる
    
    # todo: [0]- back, [1]- front
    videoDevice = AVCaptureDevice.devices()[0]
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      videoDevice, None)

    session = AVCaptureSession.alloc().init()
    session.beginConfiguration()
    _Preset_high = 'AVCaptureSessionPresetHigh'
    session.setSessionPreset_(_Preset_high)
    if session.canAddInput_(deviceInput):
      session.addInput_(deviceInput)
    else:
      # xxx: 他のエラーも探す
      print('Could not add video device input to the session')
      raise

    dataOutput = AVCaptureVideoDataOutput.alloc().init()
    
    if (session.canAddOutput_(dataOutput)):
      session.addOutput_(dataOutput)
      dataOutput.alwaysDiscardsLateVideoFrames = True
      # todo: 後で調査調整
      dataOutput.videoSettings = {
        'kCVPixelBufferPixelFormatTypeKey': 1111970369  #420f
      }
      delegate = self.create_sampleBufferDelegate()
      dataOutput.setSampleBufferDelegate_queue_(delegate,
                                                self._videoDataOutputQueue)
    else:
      print('Could not add video data output to the session')

    session.commitConfiguration()
    self._cameraFeedSession = session

  def create_sampleBufferDelegate(self):
    # --- /delegate
    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      kCGImagePropertyOrientationUp = 1

      sampleBuffer = ObjCInstance(_sampleBuffer)
      handler = VNImageRequestHandler.alloc(
      ).initWithCMSampleBuffer_orientation_options_(
        sampleBuffer, kCGImagePropertyOrientationUp, None)#.autorelease()

      handler.performRequests_error_([self._handPoseRequest], None)

      observation = self._handPoseRequest.results().firstObject()

      if (observation):
        #pdbg.state(self._handPoseRequest.results())
        #pdbg.state(observation.availableGroupKeys())
        thumbPoints = observation.recognizedPointsForGroupKey_error_('VNHumanHandPoseObservationJointsGroupNameThumb', None)

        indexFingerPoints = observation.recognizedPointsForGroupKey_error_('VNHumanHandPoseObservationJointsGroupNameIndexFinger', None)

        print(f'thumbPoints: \n{thumbPoints}')
        print(f'indexFingerPoints: \n{indexFingerPoints}')
        #allPoints = observation.recognizedPointsForGroupKey_error_('VNHumanHandPoseObservationJointsGroupNameAll', None)
        #print(allPoints)

    # --- delegate/
    _methods = [captureOutput_didOutputSampleBuffer_fromConnection_]
    _protocols = ['AVCaptureVideoDataOutputSampleBufferDelegate']

    sampleBufferDelegate = create_objc_class(
      'sampleBufferDelegate', methods=_methods, protocols=_protocols)

    return sampleBufferDelegate.new()


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

