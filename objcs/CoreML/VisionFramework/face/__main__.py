from objc_util import ObjCClass
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceDiscoverySession = ObjCClass('AVCaptureDeviceDiscoverySession')

class ViewController:
  def __init__(self):
    # AVCapture variables to hold sequence data
    self.session = None
    
    self.viewDidLoad()

  def viewDidLoad(self):
    self.session = self._setupAVCaptureSession()
    _builtInWideAngleCamera = 'AVCaptureDeviceTypeBuiltInWideAngleCamera'
    #_builtInWideAngleCamera = 1
    _video = 'AVMediaTypeVideo'
    _front = 1  # AVCaptureDevicePositionFront
    pdbg.state(AVCaptureDeviceDiscoverySession.discoverySessionWithDeviceTypes_mediaType_position_(_builtInWideAngleCamera, _video, _front))

  # --- AVCapture Setup
  def _setupAVCaptureSession(self):
    captureSession = AVCaptureSession.alloc().init()
    
  def _configureFrontCamera_for_(self, captureSession):
    pass
    


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.view_controller = ViewController()

  def will_close(self):
    pass


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

