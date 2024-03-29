import ctypes

from objc_util import c, create_objc_class, ObjCClass, ObjCInstance, on_main_thread
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')

VNDetectFaceRectanglesRequest = ObjCClass('VNDetectFaceRectanglesRequest')
VNSequenceRequestHandler = ObjCClass('VNSequenceRequestHandler')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')

UIColor = ObjCClass('UIColor')

UIDevice = ObjCClass('UIDevice')

kCVPixelFormatType_420YpCbCr8BiPlanarFullRange = 875704422
_resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'


class CMVideoDimensions(ctypes.Structure):
  _fields_ = [('width', ctypes.c_int32), ('height', ctypes.c_int32)]


CMFormatDescriptionGetMediaSubType = c.CMFormatDescriptionGetMediaSubType
CMFormatDescriptionGetMediaSubType.argtypes = [ctypes.c_void_p]
CMFormatDescriptionGetMediaSubType.restype = ctypes.c_void_p

CMVideoFormatDescriptionGetDimensions = c.CMVideoFormatDescriptionGetDimensions
CMVideoFormatDescriptionGetDimensions.argtypes = [ctypes.c_void_p]
CMVideoFormatDescriptionGetDimensions.restype = CMVideoDimensions

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p

CMSampleBufferGetImageBuffer = c.CMSampleBufferGetImageBuffer
CMSampleBufferGetImageBuffer.argtypes = [ctypes.c_void_p]
CMSampleBufferGetImageBuffer.restype = ctypes.c_void_p

CMGetAttachment = c.CMGetAttachment
CMGetAttachment.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
CMGetAttachment.restype = ctypes.c_void_p


class ViewController:
  def __init__(self, _previewView):
    # Main view for showing camera content.
    self.previewView = _previewView

    # AVCapture variables to hold sequence data
    self.session = None  # AVCaptureSession
    self.previewLayer = None  # AVCaptureVideoPreviewLayer

    self.videoDataOutput = None  # AVCaptureVideoDataOutput
    self.videoDataOutputQueue = None  # DispatchQueue

    self.captureDevice = None  # AVCaptureDevice
    self.captureDeviceResolution = None  # CGSize

    self.detectionRequests = None  # [VNDetectFaceRectanglesRequest]

    # Layer UI for drawing Vision results
    self.rootLayer = None  # CALayer

    #self.sequenceRequestHandler = VNSequenceRequestHandler.alloc().init() # lazy?

    self.viewDidLoad()

  def viewDidLoad(self):
    self.session = self._setupAVCaptureSession()
    self.prepareVisionRequest()
    self.session.startRunning()

  # todo: 終了処理を追加
  def viewWillDisappear(self):
    self.session.stopRunning()

  # --- AVCapture Setup
  # - Tag: CreateCaptureSession
  def _setupAVCaptureSession(self):
    captureSession = AVCaptureSession.alloc().init()
    inputDevice = self._configureFrontCamera_captureSession_(captureSession)
    self._configureVideoDataOutput_inputDevice_resolution_captureSession_(
      inputDevice['device'], inputDevice['resolution'], captureSession)
    self._designatePreviewLayer_captureSession_(captureSession)
    return captureSession
    # xxx: エラー処理は飛ばす
    # ex: self.teardownAVCapture()

  # - Tag: ConfigureDeviceResolution

  def _highestResolution420Format_device_(self, device):
    highestResolutionFormat = None
    highestResolutionDimensions = CMVideoDimensions(0, 0)

    for _format in device.formats():
      deviceFormat = _format
      deviceFormatDescription = deviceFormat.formatDescription()

      if (CMFormatDescriptionGetMediaSubType(deviceFormatDescription) ==
          kCVPixelFormatType_420YpCbCr8BiPlanarFullRange):
        candidateDimensions = CMVideoFormatDescriptionGetDimensions(
          ObjCInstance(deviceFormatDescription))

        if ((highestResolutionFormat != None) or
            (candidateDimensions.width > highestResolutionDimensions.width)):
          highestResolutionFormat = deviceFormat
          highestResolutionDimensions = candidateDimensions

    if (highestResolutionFormat != None):
      resolution = (highestResolutionDimensions.width,
                    highestResolutionDimensions.height)
      return {'format': highestResolutionFormat, 'resolution': resolution}
    return None

  def _configureFrontCamera_captureSession_(self, captureSession):
    device = AVCaptureDevice.devices()[1]  # front
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      device, None)
    if captureSession.canAddInput_(deviceInput):
      captureSession.addInput_(deviceInput)
    highestResolution = self._highestResolution420Format_device_(device)
    if (device.lockForConfiguration_(None)):
      device.activeFormat = highestResolution['format']
      device.unlockForConfiguration()
      return {'device': device, 'resolution': highestResolution['resolution']}
    else:
      print('NSError(domain: "ViewController", code: 1, userInfo: nil)')
      raise

  # - Tag: CreateSerialDispatchQueue
  def _configureVideoDataOutput_inputDevice_resolution_captureSession_(
      self, inputDevice, resolution, captureSession):
    videoDataOutput = AVCaptureVideoDataOutput.alloc().init()
    videoDataOutput.alwaysDiscardsLateVideoFrames = True

    videoDataOutputQueue = ObjCInstance(dispatch_get_current_queue())
    delegate = self.create_sampleBufferDelegate()
    videoDataOutput.setSampleBufferDelegate_queue_(delegate,
                                                   videoDataOutputQueue)

    if (captureSession.canAddOutput_(videoDataOutput)):
      captureSession.addOutput_(videoDataOutput)

    # todo: 不要？`=` でエラーになる
    #videoDataOutput.connectionWithMediaType_('vide').isEnabled = True

    captureConnection = videoDataOutput.connectionWithMediaType_('vide')

    if (captureConnection.isCameraIntrinsicMatrixDeliverySupported()):
      # todo: 元から`True`
      captureConnection.isCameraIntrinsicMatrixDeliveryEnabled = True

    self.videoDataOutput = videoDataOutput
    self.videoDataOutputQueue = videoDataOutputQueue

    self.captureDevice = inputDevice
    self.captureDeviceResolution = resolution

  # - Tag: DesignatePreviewLayer
  def _designatePreviewLayer_captureSession_(self, captureSession):
    videoPreviewLayer = AVCaptureVideoPreviewLayer.alloc().initWithSession_(
      captureSession)
    self.previewLayer = videoPreviewLayer
    videoPreviewLayer.name = 'CameraPreview'
    videoPreviewLayer.backgroundColor = UIColor.blackColor().cgColor()
    videoPreviewLayer.videoGravity = _resizeAspectFill

    previewRootLayer = self.previewView.layer()
    self.rootLayer = previewRootLayer
    # todo: 元から`True`
    previewRootLayer.masksToBounds = True
    # xxx: サイズが`100` かも
    videoPreviewLayer.frame = previewRootLayer.bounds()
    previewRootLayer.addSublayer_(videoPreviewLayer)

  def exifOrientationForDeviceOrientation(self, deviceOrientation):
    if (deviceOrientation == 2):  # portraitUpsideDown
      return 7  # rightMirrored
    elif (deviceOrientation == 4):  # landscapeLeft
      return 5  # downMirrored
    elif (deviceOrientation == 3):  # landscapeRight
      return 4  # upMirrored
    else:
      return 6  # leftMirrored

  def exifOrientationForCurrentDeviceOrientation(self):
    device_orientation = UIDevice.currentDevice().orientation()
    return self.exifOrientationForDeviceOrientation(device_orientation)

  # --- Performing Vision Requests
  # - Tag: WriteCompletionHandler
  #@on_main_thread
  def prepareVisionRequest(self):
    faceDetectionRequest = VNDetectFaceRectanglesRequest.alloc().init()

    self.detectionRequests = faceDetectionRequest
    self.sequenceRequestHandler = VNSequenceRequestHandler.alloc().init()

  def create_sampleBufferDelegate(self):
    # --- /delegate

    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      requestHandlerOptions = None

      #cameraIntrinsicData = CMGetAttachment(_sampleBuffer, 'RPVideoSampleOrientationKey', None)

      #sampleBuffer = ObjCInstance(_sampleBuffer)
      pixelBuffer = CMSampleBufferGetImageBuffer(_sampleBuffer)
      #pdbg.state(ObjCInstance(pixelBuffer))
      #exifOrientation = self.exifOrientationForCurrentDeviceOrientation()
      #pdbg.state(ObjCInstance(pixelBuffer))
      #pdbg.state(self.detectionRequests.results())

      #imageRequestHandler = VNImageRequestHandler

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
    self.present(style='fullscreen', orientations=['portrait'])
    self.view_controller = ViewController(self.objc_instance)

  def will_close(self):
    self.view_controller.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  #view.present(style='fullscreen', orientations=['portrait'])

