import ctypes
from objc_util import c, ObjCInstance


MIDIGetNumberOfSources = c.MIDIGetNumberOfSources
MIDIGetNumberOfSources.argtypes = []
MIDIGetNumberOfSources.restype = ctypes.c_void_p

#midi_gnos = MIDIGetNumberOfSources()


MIDIGetNumberOfDevices = c.MIDIGetNumberOfDevices
MIDIGetNumberOfDevices.argtypes = []
MIDIGetNumberOfDevices.restype = ctypes.c_void_p

midi_gnod = MIDIGetNumberOfDevices()
