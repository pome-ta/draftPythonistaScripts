import ctypes
import math

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class, CGSize, CGRect, CGPoint, on_main_thread
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

UITextView = ObjCClass('UITextView')


def dispatch_get_current_queue():
  _func = c.dispatch_get_current_queue
  _func.restype = ctypes.c_void_p
  return ObjCInstance(_func())


def dispatch_queue_create(_name, parent):
  _func = c.dispatch_queue_create
  _func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
  _func.restype = ctypes.c_void_p
  name = _name.encode('ascii')
  return ObjCInstance(_func(name, parent))


def parseCGRect(cg_rect: CGRect) -> tuple:
  _origin = cg_rect.origin
  _size = cg_rect.size
  origin_x = _origin.x
  origin_y = _origin.y
  size_width = _size.width
  size_height = _size.height
  return (origin_x, origin_y, size_width, size_height)


class CameraView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.overlayLayer = None  # CAShapeLayer
    self.layer = self.objc_instance.layer()
    self.log = None  # UITextView
    self.init()
    self.setupOverlay()
    self.setCAShapeLayer()

  def init(self):
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().init()
    self.overlayLayer = CAShapeLayer.alloc().init()

    self.log = UITextView.alloc().init()
    self.log.setEditable_(False)
    self.log.backgroundColor = UIColor.clearColor()

  def setupOverlay(self):
    self.layer.addSublayer_(self.previewLayer)

    self.objc_instance.addSubview_(self.log)

  def layout(self):
    self.previewLayer.frame = self.objc_instance.bounds()
    self.overlayLayer.frame = self.previewLayer.bounds()
    self.log.frame = self.previewLayer.bounds()

  @on_main_thread
  def log_update(self, text):
    self.log.text = f'{text}'

  @on_main_thread
  def showPoints(self, _x, _y):
    #height = size.height
    #width = size.width
    _, _, _width, _height = parseCGRect(self.overlayLayer.frame())
    x = _width - (_width * (1 - _x))
    y = _height - (_height * _y)

    center = CGPoint(x, y)
    #center = CGPoint(_width / 2, _height / 2)
    radius = 8.0
    startAngle = 0.125 * math.pi
    endAngle = 1.875 * math.pi

    arc = UIBezierPath.alloc().init()
    arc.addArcWithCenter_radius_startAngle_endAngle_clockwise_(
      center, radius, startAngle, endAngle, True)

    self.overlayLayer.setPath_(arc.CGPath())

  def setCAShapeLayer(self):
    self.overlayLayer.setLineWidth_(2.0)
    blueColor = UIColor.blueColor().cgColor()
    cyanColor = UIColor.cyanColor().cgColor()
    self.overlayLayer.setStrokeColor_(blueColor)
    self.overlayLayer.setFillColor_(cyanColor)
    self.previewLayer.addSublayer_(self.overlayLayer)


class CameraViewController:
  def __init__(self):
    self.cameraView = CameraView()
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    #self.cameraQueue = dispatch_get_current_queue()

    self.cameraQueue = dispatch_queue_create('imageDispatch', None)

    self.handPoseRequest = VNDetectHumanHandPoseRequest.alloc().init(
    )  #.autorelease()

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
    
    self.finger_names = ['VNHLKIDIP', 'VNHLKITIP']

  def detectedHandPose_request(self, request):
    results = request.results()
    for n, result in enumerate(results):
      _all = 'VNIPOAll'  # VNHumanHandPoseObservationJointsGroupNameAll
      handParts = result.recognizedPointsForJointsGroupName_error_(_all, None)
      #vnhlkidpi = handParts['VNHLKIDIP']
      #vnhlkidpi = handParts['VNHLKITIP']
      for name in self.finger_names:
        finger = handParts[name]
        x = finger.x()
        y = finger.y()
        #self.cameraView.log_update(f'{handParts}')
        self.cameraView.showPoints(x, y)
        
      '''
      x = vnhlkidpi.x()
      y = vnhlkidpi.y()
      self.cameraView.log_update(f'{handParts}')
      self.cameraView.showPoints(x, y)
      '''

      if not n:  # todo: first?
        break

  def create_sampleBufferDelegate(self):

    sequenceHandler = VNSequenceRequestHandler.alloc().init()  #.autorelease()
    _right = 6  # kCGImagePropertyOrientationRight
    self.handParts = None

    # --- /delegate
    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      
      sampleBuffer = ObjCInstance(_sampleBuffer)
      #pdbg.state(sampleBuffer)
      sequenceHandler.performRequests_onCMSampleBuffer_orientation_error_(
        [self.handPoseRequest], sampleBuffer, _right, None)

      #self.cameraView.log_update(f'{self.handPoseRequest.results()}')
      if self.handPoseRequest.results():
        self.detectedHandPose_request(self.handPoseRequest)
      

    def captureOutput_didDropSampleBuffer_fromConnection_(
        _felf, _cmd, _output, _sampleBuffer, _connection):
      ObjCInstance(_sampleBuffer)  # todo: 呼ぶだけ
      
      #pdbg.state(sampleBuffer)
      

      # --- delegate/

    _methods = [
      captureOutput_didOutputSampleBuffer_fromConnection_,
      captureOutput_didDropSampleBuffer_fromConnection_,
    ]

    _protocols = ['AVCaptureVideoDataOutputSampleBufferDelegate']

    sampleBufferDelegate = create_objc_class(
      'sampleBufferDelegate', methods=_methods, protocols=_protocols)
    return sampleBufferDelegate.alloc().init()


class View(ui.View):
  #@on_main_thread
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

