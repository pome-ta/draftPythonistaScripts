import time
import ctypes
from objc_util import ObjCClass, ObjCBlock, ObjCInstance

import pdbg

NSOperationQueue = ObjCClass('NSOperationQueue')
CMMotionManager = ObjCClass('CMMotionManager')
CMMotionManager_ = CMMotionManager.alloc().init()

if not CMMotionManager_.isAccelerometerAvailable():
  print('Accelerometer in NOT Available.')
  raise

CMMotionManager_.accelerometerUpdateInterval = 1  # 単位は秒


def _handler(_cmd, _data, _error):
  accelerometerData = ObjCInstance(_data)
  #pdbg.state(accelerometerData)
  print('😇----')
  #pdbg.state(accelerometerData.acceleration())
  print(accelerometerData.acceleration().a)


accelerometer_handler = ObjCBlock(
  _handler,
  restype=None,
  argtypes=[ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p])

CMMotionManager_.startAccelerometerUpdatesToQueue_withHandler_(
  NSOperationQueue.mainQueue(), accelerometer_handler)

if __name__ == '__main__':
  #pdbg.state(CMMotionManager_)
  #pass
  #accelerometerData = CMMotionManager_.startAccelerometerUpdates()
  #time.sleep(3)  # 単位は秒
  #print(accelerometerData)
  #print(CMMotionManager_.accelerometerData())
  #pdbg.state(NSOperationQueue)
  #currentQueue
  #mainQueue
  #print(NSOperationQueue.currentQueue())
  #print(NSOperationQueue.mainQueue())
  pdbg.state(CMMotionManager_.accelerometerData())
  time.sleep(3)
  #pdbg.state(CMMotionManager_.accelerometerData())
  print(CMMotionManager_.accelerometerData())
  CMMotionManager_.stopAccelerometerUpdates()

