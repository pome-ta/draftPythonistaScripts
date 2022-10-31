import ctypes

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class, CGRect
import ui

import pdbg

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p



def parseCGRect(cg_rect: CGRect) -> tuple:
  _origin = cg_rect.origin
  _size = cg_rect.size
  origin_x = _origin.x
  origin_y = _origin.y
  size_width = _size.width
  size_height = _size.height
  return (origin_x, origin_y, size_width, size_height)




class CameraViewController:
  def __init__(self, cameraView):
    self.cameraView = cameraView
    self.previewLayer = None  # AVCaptureVideoPreviewLayer
    self.cameraSession = None  # AVCaptureSession
    self.delegate = self.create_sampleBufferDelegate()
    self.cameraQueue = ObjCInstance(dispatch_get_current_queue())
    #self.cameraQueue = dispatch_get_current_queue()
    self.viewDidAppear()
  
  def layout(self):
    self.previewLayer.frame = self.cameraView.bounds()
  
  def viewDidAppear(self):
    self.prepareAVSession()
    self.previewLayer = AVCaptureVideoPreviewLayer.alloc().initWithSession_(self.cameraSession)
    _resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self.previewLayer.videoGravity = _resizeAspectFill
    self.cameraView.layer().addSublayer_(self.previewLayer)
    
    self.previewLayer.frame = self.cameraView.bounds()
    #pdbg.state(self.previewView)
    
    self.cameraSession.startRunning()
    
    
    
    
  def viewWillDisappear(self):
    self.cameraSession.stopRunning()

  def prepareAVSession(self):
    session = AVCaptureSession.alloc().init()
    session.beginConfiguration()
    _Preset_high = 'AVCaptureSessionPresetHigh'
    session.setSessionPreset_(_Preset_high)

    videoDevice = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      videoDevice, None)

    if session.canAddInput_(deviceInput):
      session.addInput_(deviceInput)

    dataOutput = AVCaptureVideoDataOutput.alloc().init()
    if session.canAddOutput_(dataOutput):
      session.addOutput_(dataOutput)
      dataOutput.setSampleBufferDelegate_queue_(self.delegate,
                                                self.cameraQueue)
    session.commitConfiguration()
    self.cameraSession = session

  def create_sampleBufferDelegate(self):
    # --- /delegate
    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      requestHandlerOptions = None
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

