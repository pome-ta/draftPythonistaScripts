import os

from objc_util import ObjCClass, UIApplication, on_main_thread, nsurl

from http.server import HTTPServer, SimpleHTTPRequestHandler



os.chdir(os.path.join(os.path.dirname(__file__), 'public'))



class RequestHandler(SimpleHTTPRequestHandler, object):
  def print_info(self):
    #self.log_message("%s %s\n%s", self.command, self.path, self.headers)
    pass

  def do_GET(self):
    #self.print_info()
    super(RequestHandler, self).do_GET()

  def do_POST(self):
    self.do_GET()


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)


SFSafariViewController = ObjCClass('SFSafariViewController')


@on_main_thread
def open_in_safari_vc(url):
  #pdbg.state(nsurl(url))
  #vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))
  vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))

  app = UIApplication.sharedApplication()
  root_vc = app.keyWindow().rootViewController()
  root_vc.presentViewController_animated_completion_(vc, True, None)
  vc.release()
  print(vc)


if __name__ == '__main__':
  
  open_in_safari_vc('http://localhost:8000/')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.shutdown()
    print('Server stopped')


