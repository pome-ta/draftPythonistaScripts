from objc_util import ObjCClass

import pdbg

AVAudioBuffer = ObjCClass('AVAudioBuffer')


#buf = AVAudioBuffer.alloc()
pdbg.state(AVAudioBuffer.description())
