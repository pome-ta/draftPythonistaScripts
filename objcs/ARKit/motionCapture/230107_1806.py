from objc_util import load_framework, ObjCClass
from objc_util import UIColor
import ui

import pdbg

load_framework('ARKit')
load_framework('RealityKit')

ARSCNView = ObjCClass('ARSCNView')
ARBodyTrackingConfiguration = ObjCClass('ARBodyTrackingConfiguration')


class ViewController:
  def __init__(self):
    self.arScnView: ARSCNView
    self.scene: GameScene
    self.viewDidLoad()
    self.viewDidAppear()

  def viewDidLoad(self):
    _frame = ((0, 0), (100, 100))
    arScnView = ARSCNView.alloc().initWithFrame_(_frame)
    arScnView.autoresizingMask = (1 << 1) | (1 << 4)
    arScnView.autoenablesDefaultLighting = True
    arScnView.showsStatistics = True
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
    arScnView.debugOptions = _debugOptions

    arScnView.autorelease()
    self.arScnView = arScnView

  def viewDidAppear(self):
    if not ARBodyTrackingConfiguration.isSupported():
      # xxx: ちゃんと終了処理をする
      print('未対応: This feature is only supported on devices with an A12 chip')
    configuration = ARBodyTrackingConfiguration.new()
    self.arScnView.session().runWithConfiguration_(configuration)

  def viewWillDisappear(self):
    self.arScnView.session().pause()


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.vc = ViewController()
    self.objc_instance.addSubview_(self.vc.arScnView)

  def will_close(self):
    self.vc.viewWillDisappear()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

