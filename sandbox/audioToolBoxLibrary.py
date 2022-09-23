from ctypes import *

SIMToolkitGeneralBeep = 1052
AudioToolbox = cdll.LoadLibrary(
  "/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox")
AudioToolbox.AudioServicesPlaySystemSound(SIMToolkitGeneralBeep)

