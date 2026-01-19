# [Displaying a point cloud using scene depth | Apple Developer Documentation](https://developer.apple.com/documentation/arkit/displaying-a-point-cloud-using-scene-depth?language=objc)

import ctypes
from enum import IntEnum, IntFlag

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, load_library
from pyrubicon.objc.types import CGRect, NSUInteger

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

SceneKit = load_library('SceneKit')
ARKit = load_library('ARKit')

ARSCNView = ObjCClass('ARSCNView')
ARCoachingOverlayView = ObjCClass('ARCoachingOverlayView')
ARWorldTrackingConfiguration = ObjCClass('ARWorldTrackingConfiguration')
ARMeshAnchor = ObjCClass('ARMeshAnchor')

SCNGeometrySource = ObjCClass('SCNGeometrySource')
SCNGeometryElement = ObjCClass('SCNGeometryElement')
SCNGeometry = ObjCClass('SCNGeometry')
SCNMaterial = ObjCClass('SCNMaterial')
SCNNode = ObjCClass('SCNNode')

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

CGRectZero = CGRect.in_dll(load_library('CoreGraphics'), 'CGRectZero')

# xxx: PEP8では非推奨
constSceneKit = lambda const_name: str(objc_const(SceneKit, const_name))

SCNPreferredRenderingAPIKey = constSceneKit('SCNPreferredRenderingAPIKey')


class SCNLightingModel:
  blinn = constSceneKit('SCNLightingModelBlinn')
  constant = constSceneKit('SCNLightingModelConstant')
  lambert = constSceneKit('SCNLightingModelLambert')
  phong = constSceneKit('SCNLightingModelPhong')
  physicallyBased = constSceneKit('SCNLightingModelPhysicallyBased')
  shadowOnly = constSceneKit('SCNLightingModelShadowOnly')


class SCNRenderingAPI(IntEnum):
  metal = 0
  openGLES2 = 1


#showFeaturePoints
ARSCNDebugOptionShowFeaturePoints_ulong = NSUInteger.in_dll(
  ARKit, 'ARSCNDebugOptionShowFeaturePoints')

#showWorldOrigin
ARSCNDebugOptionShowWorldOrigin_ulong = NSUInteger.in_dll(
  ARKit, 'ARSCNDebugOptionShowWorldOrigin')


class SCNDebugOptions(IntFlag):
  none = 0
  showPhysicsShapes = 1 << 0
  showBoundingBoxes = 1 << 1
  showLightInfluences = 1 << 2
  showLightExtents = 1 << 3
  showPhysicsFields = 1 << 4
  showWireframe = 1 << 5
  renderAsWireframe = 1 << 6
  showSkeletons = 1 << 7
  showCreases = 1 << 8
  showConstraints = 1 << 9
  showCameras = 1 << 10
  showFeaturePoints = ARSCNDebugOptionShowFeaturePoints_ulong.value
  showWorldOrigin = ARSCNDebugOptionShowWorldOrigin_ulong.value


class ARCoachingGoal(IntEnum):
  tracking = 0
  horizontalPlane = 1
  verticalPlane = 2
  anyPlane = 3
  geoTracking = 4


# ref: [ARConfiguration.rs - source](https://docs.rs/objc2-ar-kit/latest/src/objc2_ar_kit/generated/ARConfiguration.rs.html#158-170)
class ARSceneReconstruction(IntFlag):
  none = 0
  mesh = 1 << 0
  meshWithClassification = (1 << 1) | (1 << 0)


class SCNGeometrySourceSemantic:
  vertex = str(objc_const(SceneKit, 'SCNGeometrySourceSemanticVertex'))
  normal = str(objc_const(SceneKit, 'SCNGeometrySourceSemanticNormal'))
  texcoord = str(objc_const(SceneKit, 'SCNGeometrySourceSemanticTexcoord'))


class SCNGeometryPrimitiveType(IntEnum):
  triangles = 0
  triangleStrip = 1
  line = 2
  point = 3


class SCNFillMode(IntEnum):
  fill = 0
  lines = 1


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




class PointCloudDepthSample(UIViewController):

  scnView: ARSCNView = objc_property()
  coachingOverlayView: ARCoachingOverlayView = objc_property()

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    #print(f'\t - {NSStringFromClass(__class__)}: dealloc')
    pass

  @objc_method
  def loadView(self):
    send_super(__class__, self, 'loadView')

  @objc_method
  def viewDidLoad(self):
    send_super(__class__, self, 'viewDidLoad')
    self.navigationItem.title = NSStringFromClass(__class__)



  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

    

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    

  @objc_method
  def viewDidDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'\t{NSStringFromClass(__class__)}: didReceiveMemoryWarning')

  # MARK: - ARSCNViewDelegate
  @objc_method
  def renderer_didAddNode_forAnchor_(self, renderer, node, anchor):
    if not isinstance((meshAnchor := anchor), ARMeshAnchor):
      return
    self.appendChildNode_forMeshAnchor_(node, meshAnchor)

  @objc_method
  def renderer_didUpdateNode_forAnchor_(self, renderer, node, anchor):
    if not isinstance((meshAnchor := anchor), ARMeshAnchor):
      return

    if (previousMeshNode := node.childNodeWithName_recursively_(
        identifier.UUIDString if (identifier := meshAnchor.identifier) else '',
        True)):
      previousMeshNode.removeFromParentNode()
    self.appendChildNode_forMeshAnchor_(node, meshAnchor)

  # MARK: - ARSessionDelegate
  @objc_method
  def session_didUpdateFrame_(self, session, frame):
    #print('didUpdateFrame')
    pass

  @objc_method
  def session_didAddAnchors_(self, session, anchors):
    #print('didAddAnchors')
    pass

  @objc_method
  def session_didUpdateAnchors_(self, session, anchors):
    #print('didUpdateAnchors')
    pass

  @objc_method
  def session_didRemoveAnchors_(self, session, anchors):
    #print('didRemoveAnchors')
    pass

  # --- private
  @objc_method
  def appendChildNode_forMeshAnchor_(self, node, meshAnchor):
    meshGeometry = ARSCNMeshGeometry(meshAnchor)
    meshNode = meshGeometry.setNode_(UIColor.systemCyanColor())
    meshNode.setName_(meshAnchor.identifier.UUIDString)

    node.addChildNode_(meshNode)


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = PointCloudDepthSample.new()

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

