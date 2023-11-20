# [A simple synthesizer class in Swift · GitHub](https://gist.github.com/larsaugustin/1ba0b01ace8772cf5ecbda8f4e3cf63d)
import ctypes
from objc_util import ObjCClass, ObjCInstance, ObjCBlock, on_main_thread
import pdbg

OSStatus = ctypes.c_int32
noErr = 0

AVAudioEngine = ObjCClass('AVAudioEngine')
AVAudioSourceNode = ObjCClass('AVAudioSourceNode')
AVAudioFormat = ObjCClass('AVAudioFormat')


class Synthesizer:

  def __init__(self):
    self.audioEngine: AVAudioEngine
    self.sourceNode: AVAudioSourceNode
    self.time = 0.0
    self.frequencyRamp = 0.0
    self.currentFrequency = 0.0

  #@on_main_thread
  def _setup(self):
    self.audioEngine = AVAudioEngine.new()
    outputNode = self.audioEngine.outputNode()
    #format = self.audioEngine.outputNode().inputFormatForBus(0)
    format = outputNode.inputFormatForBus(0)

    inputFormat = AVAudioFormat.alloc().initWithCommonFormat(
      format.commonFormat(),
      sampleRate=format.sampleRate(),
      channels=1,
      interleaved=format.isInterleaved())
    #pdbg.state(inputFormat)
    #pdbg.state(format.sampleRate())
    renderBlock = ObjCBlock(self._create_block,
                            restype=OSStatus,
                            argtypes=[
                              ctypes.c_void_p,
                              ctypes.c_void_p,
                              ctypes.c_void_p,
                              ctypes.c_void_p,
                            ])
    #pdbg.state(renderBlock)
    #pdbg.state(self.audioEngine)
    self.sourceNode = AVAudioSourceNode.alloc().initWithRenderBlock(
      renderBlock)
    #pdbg.state(self.sourceNode)

    self.audioEngine.attachNode(self.sourceNode)
    #pdbg.state(self.audioEngine)
    self.audioEngine.connect(self.sourceNode,
                             to=outputNode,
                             format=inputFormat)

  #@on_main_thread
  def _create_block(self, _cmd, _isSilence, _timestamp, _frameCount,
                    _outputData):
    print('h')
    return noErr

  def start(self):
    self.audioEngine.startAndReturnError(None)


if __name__ == '__main__':
  synthesizer = Synthesizer()
  synthesizer._setup()
  synthesizer.start()

