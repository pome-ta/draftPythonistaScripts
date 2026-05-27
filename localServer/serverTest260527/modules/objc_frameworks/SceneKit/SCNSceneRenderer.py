from enum import IntEnum, IntFlag


class SCNRenderingAPI(IntEnum):
  #[doc(alias = "SCNRenderingAPIMetal")]
  metal = 0
  openGLES2 = 1


class SCNDebugOptions(IntFlag):
  #[doc(alias = "SCNDebugOptionNone")]
  none = 0
  #[doc(alias = "SCNDebugOptionShowPhysicsShapes")]
  showPhysicsShapes = 1 << 0
  #[doc(alias = "SCNDebugOptionShowBoundingBoxes")]
  showBoundingBoxes = 1 << 1
  #[doc(alias = "SCNDebugOptionShowLightInfluences")]
  showLightInfluences = 1 << 2
  #[doc(alias = "SCNDebugOptionShowLightExtents")]
  showLightExtents = 1 << 3
  #[doc(alias = "SCNDebugOptionShowPhysicsFields")]
  showPhysicsFields = 1 << 4
  #[doc(alias = "SCNDebugOptionShowWireframe")]
  showWireframe = 1 << 5
  #[doc(alias = "SCNDebugOptionRenderAsWireframe")]
  renderAsWireframe = 1 << 6
  #[doc(alias = "SCNDebugOptionShowSkeletons")]
  showSkeletons = 1 << 7
  #[doc(alias = "SCNDebugOptionShowCreases")]
  showCreases = 1 << 8
  #[doc(alias = "SCNDebugOptionShowConstraints")]
  showConstraints = 1 << 9
  #[doc(alias = "SCNDebugOptionShowCameras")]
  showCameras = 1 << 10

