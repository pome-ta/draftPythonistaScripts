import pathlib
from objc_util import ObjCClass, on_main_thread
import ui

import pdbg

#import wkwebview

uri = pathlib.Path('./public/index.html')


class WebView(ui.View):

  def __init__(self):
    self.create_webview()

  @on_main_thread
  def create_webview(self):
    self.webview = ObjCClass('WKWebView').alloc().initWithFrame_(
      (0, 0, 100, 100))
    self.objc_instance.addSubview_(self.webview)


class View(ui.View):

  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.wv = wkwebview.WKWebView(delegate=MyWebViewDelegate())
    #self.wv = wkwebview.WKWebView()
    self.wv = WebView()
    #self.present(style='fullscreen', orientations=['portrait'])
    url = 'file://' + str(uri.resolve()).replace(' ', '%20')
    #self.wv.load_url(url)
    #self.wv.load_url(uri.resolve())
    pdbg.state(self.wv)
    self.wv.flex = 'WH'
    self.add_subview(self.wv)

  def will_close(self):
    #self.wv.clear_cache()
    pass


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.wv.clear_cache()

