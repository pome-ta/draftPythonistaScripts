import ctypes
from objc_util import c, ObjCInstance

import pdbg



'''
MIDIGetNumberOfSources = c.MIDIGetNumberOfSources
MIDIGetNumberOfSources.argtypes = []
MIDIGetNumberOfSources.restype = ctypes.c_void_p

#midi_gnos = MIDIGetNumberOfSources()
'''

MIDIGetNumberOfDevices = c.MIDIGetNumberOfDevices
MIDIGetNumberOfDevices.argtypes = []
MIDIGetNumberOfDevices.restype = ctypes.c_int

MIDIGetDevice = c.MIDIGetDevice
MIDIGetDevice.argtypes = [ctypes.c_int]
MIDIGetDevice.restype = ctypes.c_void_p


MIDIObjectGetStringProperty = c.MIDIObjectGetStringProperty
MIDIObjectGetStringProperty.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
MIDIObjectGetStringProperty.restype = ctypes.c_void_p

MIDIDeviceGetNumberOfEntities = c.MIDIDeviceGetNumberOfEntities
MIDIDeviceGetNumberOfEntities.argtypes = [ctypes.c_void_p]
MIDIDeviceGetNumberOfEntities.restype = ctypes.c_void_p




MIDIDeviceGetEntity = c.MIDIDeviceGetEntity
MIDIDeviceGetEntity.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
MIDIDeviceGetEntity.restype = ctypes.c_void_p


count = MIDIGetNumberOfDevices()  # 2がデフォ？
for i in range(count):
  devRef = MIDIGetDevice(i)
  err = MIDIObjectGetStringProperty(devRef, 0, 0)
  numEntities = MIDIDeviceGetNumberOfEntities(devRef)
  for j in range(numEntities):
    entityRef = MIDIDeviceGetEntity(devRef, j)
  
  
  
