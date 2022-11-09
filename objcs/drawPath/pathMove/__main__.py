import ctypes

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class, CGSize, CGRect, CGPoint, on_main_thread
import ui

import pdbg

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')

UIColor = ObjCClass('UIColor')


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


class ShapeView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.previewLayer = AVCaptureVideoPreviewLayer.new()
    self.overlayLayer = CAShapeLayer.new()
    self.layer = self.objc_instance.layer()
    self.layer.addSublayer_(self.previewLayer)

  def layout(self):
    self.previewLayer.frame = self.objc_instance.bounds()
    self.overlayLayer.frame = self.previewLayer.bounds()


class UpdateViewController:
  def __init__(self):
    self.shapeView = ShapeView()
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    self.cameraQueue = dispatch_queue_create('imageDispatch', None)

    self.viewDidAppear()

  def viewDidAppear(self):
    self.prepareAVSession()
    self.shapeView.previewLayer.setSession_(self.cameraSession)

    _resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self.shapeView.previewLayer.setVideoGravity_(_resizeAspectFill)
    self.cameraSession.startRunning()

  def viewWillDisappear(self):
    self.cameraSession.stopRunning()

  def prepareAVSession(self):
    session = AVCaptureSession.new()
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
      print(f'-out: {self.counter}')
      self.counter += 1

    def captureOutput_didDropSampleBuffer_fromConnection_(
        _felf, _cmd, _output, _sampleBuffer, _connection):
      ObjCInstance(_sampleBuffer)  # todo: 呼ぶだけ
      print(f'drp-: {self.counter}')
      self.counter += 1

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
    self.uvc = UpdateViewController()
    self.add_subview(self.uvc.shapeView)

  def will_close(self):
    self.uvc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

