from objc_util import load_framework, ObjCClass, on_main_thread
from objc_util import UIColor, UIImage, NSData, nsurl
import ui

import pdbg

load_framework('SceneKit')

SCNScene = ObjCClass('SCNScene')
SCNView = ObjCClass('SCNView')
SCNNode = ObjCClass('SCNNode')

SCNLight = ObjCClass('SCNLight')
SCNCamera = ObjCClass('SCNCamera')



class GameScene:
  def __init__(self):
    self.scene: SCNScene
    self.setUpScene()

  def setUpScene(self):

    # --- import
    robot_URL = nsurl('./character/robot.usdz')
    
    # --- SCNScene
    scene = SCNScene.sceneWithURL_options_(robot_URL, None)
    scene.background().contents = UIColor.yellowColor()

    scene_rootNode_addChildNode_ = scene.rootNode().addChildNode_

    robotNode = scene.rootNode().objectInChildNodesAtIndex_(0)
    
    #pdbg.state(robotNode)
    


    # --- SCNLight
    lightNode = SCNNode.node()
    lightNode.light = SCNLight.light()
    #lightNode.castsShadow = True
    lightNode.position = (0.0, 8.0, 8.0)
    scene_rootNode_addChildNode_(lightNode)

    # --- SCNCamera
    camera = SCNCamera.camera()
    '''

    camera.wantsHDR = True
    camera.bloomBlurRadius = 18.0
    camera.bloomIntensity = 1.0
    camera.bloomThreshold = 1.0
    camera.colorFringeIntensity = 4.0
    camera.colorFringeStrength = 4.0
    camera.motionBlurIntensity = 6
    '''

    camera.xFov = 35.0
    camera.yFov = 35.0

    cameraNode = SCNNode.node()
    cameraNode.camera = camera
    cameraNode.position = (0.0, 0.25, 2.0)
    scene_rootNode_addChildNode_(cameraNode)

    self.scene = scene


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.name = ''
    self.bg_color = 'maroon'

    self.scene: GameScene
    self.scnView: SCNView

    self.viewDidLoad()
    self.objc_instance.addSubview_(self.scnView)

  #@on_main_thread
  def viewDidLoad(self):
    scene = GameScene()

    # --- SCNView
    _frame = ((0, 0), (100, 100))
    scnView = SCNView.alloc().initWithFrame_(_frame)
    scnView.setAutoresizingMask_((1 << 1) | (1 << 4))
    scnView.backgroundColor = UIColor.blackColor()

    scnView.allowsCameraControl = True
    scnView.showsStatistics = True
    '''
    OptionNone = 0
    ShowPhysicsShapes = (1 << 0)
    ShowBoundingBoxes = (1 << 1)
    ShowLightInfluences = (1 << 2)
    ShowLightExtents = (1 << 3)
    ShowPhysicsFields = (1 << 4)
    ShowWireframe = (1 << 5)
    RenderAsWireframe = (1 << 6)
    ShowSkeletons = (1 << 7)
    ShowCreases = (1 << 8)
    ShowConstraints = (1 << 9)
    ShowCameras = (1 << 10)
    '''
    _debugOptions = ((1 << 0) | (1 << 1) | (1 << 2) | (1 << 3) | (1 << 10))
    scnView.debugOptions = _debugOptions

    scnView.autorelease()

    scnView.scene = scene.scene
    self.scene = scene
    self.scnView = scnView

  def touch_began(self, touch):
    pass


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

