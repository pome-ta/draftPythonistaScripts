import ctypes

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super
from pyrubicon.objc.types import CGRectMake

from rbedge.functions import NSStringFromClass
from rbedge import pdbr

SCNView = ObjCClass('SCNView')

UIViewController = ObjCClass('UIViewController')
NSLayoutConstraint = ObjCClass('NSLayoutConstraint')


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

    #scnView = SCNView.new()
    scnView = SCNView.alloc().initWithFrame_(CGRectMake(
      0.0, 0.0, 100.0, 100.0))
    scnView.setShowsStatistics_(True)
    #pdbr.state(scnView)
    # --- Layout
    safeAreaLayoutGuide = self.view.safeAreaLayoutGuide
    pdbr.state(scnView.leadingAnchor)

    self.view.addSubview_(scnView)
    scnView.translatesAutoresizingMaskIntoConstraints = False
    '''
    
    NSLayoutConstraint.activateConstraints_([
      scnView.topAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.topAnchor),
      scnView.leadingAnchor.constraintEqualToAnchor_(safeAreaLayoutGuide.leadingAnchor),
      #scnView.leadingAnchor.constraintEqualToAnchor_multiplier_(safeAreaLayoutGuide.leadingAnchor,0.8),
      scnView.trailingAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.trailingAnchor),
      scnView.bottomAnchor.constraintEqualToAnchor_(safeAreaLayoutGuide.bottomAnchor),
      
    ])
    '''
    
    NSLayoutConstraint.activateConstraints_([
      scnView.centerXAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerXAnchor),
      scnView.centerYAnchor.constraintEqualToAnchor_(
        safeAreaLayoutGuide.centerYAnchor),
      scnView.widthAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.widthAnchor, 1.0),
      scnView.heightAnchor.constraintEqualToAnchor_multiplier_(
        safeAreaLayoutGuide.heightAnchor, 0.5),
    ])


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

