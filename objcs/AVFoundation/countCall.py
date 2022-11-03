import ctypes

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class, CGRect, CGPoint, on_main_thread
import ui

import pdbg

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')

UIColor = ObjCClass('UIColor')
UITextView = ObjCClass('UITextView')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p


def dispatch_queue_create(_name, parent):
  _func = c.dispatch_queue_create
  _func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
  _func.restype = ctypes.c_void_p
  name = _name.encode('ascii')
  return ObjCInstance(_func(name, parent))


class CameraView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.layer = self.objc_instance.layer()
    self.log = None  # UITextView
    self.init()
    self.setupOverlay()

  def init(self):
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().init()
    self.log = UITextView.alloc().init()
    self.log.setEditable_(False)
    self.log.backgroundColor = UIColor.clearColor()

  def setupOverlay(self):
    self.layer.addSublayer_(self.previewLayer)
    self.objc_instance.addSubview_(self.log)

  def layout(self):
    self.previewLayer.frame = self.objc_instance.bounds()
    self.log.frame = self.previewLayer.bounds()

  @on_main_thread
  def log_update(self, text):
    self.log.text = f'{text}'


class CameraViewController:
  def __init__(self):
    self.cameraView = CameraView()
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    #self.cameraQueue = ObjCInstance(dispatch_get_current_queue())

    self.cameraQueue = dispatch_queue_create('imageDispatch', None)

    self.viewDidAppear()

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

  def create_sampleBufferDelegate(self):
    self.counter = 0

    # --- /delegate
    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)

      self.counter += 1
      self.cameraView.log_update(f'did: {self.counter}')

    def captureOutput_didDropSampleBuffer_fromConnection_(
        _felf, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)
      self.counter += 1
      self.cameraView.log_update(f'drp: {self.counter}')

      # --- delegate/

    _methods = [
      captureOutput_didOutputSampleBuffer_fromConnection_,
      captureOutput_didDropSampleBuffer_fromConnection_,
    ]

    _protocols = ['AVCaptureVideoDataOutputSampleBufferDelegate']

    sampleBufferDelegate = create_objc_class(
      'sampleBufferDelegate', methods=_methods, protocols=_protocols)
    return sampleBufferDelegate.new()


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.cvc = CameraViewController()
    self.add_subview(self.cvc.cameraView)

  def will_close(self):
    self.cvc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

