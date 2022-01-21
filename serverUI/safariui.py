
from http.server import HTTPServer, SimpleHTTPRequestHandler

from objc_util import ObjCClass, UIApplication, on_main_thread, nsurl
import ui
import pdbg

myurl = 'https://ics.media/entry/16511/'

class Main(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    pdbg.state(self.objc_instance)

main = Main()
main.present()

'''
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)

SFSafariViewController = ObjCClass('SFSafariViewController')


@on_main_thread
def open_in_safari_vc(url):
  #pdbg.state(nsurl(url))
  #vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))
  vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))

  app = UIApplication.sharedApplication()
  root_vc = app.keyWindow().rootViewController()
  #vc.setModalPresentationStyle_(4)
  tab_vc = root_vc.detailViewController()

  #root_vc.presentViewController_animated_completion_(vc, True, None)
  
  tab_vc.addTabWithViewController_(vc)
  vc.release()


if __name__ == '__main__':

  open_in_safari_vc('http://localhost:8000/')
  import ui
  u = ui.View()
  u.present()
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.shutdown()
    print('Server stopped')
'''

