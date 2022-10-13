import time
import ctypes
from objc_util import ObjCClass, ObjCBlock, ObjCInstance

import pdbg

NSOperationQueue = ObjCClass('NSOperationQueue')
CMMotionManager = ObjCClass('CMMotionManager')


class MotionAccelerometer:
  def __init__(self, update_interval=0.1):
    self.accelerometerData = []
    self.CMMotionManager = CMMotionManager.alloc().init()
    if not self.CMMotionManager.isAccelerometerAvailable():
      print('Accelerometer in NOT Available.')
      raise
    self.accelerometerUpdateInterval = update_interval
    
    self.accelerometer_handler = ObjCBlock(
      self.__handler,
      restype=None,
      argtypes=[ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p])

  def startAccelerometerUpdates(self):
    self.CMMotionManager.accelerometerUpdateInterval = self.accelerometerUpdateInterval
    self.CMMotionManager.startAccelerometerUpdatesToQueue_withHandler_(
      NSOperationQueue.mainQueue(), self.accelerometer_handler)

  def stopAccelerometerUpdates(self, timer=3):
    time.sleep(timer)
    self.CMMotionManager.stopAccelerometerUpdates()

  def append_data(self, data):
    acceleration = data.acceleration()
    x = acceleration.a
    y = acceleration.b
    z = acceleration.c
    ts = data.timestamp()
    self.accelerometerData.append({'x': x, 'y': y, 'z': z, 'at': ts})

  def __handler(self, _cmd, _data, _error):
    data = ObjCInstance(_data)
    self.append_data(data)


if __name__ == '__main__':
  ma = MotionAccelerometer()
  ma.startAccelerometerUpdates()
  ma.stopAccelerometerUpdates(2)
  print(ma.accelerometerData)

