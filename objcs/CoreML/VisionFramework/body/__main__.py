import ctypes

from objc_util import c, ObjCClass, ObjCInstance, create_objc_class
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = ctypes.c_void_p


class CameraViewController:
  def __init__(self, _previewView):
    self.previewView = _previewView
    self.cameraSession = None
    # xxx: ObjCInstance 必要？
    self.cameraQueue = ObjCInstance(dispatch_get_current_queue())
    self.viewDidAppear()

  def viewDidAppear(self):
    self.prepareAVSession()

  def prepareAVSession(self):
    session = AVCaptureSession.alloc().init()
    session.beginConfiguration()
    _Preset_high = 'AVCaptureSessionPresetHigh'
    session.setSessionPreset_(_Preset_high)
    
    _BuiltInWideAngleCamera = 1
    _video = 'vide'
    _front = 2
    videoDevice = AVCaptureDevice.defaultDeviceWithDeviceType_mediaType_position_(_BuiltInWideAngleCamera, _video, _front)
    pdbg.state(videoDevice)

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
    self.present(style='fullscreen', orientations=['portrait'])
    self.cvc = CameraViewController(self.objc_instance)

  def will_close(self):
    pass


if __name__ == '__main__':
  view = View()

