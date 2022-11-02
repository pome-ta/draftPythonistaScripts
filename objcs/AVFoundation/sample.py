# coding: utf-8
# based on Cethric's image capture gist....
#FRAME_PROC_INTERVAL = 15  #num frames to skip. 1=go as fast as possible, 5=every fifth frame

import ctypes

import ui
from objc_util import ObjCClass, ObjCInstance, create_objc_class, c, on_main_thread

AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')
AVCaptureStillImageOutput = ObjCClass('AVCaptureStillImageOutput')
AVCaptureConnection = ObjCClass('AVCaptureConnection')


def dispatch_queue_create(name, parent):
  func = c.dispatch_queue_create
  func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
  func.restype = ctypes.c_void_p
  return ObjCInstance(func(name, parent))


def dispatch_get_current_queue():
  func = c.dispatch_get_current_queue
  func.argtypes = []
  #func.restype = c_void_p
  func.restype = ctypes.c_void_p
  return ObjCInstance(func())


def dispatch_release(queue_obj):
  #raise RuntimeError('This is not the method you are looking for')
  func = c.dispatch_release
  func.argtyps = [ctypes.c_void_p]
  func.restype = None
  return func(ObjCInstance(queue_obj).ptr)


'''
cnt = 0


def captureOutput_didOutputSampleBuffer_fromConnection_(
    _cmd, _self, _output, _buffer, _connection):
  #view.frame_count = (view.frame_count + 1)
  global cnt
  cnt += 1
  print(cnt)


delegate_call = create_objc_class(
  'delegate_call',
  protocols=['AVCaptureVideoDataOutputSampleBufferDelegate'],
  methods=[captureOutput_didOutputSampleBuffer_fromConnection_])
'''


class CameraView(ui.View):
  #@on_main_thread
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.inputDevice = AVCaptureDevice.devices()[0]
    self.captureInput = AVCaptureDeviceInput.deviceInputWithDevice_error_(
      self.inputDevice, None)
    if not self.captureInput:
      print('Failed to create device')
      exit()
    self.captureOutput = AVCaptureVideoDataOutput.alloc().init()
    self.captureSession = AVCaptureSession.alloc().init()
    self.captureSession.setSessionPreset_('AVCaptureSessionPresetHigh')

    if self.captureSession.canAddInput_(self.captureInput):
      self.captureSession.addInput_(self.captureInput)
    if self.captureSession.canAddOutput_(self.captureOutput):
      self.captureSession.addOutput_(self.captureOutput)
    self.captureVideoPreviewLayer = AVCaptureVideoPreviewLayer.layerWithSession_(
      self.captureSession)

    #queue_test = dispatch_queue_create(b'imageDispatch', None)
    queue_test = dispatch_get_current_queue()

    #callback = delegate_call.alloc().init()
    callback = self.create_sampleBufferDelegate().alloc().init()

    self.captureOutput.setSampleBufferDelegate_queue_(callback, queue_test)
    self.queue = queue_test
    self.set_layer()

  def set_layer(self):
    v = ObjCInstance(self)
    self.captureVideoPreviewLayer.setFrame_(v.bounds())
    self.captureVideoPreviewLayer.setVideoGravity_(
      'AVLayerVideoGravityResizeAspectFill')
    v.layer().addSublayer_(self.captureVideoPreviewLayer)
    self.captureSession.startRunning()

  #@on_main_thread
  def will_close(self):
    self.captureSession.stopRunning()
    #dispatch_release(self.queue)

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
    return sampleBufferDelegate


class CustomView(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.frame = (0, 0, 800, 600)
    self.present()
    self.cv = CameraView(frame=(0, 0, 400, 600), name='camera')
    self.add_subview(self.cv)
    '''self.frame_count = 0
    self.processed_frames = 0
    self.last_time = time.perf_counter()
    self.faces = []
    self.rects = []'''
    #self['camera'].set_layer()

  def did_load(self):
    self['camera'].set_layer()
    #self['imageview1'].image = ui.Image.named('test:Numbers')

  '''
  def present(self, *args, **kwargs):
    ui.View.present(self, *args, **kwargs)
    print('h')
  '''

  def will_close(self):
    self['camera'].will_close()


view = CustomView()
#cv = CameraView(frame=(0, 0, 400, 600), name='camera')
#pv = PathView(frame=(0, 0, 400, 600), name='path')
#iv=ui.ImageView(name='imageview1', frame=(400,0,400,600))
#lbl = ui.Label(name='lbl', frame=(0, 0, 800, 200))
#lbl.text_color = '#fbff99'
#view.add_subview(cv)
#view.add_subview(pv)
#view.add_subview(iv)
#view.add_subview(lbl)
#view.did_load()
#view.present()

