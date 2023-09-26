import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


from objc_util import ObjCClass, nsurl, on_main_thread
import ui

import pdbg

SFVC = ObjCClass('SFSafariViewController')
URL = 'http://localhost:8000/'

os.chdir(os.path.join(os.path.dirname(__file__), 'public'))


#httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
#httpd.serve_forever()

#@on_main_thread
class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.server_run()
  
  @ui.in_background
  def server_run(self):
    self.httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    self.httpd.serve_forever()
    

  @on_main_thread
  def run(self):
    self.server_run()
    sfvc = SFVC.alloc().initWithURL_(nsurl(URL))
    sfvc.view().setAutoresizingMask_((1 << 1) | (1 << 4))
    self.objc_instance.addSubview_(sfvc.view())
    #sfvc.view().setAutoresizingMask_((1 << 1) | (1 << 4))

    self.present(style='panel')  #must be presented for nextResponder to work
    
    #parentViewController
    #firstResponder
    self.objc_instance.nextResponder().addChildViewController_(sfvc)
    #sfvc.view().reloadInputViews()
    
    #sfvc.didMoveToParentViewController_(self.objc_instance)
    #pdbg.state(self.objc_instance.nextResponder())
    #pdbg.state(self.objc_instance)
    
    #presentViewController_animated_completion_

    #sfSafariViewController.release()
    #pdbg.state(sfvc.view())
    
    #self.objc_instance.nextResponder().presentViewController_animated_completion_(sfvc,True, None)
    sfvc.release()
    
  def will_close(self):
    self.httpd.shutdown()
    print('close')


if __name__ == '__main__':
  view = View()
  view.run()


