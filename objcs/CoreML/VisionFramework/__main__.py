from objc_util import ObjCClass, CGRect, CGPoint, CGSize
import ui

import pdbg

# xxx: Vision framework のload は不要？
VNDetectHumanHandPoseRequest = ObjCClass('VNDetectHumanHandPoseRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')


# [PythonやJupyterでiPhone/iPad先端機能を簡単･自由にプログラミング！「土台篇」：hirax](https://techbookfest.org/product/wTZTyeibm5GQ5XgdfMrEBV?productVariantID=kRDmN1udbEYZUWbETdwL8r)
class LiveCameraView(ui.View):
  def __init__(self, device=0, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self._session = ObjCClass('AVCaptureSession').alloc().init()
    self._session.setSessionPreset_('AVCaptureSessionPresetHigh')
    inputDevices = ObjCClass('AVCaptureDevice').devices()
    self._inputDevice = inputDevices[device]

    deviceInput = ObjCClass(
      'AVCaptureDeviceInput').deviceInputWithDevice_error_(
        self._inputDevice, None)
    if self._session.canAddInput_(deviceInput):
      self._session.addInput_(deviceInput)
    self._previewLayer = ObjCClass(
      'AVCaptureVideoPreviewLayer').alloc().initWithSession_(self._session)
    self._previewLayer.setVideoGravity_('AVLayerVideoGravityResizeAspectFill')
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


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.rootview = LiveCameraView(frame=(0, 0, 576, 576))
    self.add_subview(self.rootview)

  def will_close(self):
    self.rootview.will_close()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

