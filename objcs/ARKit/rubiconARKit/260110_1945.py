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

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

CGRectZero = CGRect.in_dll(load_library('CoreGraphics'), 'CGRectZero')

SCNPreferredRenderingAPIKey = str(
  objc_const(SceneKit, 'SCNPreferredRenderingAPIKey'))


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


class ARSceneReconstruction(IntFlag):
  none = 0
  mesh = 1 << 0
  meshWithClassification = (1 << 1) | (1 << 0)


class MainViewController(UIViewController):

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

    #scnView = ARSCNView.new()
    scnView = ARSCNView.alloc().initWithFrame_options_(
      CGRectZero, {
        SCNPreferredRenderingAPIKey: SCNRenderingAPI.metal,
      })

    scnView.session.delegate = self
    scnView.setAllowsCameraControl_(True)

    debugOptions = SCNDebugOptions.showFeaturePoints | SCNDebugOptions.showWorldOrigin
    scnView.setDebugOptions_(debugOptions)
    scnView.setShowsStatistics_(True)

    coachingOverlayView = ARCoachingOverlayView.new()
    coachingOverlayView.setGoal_(ARCoachingGoal.tracking)
    coachingOverlayView.setActivatesAutomatically_(True)
    coachingOverlayView.setSession_(scnView.session)
    coachingOverlayView.setActive_animated_(True, True)

    scnView.addSubview_(coachingOverlayView)
    self.view.addSubview_(scnView)

    # --- Layout

    scnView.translatesAutoresizingMaskIntoConstraints = False
    coachingOverlayView.translatesAutoresizingMaskIntoConstraints = False

    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    NSLayoutConstraint.activateConstraints_([
      scnView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      scnView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
      scnView.widthAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.widthAnchor, 1.0),
      scnView.heightAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.heightAnchor, 1.0),
    ])

    NSLayoutConstraint.activateConstraints_([
      coachingOverlayView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      coachingOverlayView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
      coachingOverlayView.widthAnchor.constraintEqualToAnchor_multiplier_(
        scnView.widthAnchor, 0.4),
      coachingOverlayView.heightAnchor.constraintEqualToAnchor_multiplier_(
        scnView.heightAnchor, 0.4),
    ])

    self.scnView = scnView
    self.coachingOverlayView = coachingOverlayView

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])

    configuration = ARWorldTrackingConfiguration.new()
    configuration.setSceneReconstruction_(ARSceneReconstruction.mesh)

    self.scnView.session.runWithConfiguration_(configuration)

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
    self.scnView.session.pause()

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

  # MARK: - ARSessionDelegate
  @objc_method
  def session_didUpdateFrame_(self, session, frame):
    #print('didUpdateFrame')
    pass

  @objc_method
  def session_didAddAnchors_(self, session, anchors):
    print('didAddAnchors')

  @objc_method
  def session_didUpdateAnchors_(self, session, anchors):
    print('didUpdateAnchors')

  @objc_method
  def session_didRemoveAnchors_(self, session, anchors):
    print('didRemoveAnchors')


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = MainViewController.new()

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

