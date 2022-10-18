# [Pythonista/live_camera_view.py at master · tdamdouni/Pythonista](https://github.com/tdamdouni/Pythonista/blob/master/camera/live_camera_view.py)
# todo: partly customized 2022/10/18

from objc_util import ObjCClass, CGRect, CGPoint, CGSize
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')


class LiveCameraView(ui.View):
  def __init__(self, device=0, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self._session = AVCaptureSession.alloc().init()
    #pdbg.state(self._session)
    self._session.setSessionPreset_('AVCaptureSessionPresetHigh')
    inputDevices = AVCaptureDevice.devices()
    self._inputDevice = inputDevices[device]
    pdbg.state(self._inputDevice)

    deviceInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      self._inputDevice, None)
    
    if self._session.canAddInput_(deviceInput):
      self._session.addInput_(deviceInput)
    
    self._previewLayer = AVCaptureVideoPreviewLayer.alloc().initWithSession_(
      self._session)

    resizeAspectFill = 'AVLayerVideoGravityResizeAspectFill'
    self._previewLayer.setVideoGravity_(resizeAspectFill)
    #rootLayer = ObjCInstance(self).layer()
    rootLayer = self.objc_instance.layer()
    rootLayer.setMasksToBounds_(True)
    self._previewLayer.setFrame_(
      CGRect(CGPoint(-70, 0), CGSize(self.height, self.height)))
    rootLayer.insertSublayer_atIndex_(self._previewLayer, 0)
    self._session.startRunning()

  def will_close(self):
    self._session.stopRunning()

  def layout(self):
    if not self._session.isRunning():
      self._session.startRunning()


if __name__ == '__main__':
  rootview = LiveCameraView(frame=(0, 0, 576, 576))
  rootview.present('sheet')

