# [A simple synthesizer class in Swift · GitHub](https://gist.github.com/larsaugustin/1ba0b01ace8772cf5ecbda8f4e3cf63d)

from objc_util import ObjCClass, ObjCInstance
import pdbg

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

  def _setup(self):
    self.audioEngine = AVAudioEngine.new()
    format = self.audioEngine.outputNode().inputFormatForBus(0)

    #pdbg.state(format)
    #commonFormat
    #sampleRate
    #isInterleaved
    #pdbg.state(format.isInterleaved())
    #pdbg.state(AVAudioFormat.new())
    #initWithCommonFormat_sampleRate_channels_interleaved_',
    inputFormat = AVAudioFormat.alloc().initWithCommonFormat(
      format.commonFormat(),
      sampleRate=format.sampleRate(),
      channels=1,
      interleaved=format.isInterleaved())
    pdbg.state(inputFormat)


if __name__ == '__main__':
  synthesizer = Synthesizer()
  synthesizer._setup()

