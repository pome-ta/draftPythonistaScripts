import ctypes

from objc_util import ObjCClass, ObjCInstance, create_objc_class, on_main_thread, c
import ui

AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')


def dispatch_get_current_queue():
  func = c.dispatch_get_current_queue
  func.argtypes = []
  func.restype = ctypes.c_void_p
  return ObjCInstance(func())


class CameraViewController:
  def __init__(self, py_uiview):
    self.py_uiview = py_uiview
    self.inputDevice = AVCaptureDevice.devices()[0]
    self.captureInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      self.inputDevice, None)

    if not self.captureInput:
      print('Failed to create device')
      exit()
    self.captureOutput = AVCaptureVideoDataOutput.alloc().init()
    self.captureSession = AVCaptureSession.alloc().init()
    self.captureSession.setSessionPreset_('AVCaptureSessionPresetHigh')

    canadd_in = self.captureSession.canAddInput_(self.captureInput)

    if canadd_in:
      self.captureSession.addInput_(self.captureInput)

    canadd_out = self.captureSession.canAddOutput_(self.captureOutput)

    if canadd_out:
      self.captureSession.addOutput_(self.captureOutput)

    self.captureVideoPreviewLayer = AVCaptureVideoPreviewLayer.layerWithSession_(
      self.captureSession)

    queue_test = dispatch_get_current_queue()
    callback = self.create_sampleBufferDelegate()
    self.captureOutput.setSampleBufferDelegate_queue_(callback, queue_test)
    self.queue = queue_test
    #self.set_layer()

  @on_main_thread
  def set_layer(self):
    v = ObjCInstance(self.py_uiview)
    self.captureVideoPreviewLayer.setFrame_(v.bounds())
    self.captureVideoPreviewLayer.setVideoGravity_(
      'AVLayerVideoGravityResizeAspectFill')
    v.layer().addSublayer_(self.captureVideoPreviewLayer)
    self.captureSession.startRunning()

  def viewWillDisappear(self):
    self.captureSession.stopRunning()

  def create_sampleBufferDelegate(self):
    self.cnt = 0

    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)
      self.cnt += 1
      print(self.cnt)

    _methods = [captureOutput_didOutputSampleBuffer_fromConnection_]
    _protocols = ['AVCaptureVideoDataOutputSampleBufferDelegate']

    sampleBufferDelegate = create_objc_class(
      'sampleBufferDelegate', methods=_methods, protocols=_protocols)
    return sampleBufferDelegate.new()


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.bg_color = 'maroon'
    self.cvc = CameraViewController(self)
    
  def did_load(self):
    self.cvc.set_layer()

  def will_close(self):
    self.cvc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  #view.present(style='fullscreen', orientations=['portrait'])
  view.did_load()
  view.present()

