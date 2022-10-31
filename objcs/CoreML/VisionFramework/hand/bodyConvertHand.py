import ctypes
import math

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class, CGRect, CGPoint
import ui

import pdbg

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')

VNSequenceRequestHandler = ObjCClass('VNSequenceRequestHandler')
VNDetectHumanHandPoseRequest = ObjCClass('VNDetectHumanHandPoseRequest')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')

UIColor = ObjCClass('UIColor')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p


class CameraView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.overlayLayer = None  # CAShapeLayer
    self.layer = self.objc_instance.layer()
    self.init()

  def init(self):
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().init()
    self.overlayLayer = CAShapeLayer.alloc().init()

    self.setupOverlay()
    self.setCAShapeLayer()

  def setupOverlay(self):
    self.layer.addSublayer_(self.previewLayer)

  def layout(self):
    self.previewLayer.frame = self.objc_instance.bounds()
    self.overlayLayer.frame = self.previewLayer.bounds()
    self.showPoints(self.overlayLayer.frame().size)

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

    self.overlayLayer.setPath_(arc.CGPath())

  def setCAShapeLayer(self):
    self.overlayLayer.setLineWidth_(20.0)
    blueColor = UIColor.blueColor().cgColor()
    cyanColor = UIColor.cyanColor().cgColor()
    self.overlayLayer.setStrokeColor_(blueColor)
    self.overlayLayer.setFillColor_(cyanColor)
    self.previewLayer.addSublayer_(self.overlayLayer)


class CameraViewController:
  def __init__(self):
    self.cameraView = CameraView()
    #self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    self.cameraQueue = ObjCInstance(dispatch_get_current_queue())
    self.handPoseRequest = VNDetectHumanHandPoseRequest.alloc().init()

    self.viewDidLoad()
    self.viewDidAppear()

  def viewDidLoad(self):
    self.handPoseRequest.maximumHandCount = 1

  def viewDidAppear(self):
    self.prepareAVSession()
    self.cameraView.previewLayer.setSession_(self.cameraSession)

    _resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self.cameraView.previewLayer.setVideoGravity_(_resizeAspectFill)
    self.cameraSession.startRunning()

  def viewWillDisappear(self):
    self.cameraSession.stopRunning()

  def prepareAVSession(self):
    session = AVCaptureSession.alloc().init()
    session.beginConfiguration()
    _Preset_high = 'AVCaptureSessionPresetHigh'
    session.setSessionPreset_(_Preset_high)

    _builtInWideAngleCamera = 'AVCaptureDeviceTypeBuiltInWideAngleCamera'
    _video = 'vide'
    _front = 2  # back -> 1
    _back = 1
    videoDevice = AVCaptureDevice.defaultDeviceWithDeviceType_mediaType_position_(
      _builtInWideAngleCamera, _video, _back)

    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      videoDevice, None)

    if session.canAddInput_(deviceInput):
      session.addInput_(deviceInput)
    else:
      raise

    dataOutput = AVCaptureVideoDataOutput.alloc().init()
    if session.canAddOutput_(dataOutput):
      session.addOutput_(dataOutput)
    else:
      raise
    dataOutput.setSampleBufferDelegate_queue_(self.delegate, self.cameraQueue)
    session.commitConfiguration()
    self.cameraSession = session

  def detectedHandPose_request(self, request):
    results = request.results()
    for n, result in enumerate(results):
      _all = 'VNIPOAll'  # VNHumanHandPoseObservationJointsGroupNameAll
      handParts = result.recognizedPointsForJointsGroupName_error_(_all, None)
      vnhlkidpi = handParts['VNHLKIDIP']
      x = vnhlkidpi.x()
      y = vnhlkidpi.y()
      #print(type(vnhlkidpi))
      #print('----')
      #pdbg.state(x)
      #print(vnhlkidpi)
      greenColor = UIColor.greenColor().cgColor()
      self.cameraView.overlayLayer.setStrokeColor_(greenColor)

      if not n:  # todo: first?
        break

  def create_sampleBufferDelegate(self):
    # --- /delegate
    sequenceHandler = VNSequenceRequestHandler.alloc().init().autorelease()
    self.handParts = None

    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)

      _right = 6  # kCGImagePropertyOrientationRight
      sequenceHandler.performRequests_onCMSampleBuffer_orientation_error_(
        [self.handPoseRequest], sampleBuffer, _right, None)

      if self.handPoseRequest.results():
        self.detectedHandPose_request(self.handPoseRequest)

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
    # xxx: 先に呼ぶ？
    #self.present(style='fullscreen', orientations=['portrait'])
    self.cvc = CameraViewController()
    self.add_subview(self.cvc.cameraView)

  def will_close(self):
    self.cvc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

