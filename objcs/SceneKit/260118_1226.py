#https://cdn-ak.f.st-hatena.com/images/fotolife/x/x67x6fx74x6f/20080922/20080922100958.jpg
# [iOS で SceneKit を試す(Swift 3) その4 - SceneKit の構造 - Apple Engine](https://appleengine.hatenablog.com/entry/2017/05/30/192435)

import ctypes
from enum import IntEnum, IntFlag

from pyrubicon.objc.api import ObjCClass, ObjCInstance
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, load_library
from pyrubicon.objc.types import CGRect, NSUInteger

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

SceneKit = load_library('SceneKit')

SCNScene = ObjCClass('SCNScene')
SCNView = ObjCClass('SCNView')

SCNNode = ObjCClass('SCNNode')
SCNSphere = ObjCClass('SCNSphere')
SCNLight = ObjCClass('SCNLight')
SCNCamera = ObjCClass('SCNCamera')

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


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

class SCNLightType:
  IES = str(objc_const(SceneKit, 'SCNLightTypeIES'))
  ambient = str(objc_const(SceneKit, 'SCNLightTypeAmbient'))
  directional = str(objc_const(SceneKit, 'SCNLightTypeDirectional'))
  omni = str(objc_const(SceneKit, 'SCNLightTypeOmni'))
  probe = str(objc_const(SceneKit, 'SCNLightTypeProbe'))
  spot = str(objc_const(SceneKit, 'SCNLightTypeSpot'))
  area = str(objc_const(SceneKit, 'SCNLightTypeArea'))




class GameScene:

  def __init__(self):
    self.scene: SCNScene
    self.setUpScene()

  def setUpScene(self):
    scene = SCNScene.scene()

    rootNodeAddChildNode_ = scene.rootNode.addChildNode_

    # --- SCNSphere
    sphere = SCNSphere.sphereWithRadius_(2.0)
    sphereNode = SCNNode.nodeWithGeometry_(sphere)
    rootNodeAddChildNode_(sphereNode)

    # --- SCNLight
    lightNode = SCNNode.node()
    lightNode.light = SCNLight.light()
    lightNode.light.type = SCNLightType.omni

  
    lightNode.position = (0.0, 10.0, 10.0)
    rootNodeAddChildNode_(lightNode)

    # --- SCNCamera
    cameraNode = SCNNode.node()
    cameraNode.camera = SCNCamera.camera()
    cameraNode.position = (0.0, 0.0, 10.0)
    rootNodeAddChildNode_(cameraNode)

    self.scene = scene


class MainViewController(UIViewController):

  scnView: SCNView = objc_property()

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

    gameScene = GameScene()

    scnView = SCNView.new()
    #scnView.backgroundColor = UIColor.systemBackgroundColor()
    scnView.backgroundColor = UIColor.systemBlackColor()
    
    scnView.scene = gameScene.scene

    debugOptions = SCNDebugOptions.showBoundingBoxes | SCNDebugOptions.showCameras
    scnView.debugOptions = debugOptions
    scnView.showsStatistics = True

    scnView.allowsCameraControl = True

    self.view.addSubview_(scnView)

    # --- Layout

    scnView.translatesAutoresizingMaskIntoConstraints = False

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

    self.scnView = scnView

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


if __name__ == '__main__':
  from rbedge.app import App
  from rbedge.enumerations import UIModalPresentationStyle

  main_vc = MainViewController.new()

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()

