import ctypes

from objc_util import ObjCClass
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')


class CMVideoDimensions(ctypes.Structure):
    _fields_ = [('width', ctypes.c_float), ('height', ctypes.c_float)]


class ViewController:
    def __init__(self):
        # AVCapture variables to hold sequence data
        self.session = None

        self.viewDidLoad()

    def viewDidLoad(self):
        self.session = self._setupAVCaptureSession()

    # --- AVCapture Setup
    def _setupAVCaptureSession(self):
        captureSession = AVCaptureSession.alloc().init()

    def _highestResolution420Format_for_(self, device):
        highestResolutionFormat = None
        highestResolutionDimensions = CMVideoDimensions(0, 0)
        for _format in device.formats():
            deviceFormat = _format


def _configureFrontCamera_for_(self, captureSession):
    device = AVCaptureDevice.devices()[1]  # front
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
        device, None)
    if captureSession.canAddInput_(deviceInput):
        captureSession.addInput_(deviceInput)


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
