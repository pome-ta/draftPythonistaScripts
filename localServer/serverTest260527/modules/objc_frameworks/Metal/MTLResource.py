from enum import IntEnum, IntFlag

from .resource import (
  MTLResourceCPUCacheModeShift,
  MTLResourceStorageModeShift,
  MTLResourceHazardTrackingModeShift,
)


class MTLCPUCacheMode(IntEnum):
  #[doc(alias = "MTLCPUCacheModeDefaultCache")]
  defaultCache = 0
  #[doc(alias = "MTLCPUCacheModeWriteCombined")]
  writeCombined = 1


class MTLStorageMode(IntEnum):
  #[doc(alias = "MTLStorageModeShared")]
  shared = 0
  #[doc(alias = "MTLStorageModeManaged")]
  managed = 1
  #[doc(alias = "MTLStorageModePrivate")]
  Private = 2
  #[doc(alias = "MTLStorageModeMemoryless")]
  memoryless = 3


class MTLHazardTrackingMode(IntEnum):
  #[doc(alias = "MTLHazardTrackingModeDefault")]
  default = 0
  #[doc(alias = "MTLHazardTrackingModeUntracked")]
  untracked = 1
  #[doc(alias = "MTLHazardTrackingModeTracked")]
  tracked = 2


class MTLResourceOptions(IntFlag):
  #[doc(alias = "MTLResourceCPUCacheModeDefaultCache")]
  cpuCacheModeDefaultCache = MTLCPUCacheMode.defaultCache << MTLResourceCPUCacheModeShift
  #[doc(alias = "MTLResourceCPUCacheModeWriteCombined")]
  cpuCacheModeWriteCombined = MTLCPUCacheMode.writeCombined << MTLResourceCPUCacheModeShift
  #[doc(alias = "MTLResourceStorageModeShared")]
  storageModeShared = MTLStorageMode.shared << MTLResourceStorageModeShift
  #[doc(alias = "MTLResourceStorageModeManaged")]
  storageModeManaged = MTLStorageMode.managed << MTLResourceStorageModeShift
  #[doc(alias = "MTLResourceStorageModePrivate")]
  storageModePrivate = MTLStorageMode.Private << MTLResourceStorageModeShift
  #[doc(alias = "MTLResourceStorageModeMemoryless")]
  storageModeMemoryless = MTLStorageMode.memoryless << MTLResourceStorageModeShift
  #[doc(alias = "MTLResourceHazardTrackingModeDefault")]
  hazardTrackingModeDefault = MTLHazardTrackingMode.default << MTLResourceHazardTrackingModeShift
  #[doc(alias = "MTLResourceHazardTrackingModeUntracked")]
  hazardTrackingModeUntracked = MTLHazardTrackingMode.untracked << MTLResourceHazardTrackingModeShift
  #[doc(alias = "MTLResourceHazardTrackingModeTracked")]
  hazardTrackingModeTracked = MTLHazardTrackingMode.tracked << MTLResourceHazardTrackingModeShift
  #[doc(alias = "MTLResourceOptionCPUCacheModeDefault")]
  optionCPUCacheModeDefault = cpuCacheModeDefaultCache  #[deprecated]
  #[doc(alias = "MTLResourceOptionCPUCacheModeWriteCombined")]
  OptionCPUCacheModeWriteCombined = cpuCacheModeWriteCombined  #[deprecated]

