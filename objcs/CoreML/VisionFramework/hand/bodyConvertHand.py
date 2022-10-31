import ctypes

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')

VNSequenceRequestHandler = ObjCClass('VNSequenceRequestHandler')
VNDetectHumanBodyPoseRequest = ObjCClass('VNDetectHumanBodyPoseRequest')

VNDetectHumanHandPoseRequest = ObjCClass('VNDetectHumanHandPoseRequest')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p


class CameraViewController:
  def __init__(self, cameraView):
    self.cameraView = cameraView
    self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    self.cameraQueue = ObjCInstance(dispatch_get_current_queue())
    self.handPoseRequest = VNDetectHumanHandPoseRequest.alloc().init()

    self.viewDidLoad()
    self.viewDidAppear()

  # todo: 独自に生やした
  def layout(self):
    self.previewLayer.frame = self.cameraView.bounds()

  def viewDidLoad(self):
    self.handPoseRequest.maximumHandCount = 1

  def viewDidAppear(self):
    self.prepareAVSession()
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().initWithSession_(
      self.cameraSession)
    _resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self.previewLayer.videoGravity = _resizeAspectFill
    self.cameraView.layer().addSublayer_(self.previewLayer)
    self.layout()
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

  def create_sampleBufferDelegate(self):
    # --- /delegate
    sequenceHandler = VNSequenceRequestHandler.alloc().init().autorelease()

    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)

      _right = 6  # kCGImagePropertyOrientationRight
      sequenceHandler.performRequests_onCMSampleBuffer_orientation_error_(
        [self.handPoseRequest], sampleBuffer, _right, None)

      results = self.handPoseRequest.results()
      for n, result in enumerate(results):
        _all = 'VNIPOAll'  # VNHumanHandPoseObservationJointsGroupNameAll
        observation = result.recognizedPointsForJointsGroupName_error_(
          _all, None)
        #print(f'nm: {result.availableJointNames()}')
        #print(f'gr{result.availableJointsGroupNames()}')
        #VNHLKIDIP
        vnhlkidpi = observation['VNHLKIDIP']
        x = vnhlkidpi.x()
        y = vnhlkidpi.y()
        #print(type(vnhlkidpi))
        print('----')
        pdbg.state(x)
        print(vnhlkidpi)

        if not n:  # todo: first?
          break
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
    self.cvc = CameraViewController(self.objc_instance)

  def layout(self):
    self.cvc.layout()

  def will_close(self):
    self.cvc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

