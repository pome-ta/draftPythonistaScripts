import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from objc_util import ObjCClass, UIApplication, on_main_thread, nsurl

import pdbg

os.chdir(os.path.join(os.path.dirname(__file__), 'public'))

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
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.shutdown()
    print('Server stopped')

