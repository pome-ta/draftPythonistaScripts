from objc_util import load_framework, ObjCClass
from objc_util import UIColor
import ui

import pdbg

load_framework('ARKit')

ARSCNView = ObjCClass('ARSCNView')
ARBodyTrackingConfiguration = ObjCClass('ARBodyTrackingConfiguration')


class ViewController:
  def __init__(self):
    self.arView: ARSCNView
    self.scene: GameScene
    self.viewDidLoad()
    self.viewWillAppear()

  def viewDidLoad(self):
    #scene = GameScene()

    _frame = ((0, 0), (100, 100))
    arView = ARSCNView.alloc().initWithFrame_(_frame)
    arView.autoresizingMask = (1 << 1) | (1 << 4)
    arView.autoenablesDefaultLighting = True
    arView.showsStatistics = True
    ''' debugOptions
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
    ARSCNDebugOptionShowFeaturePoints = (1 << 30)
    ARSCNDebugOptionShowWorldOrigin = (1 << 32)
    '''

    _debugOptions = (1 << 1) | (1 << 30) | (1 << 32)
    arView.debugOptions = _debugOptions

    #arView.scene = scene.scene
    arView.autorelease()

    #self.scene = scene
    self.arView = arView

  def viewWillAppear(self):
    self.resetTracking()

  def viewWillDisappear(self):
    self.arView.session().pause()

  def resetTracking(self):
    #configuration = ARWorldTrackingConfiguration.new()
    #self.sceneView.session().runWithConfiguration_(configuration)
    pass


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.vc = ViewController()
    self.objc_instance.addSubview_(self.vc.arView)

  def will_close(self):
    self.vc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])
