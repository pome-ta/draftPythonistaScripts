from objc_util import ObjCClass, ObjCInstance, CGRect, CGPoint, CGSize
import ui

import pdbg

AVCaptureSession = ObjCClass('AVCaptureSession')

AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')


def dispatch_queue_create(_name, parent):
  _func = c.dispatch_queue_create
  _func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
  _func.restype = ctypes.c_void_p
  name = _name.encode('ascii')
  return ObjCInstance(_func(name, parent))


class ShapeLayerView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.overlayLayer = CAShapeLayer.new()
    self.objc_instance.layer().addSublayer_(self.overlayLayer)

  def layout(self):
    self.overlayLayer.frame = self.objc_instance.bounds()


class UpdateViewController:
  def __init__(self):
    self.delegate = self.create_sampleBufferDelegate()
    self.cameraQueue = dispatch_queue_create('imageDispatch', None)

  def create_sampleBufferDelegate(self):
    # --- /delegate
    def captureOutput_didOutputSampleBuffer_fromConnection_(
        _self, _cmd, _output, _sampleBuffer, _connection):
      sampleBuffer = ObjCInstance(_sampleBuffer)

    def captureOutput_didDropSampleBuffer_fromConnection_(
        _felf, _cmd, _output, _sampleBuffer, _connection):
      ObjCInstance(_sampleBuffer)  # todo: 呼ぶだけ
      # --- delegate/

    _methods = [
      captureOutput_didOutputSampleBuffer_fromConnection_,
      captureOutput_didDropSampleBuffer_fromConnection_,
    ]

    _protocols = ['AVCaptureVideoDataOutputSampleBufferDelegate']

    sampleBufferDelegate = create_objc_class(
      'sampleBufferDelegate', methods=_methods, protocols=_protocols)
    return sampleBufferDelegate.alloc().init()


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.shapelayer_view = ShapeLayerView()
    self.add_subview(self.shapelayer_view)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

