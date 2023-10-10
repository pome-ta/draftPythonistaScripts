import ctypes
from objc_util import ObjCClass

import pdbg

CHANNEL = 1

AVAudioEngine = ObjCClass('AVAudioEngine')
AVAudioSourceNode = ObjCClass('AVAudioSourceNode')
AVAudioFormat = ObjCClass('AVAudioFormat')


class AudioBuffer(ctypes.Structure):
  _fields_ = [
    ('mNumberChannels', ctypes.c_uint32),
    ('mDataByteSize', ctypes.c_uint32),
    ('mData', ctypes.c_void_p),
  ]


class AudioBufferList(ctypes.Structure):
  _fields_ = [
    ('mNumberBuffers', ctypes.c_uint32),
    ('mBuffers', AudioBuffer * CHANNEL),
  ]


class Synth:

  def __init__(self):
    self.audioEngine: AVAudioEngine
    self.sampleRate: float = 44100.0  # set_up メソッド: outputNode より確定
    self.deltaTime: float = 0.0  # 1/sampleRate 時間間隔

    self.set_up()

  def set_up(self):
    audioEngine = AVAudioEngine.new()
    sourceNode = AVAudioSourceNode.alloc()
    mainMixer = audioEngine.mainMixerNode()
    outputNode = audioEngine.outputNode()
    format = outputNode.inputFormatForBus_(0)

    self.sampleRate = format.sampleRate()
    self.deltaTime = 1 / self.sampleRate

    inputFormat = AVAudioFormat.alloc(
    ).initWithCommonFormat_sampleRate_channels_interleaved_(
      format.commonFormat(), self.sampleRate, CHANNEL, format.isInterleaved())


if __name__ == '__main__':
  synth = Synth()

