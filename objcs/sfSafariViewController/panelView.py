from objc_util import ObjCClass, nsurl, on_main_thread
import ui

import pdbg

SFVC = ObjCClass('SFSafariViewController')
URL = 'https://github.com/pome-ta'


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)

  #@on_main_thread
  def run(self):
    sfvc = SFVC.alloc().initWithURL_(nsurl(URL))
    sfvc.view().setAutoresizingMask_((1 << 1) | (1 << 4))
    self.objc_instance.addSubview_(sfvc.view())
    #sfvc.view().setAutoresizingMask_((1 << 1) | (1 << 4))

    self.present(style='panel')  #must be presented for nextResponder to work
    
    #parentViewController
    #firstResponder
    self.objc_instance.nextResponder().addChildViewController_(sfvc)
    #sfvc.didMoveToParentViewController_(self.objc_instance)
    #pdbg.state(self.objc_instance.nextResponder())
    #pdbg.state(self.objc_instance)
    
    #presentViewController_animated_completion_

    #sfSafariViewController.release()
    #pdbg.state(sfvc.view())
    
    #self.objc_instance.nextResponder().presentViewController_animated_completion_(sfvc,True, None)
    #sfvc.release()
    pdbg.state(sfvc.view())


if __name__ == '__main__':
  view = View()
  view.run()


