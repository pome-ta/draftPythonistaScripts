import pathlib

from objc_util import ObjCClass, on_main_thread, nsurl
import ui

import pdbg


uri = pathlib.Path('./public/index.html')

NSURLRequest = ObjCClass('NSURLRequest')

WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')


class WkWeb:
  #@on_main_thread
  def __init__(self):
    self.wkwebview = WKWebView.alloc()
    self.wwvconf = WKWebViewConfiguration.new()
    self.loadView()
    self.viewDidLoad()
    #pdbg.state(self.wkwebview)

  @on_main_thread
  def loadView(self):
    _frame = ((0.0, 0.0), (100.0, 100.0))
    self.wkwebview.initWithFrame_configuration_(_frame, self.wwvconf)
    self.wkwebview.setAutoresizingMask_((1 << 1) | (1 << 4))

  @on_main_thread
  def viewDidLoad(self):
    #myURL = nsurl('https://www.apple.com')
    #myURL = nsurl('http://localhost:8000/')
    url = 'file://' + str(uri.resolve()).replace(' ', '%20')
    myURL = nsurl(str(url))
    req = NSURLRequest.requestWithURL_(myURL)
    #req = NSURLRequest.requestWithURL_cachePolicy_timeoutInterval_(myURL, 0, 10)
    self.wkwebview.loadRequest_(req)
    


class View(ui.View):
  #@on_main_thread
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.wk = WkWeb()
    self.objc_instance.addSubview_(self.wk.wkwebview)
    #self.wk.viewDidLoad()
    '''
    self.web = ui.WebView()
    url = 'file://' + str(uri.resolve()).replace(' ', '%20')
    self.web.load_url(url)
    self.web.flex = 'WH'
    self.add_subview(self.web)
    '''

  def will_close(self):
    pass


if __name__ == '__main__':
  view = View()
  view.present(style='panel')
  #view.present()

