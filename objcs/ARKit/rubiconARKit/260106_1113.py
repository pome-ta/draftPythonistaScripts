import ctypes
from enum import IntEnum

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method, objc_property, objc_const
from pyrubicon.objc.runtime import send_super, load_library
from pyrubicon.objc.types import CGRect

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

SceneKit = load_library('SceneKit')
SCNView = ObjCClass('SCNView')
SCNScene = ObjCClass('SCNScene')

SCNPreferredRenderingAPIKey = str(
  objc_const(SceneKit, 'SCNPreferredRenderingAPIKey'))

CoreGraphics = load_library('CoreGraphics')
CGRectZero = CGRect.in_dll(CoreGraphics, 'CGRectZero')

UIViewController = ObjCClass('UIViewController')
UIColor = ObjCClass('UIColor')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


class SCNRenderingAPI(IntEnum):
  metal = 0
  openGLES2 = 1


class MainViewController(UIViewController):

  scnView: SCNView = objc_property()
  scnScene: SCNScene = objc_property()

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

    #scnView = SCNView.alloc().initWithFrame_(CGRectZero)
    scnView = SCNView.alloc().initWithFrame_options_(
      CGRectZero, {
        SCNPreferredRenderingAPIKey: SCNRenderingAPI.metal,
      })
    #pdbr.state(scnView)
    #scnView = SCNView.new()
    scnScene = SCNScene.new()

    scnView.setScene_(scnScene)

    scnView.setShowsStatistics_(True)
    scnView.setAllowsCameraControl_(True)
    #pdbr.state(scnScene)

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

    self.scnView = scnView
    self.scnScene = scnScene

  @objc_method
  def viewWillAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.scnView)

  @objc_method
  def viewDidAppear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewDidAppear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.scnScene)

  @objc_method
  def viewWillDisappear_(self, animated: bool):
    send_super(__class__,
               self,
               'viewWillDisappear:',
               animated,
               argtypes=[
                 ctypes.c_bool,
               ])
    #pdbr.state(self.scnView.renderingAPI())
    #print(self.scnView.renderingAPI)
    #pdbr.state(self.scnScene)

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

