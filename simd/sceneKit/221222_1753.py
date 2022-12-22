from math import pi
import ctypes

from objc_util import c, load_framework, ObjCClass, on_main_thread, ObjCInstance, _struct_class_from_fields
from objc_util import UIColor
import ui

import pdbg

load_framework('SceneKit')


class SCNMatrix4(ctypes.Structure):
  _fields_ = [
    ('a', ctypes.c_float),
    ('b', ctypes.c_float),
    ('c', ctypes.c_float),
    ('d', ctypes.c_float),
    ('e', ctypes.c_float),
    ('f', ctypes.c_float),
    ('g', ctypes.c_float),
    ('h', ctypes.c_float),
    ('i', ctypes.c_float),
    ('j', ctypes.c_float),
    ('k', ctypes.c_float),
    ('l', ctypes.c_float),
    ('m', ctypes.c_float),
    ('n', ctypes.c_float),
    ('o', ctypes.c_float),
    ('p', ctypes.c_float),
  ]


'''
class SCNMatrix4(ctypes.Structure):
  _fields_ = [
    ('mNumberChannels', ctypes.c_uint32),
    ('mDataByteSize', ctypes.c_uint32),
    ('mData', ctypes.c_void_p),
  ]
'''


def SCNMatrix4MakeRotation(angle, x, y, z):
  _func = c.SCNMatrix4MakeRotation
  _func.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
  ]
  _func.restype = SCNMatrix4
  #pdbg.state(_func)
  _instance = _func(angle, x, y, z)
  #pdbg.state(_instance.a)
  #obj_instance = ObjCInstance(_instance)
  #return obj_instance
  return _instance


SCNScene = ObjCClass('SCNScene')
SCNView = ObjCClass('SCNView')
SCNNode = ObjCClass('SCNNode')

SCNLight = ObjCClass('SCNLight')
SCNCamera = ObjCClass('SCNCamera')

SCNBox = ObjCClass('SCNBox')


class GameScene:
  def __init__(self):
    self.scene: SCNScene
    self.setUpScene()

  def setUpScene(self):
    scene = SCNScene.scene()
    # 呼び出しが面倒なので、変数化
    scene_rootNode_addChildNode_ = scene.rootNode().addChildNode_

    box = SCNBox.boxWithWidth_height_length_chamferRadius_(2, 1, 1.5, 0.2)
    #box.firstMaterial().diffuse().contents = UIColor.blueColor()
    geometryNode = SCNNode.nodeWithGeometry_(box)
    '''
    geometryNode.runAction_(
      SCNAction.repeatActionForever_(
        SCNAction.rotateByX_y_z_duration_(0.0, 0.2, 0.1, 0.3)))
    '''

    scene_rootNode_addChildNode_(geometryNode)
    #geometryNode.transform = SCNMatrix4MakeRotation(pi / 2, 1, 0, 0)
    #pdbg.state(rt)

    pdbg.state(geometryNode.transform())

    # --- SCNLight
    lightNode = SCNNode.node()
    lightNode.light = SCNLight.light()
    lightNode.position = (0.0, 10.0, 10.0)
    scene_rootNode_addChildNode_(lightNode)

    ambientLightNode = SCNNode.node()
    ambientLightNode.light = SCNLight.light()
    ambientLightNode.light().type = 'ambient'
    ambientLightNode.light().color = UIColor.redColor()
    #ambientLightNode.light().color = UIColor.darkGrayColor()
    scene_rootNode_addChildNode_(ambientLightNode)

    # --- SCNCamera
    cameraNode = SCNNode.node()
    cameraNode.camera = SCNCamera.camera()
    cameraNode.position = (0.0, 0.0, 10.0)
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
    # ui.View.flex = 'WH' と同じ
    scnView.setAutoresizingMask_((1 << 1) | (1 << 4))
    scnView.backgroundColor = UIColor.blackColor()

    scnView.allowsCameraControl = True
    scnView.showsStatistics = True
    scnView.autorelease()

    scnView.scene = scene.scene
    self.scene = scene
    self.scnView = scnView

  def touch_began(self, touch):
    pass


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

