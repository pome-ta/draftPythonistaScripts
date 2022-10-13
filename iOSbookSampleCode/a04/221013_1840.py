import time
import ctypes
from objc_util import ObjCClass, ObjCBlock, ObjCInstance

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

  def get_accelerometer_data(self, timer=3):
    self.startAccelerometerUpdates()
    self.stopAccelerometerUpdates(3)
    return self.accelerometerData

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
  import matplotlib.pyplot as plt
  ma = MotionAccelerometer()
  accelerometerData = ma.get_accelerometer_data()

  x = []
  y = []
  z = []
  t = []
  for a in accelerometerData:
    x.append(a['x'])
    y.append(a['y'])
    z.append(a['z'])
    t.append(a['at'])

  plt.scatter(t, x, c='r')
  plt.scatter(t, y, c='g')
  plt.scatter(t, z, c='b')
  
  plt.plot(t, x, c='r')
  plt.plot(t, y, c='g')
  plt.plot(t, z, c='b')
  
  plt.xlabel('Time (s)')
  plt.ylabel('Acclerometer (m/s^2)')
  plt.show()

