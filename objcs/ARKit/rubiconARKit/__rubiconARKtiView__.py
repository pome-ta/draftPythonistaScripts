import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

SCNView = ObjCClass('SCNView')
SCNScene = ObjCClass('SCNScene')
SCNNode = ObjCClass('SCNNode')

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class GameScene:

  def __init__(self):
    self.scene: SCNScene
    self.setUpScene()

  def setUpScene(self):
    scene = SCNScene.scene()
    # ---
    # ここに処理を書いていく
    # ---
    scene.rootNode.addChildNode_(SCNNode.node())
    pdbr.state(scene)
    self.scene = scene


class MainViewController(UIViewController):

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

    #scene = GameScene()
    scnView = SCNView.new()
    #scnView.backgroundColor = UIColor.systemBackgroundColor()
    #scnView.delegate = self

    #scnView = SCNView.alloc().initWithFrame_(CGRectMake(0.0, 0.0, 100.0, 100.0))

    #pdbr.state(scnView)
    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide

    self.view.addSubview_(scnView)
    scnView.translatesAutoresizingMaskIntoConstraints = False

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

    
    #scnView.scene = scene.scene
    scnView.scene = SCNScene.scene()
    #scnView.setShowsStatistics_(True)
    scnView.allowsCameraControl = True
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
    _debugOptions = ((1 << 0) | (1 << 1) | (1 << 4) | (1 << 10))
    scnView.debugOptions = _debugOptions

    scnView.showsStatistics = True

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

  #print('--- run ---')
  main_vc = MainViewController.new()

  presentation_style = UIModalPresentationStyle.fullScreen
  #presentation_style = UIModalPresentationStyle.pageSheet

  app = App(main_vc, presentation_style)
  app.present()
  #print('--- end ---')

