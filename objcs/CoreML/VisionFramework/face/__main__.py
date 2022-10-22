import ctypes

from objc_util import c, ObjCClass, ObjCInstance
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')


class CMVideoDimensions(ctypes.Structure):
  _fields_ = [('width', ctypes.c_int32), ('height', ctypes.c_int32)]


CMFormatDescriptionGetMediaSubType = c.CMFormatDescriptionGetMediaSubType
CMFormatDescriptionGetMediaSubType.argtypes = [ctypes.c_void_p]
CMFormatDescriptionGetMediaSubType.restype = ctypes.c_void_p

CMVideoFormatDescriptionGetDimensions = c.CMVideoFormatDescriptionGetDimensions
CMVideoFormatDescriptionGetDimensions.argtypes = [ctypes.c_void_p]
CMVideoFormatDescriptionGetDimensions.restype = CMVideoDimensions


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
    self._configureFrontCamera_for_(captureSession)

  def _highestResolution420Format_for_(self, device):
    kCVPixelFormatType_420YpCbCr8BiPlanarFullRange = 875704422
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
      return (highestResolutionFormat, resolution)
    return None

  def _configureFrontCamera_for_(self, captureSession):
    device = AVCaptureDevice.devices()[1]  # front
    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      device, None)
    if captureSession.canAddInput_(deviceInput):
      captureSession.addInput_(deviceInput)
    highestResolution = self._highestResolution420Format_for_(device)
    print(highestResolution)


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

