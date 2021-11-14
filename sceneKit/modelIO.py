import ui
from objc_util import ObjCClass, load_framework, nsurl

import pdbg

load_framework('SceneKit')

UIColor = ObjCClass('UIColor')

#https://stackoverflow.com/questions/35511851/objective-c-scenekit-import-obj-file-externally-and-color-it


class SceneView:
  def __init__(self, frame):
    self.view = self.viewDidLoad(frame)

  def viewDidLoad(self, frame):
    scnView = ObjCClass('SCNView').alloc()
    _frame = ((frame[0], frame[1]), (frame[2], frame[3]))
    scnView.initWithFrame_(_frame)
    scnView.autoresizingMask = ((1 << 1) | (1 << 4))
    #scnView.backgroundColor = UIColor.blackColor()
    scnView.backgroundColor = UIColor.lightGrayColor()
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
    #scnView.debugOptions = (1 << 1) | (1 << 3) | (1 << 5) | (1 << 6) | (1 << 7) | (1 << 10)

    SCNScene = ObjCClass('SCNScene')

    objUrl = nsurl('./Resources/mushroom.obj')
    scene = SCNScene.scene()

    asset = ObjCClass('MDLAsset').new()
    asset.initWithURL_(objUrl)

    SCNNode = ObjCClass('SCNNode')

    node = SCNNode.nodeWithMDLObject_(asset.objectAtIndex_(0))

    pngUrl = ObjCClass('NSData').dataWithContentsOfURL_(
      nsurl('./Resources/mushroom.png'))
    tex_png = ObjCClass('UIImage').alloc().initWithData_(pngUrl)

    material = ObjCClass('SCNMaterial').material()
    material.diffuse().setContents_(tex_png)
    node.geometry().setFirstMaterial_(material)
    pdbg.state(node.geometry())

    scene.rootNode().addChildNode_(node)

    cameraNode = SCNNode.node()
    cameraNode.camera = ObjCClass('SCNCamera').camera()
    cameraNode.position = (0.0, 0.0, 15.0)
    scene.rootNode().addChildNode_(cameraNode)

    scnView.scene = scene

    return scnView


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'

    scn = SceneView(self.frame)
    self.objc_instance.addSubview_(scn.view)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

