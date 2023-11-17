# [A simple synthesizer class in Swift · GitHub](https://gist.github.com/larsaugustin/1ba0b01ace8772cf5ecbda8f4e3cf63d)

from objc_util import ObjCClass, ObjCInstance
import pdbg

AVAudioEngine = ObjCClass('AVAudioEngine')
AVAudioSourceNode = ObjCClass('AVAudioSourceNode')

pdbg.state(AVAudioEngine)


class Synthesizer:

  def __init__(self):
    self.audioEngine = 0
    self.time = 0.0


if __name__ == '__main__':
  pass

