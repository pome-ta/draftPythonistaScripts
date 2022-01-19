import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pathlib
import ui
#sys.path.append(str(pathlib.Path.cwd())
import wkwebview


os.chdir(os.path.join(os.path.dirname(__file__), 'public'))
uri = pathlib.Path('./index.html')

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)


class MyWebViewDelegate:
  def webview_should_start_load(self, webview, url, nav_type):
    """
    See nav_type options at
    https://developer.apple.com/documentation/webkit/wknavigationtype?language=objc
    """
    print('Will start loading', url)
    return True

  def webview_did_start_load(self, webview):
    #print('Started loading')
    pass

  @ui.in_background
  def webview_did_finish_load(self, webview):
    #str(webview.eval_js('document.title'))
    print('Finished loading ' + str(webview.eval_js('document.title')))
    #pass


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.wv = wkwebview.WKWebView(delegate=MyWebViewDelegate())
    self.wv = wkwebview.WKWebView()
    #self.present(style='fullscreen', orientations=['portrait'])

    #self.wv.load_url(str(uri), True)
    #self.wv.load_url('http://localhost:8000/')
    
    self.wv.flex = 'WH'
    self.add_subview(self.wv)
  '''
  def layout(self):
    self.wv.width = self.width
    self.wv.height = self.height
    #self.wv.flex = 'WH'
  '''

  def will_close(self):
    self.wv.clear_cache()
    httpd.shutdown()


if __name__ == '__main__':
  view = View()
  view.present(style='panel', orientations=['portrait'])
  #view.wv.clear_cache()
  
  try:
    view.wv.load_url('http://localhost:8000/')
    httpd.serve_forever()
    
  except KeyboardInterrupt:
    httpd.shutdown()
    print('Server stopped')
  


