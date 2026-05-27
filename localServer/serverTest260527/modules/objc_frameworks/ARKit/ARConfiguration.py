from enum import IntEnum, IntFlag


class ARSceneReconstruction(IntFlag):
  none = 0
  mesh = 1 << 0
  meshWithClassification = (1 << 1) | (1 << 0)


# ref: [ARFrameSemantics | Apple Developer Documentation](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct?language=objc)
class ARFrameSemantics(IntFlag):
  # ref: [ARConfiguration.rs - source](https://docs.rs/objc2-ar-kit/latest/src/objc2_ar_kit/generated/ARConfiguration.rs.html#25-73)
  none = 0
  personSegmentation = 1 << 0
  personSegmentationWithDepth = (1 << 1) | (1 << 0)
  bodyDetection = 1 << 2
  sceneDepth = 1 << 3
  smoothedSceneDepth = 1 << 4


# ref: [AREnvironmentTexturing | Apple Developer Documentation](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/environmenttexturing-swift.enum?language=objc)
class AREnvironmentTexturing(IntEnum):
  # ref: [ARConfiguration.rs - source](https://docs.rs/objc2-ar-kit/latest/src/objc2_ar_kit/generated/ARConfiguration.rs.html#126-137)
  none = 0
  manual = 1
  automatic = 2

