import time
from objc_util import ObjCClass

import pdbg

NSOperationQueue = ObjCClass('NSOperationQueue')
CMMotionManager = ObjCClass('CMMotionManager')
CMMotionManager_ = CMMotionManager.alloc().init()

if not CMMotionManager_.isAccelerometerAvailable():
  print('Accelerometer in NOT Available.')
  raise
else:
  print('Accelerometer is Available.')

# 便利のために変数などを用意しておく
CMMotionManager_.accelerometerUpdateInterval = 0.1  # 単位は秒

if __name__ == '__main__':
  pdbg.state(CMMotionManager_)
  accelerometerData = CMMotionManager_.startAccelerometerUpdates()
  time.sleep(3)  # 単位は秒
  print(accelerometerData)
  print(CMMotionManager_.accelerometerData())
  #pdbg.state(NSOperationQueue)
  #currentQueue
  #mainQueue
  #print(NSOperationQueue.currentQueue())
  #print(NSOperationQueue.mainQueue())

