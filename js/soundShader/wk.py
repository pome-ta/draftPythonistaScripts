from objc_util import ObjCClass, on_main_thread, nsurl
import ui

import pdbg

NSURLRequest = ObjCClass('NSURLRequest')

WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')


class WkWeb:
  def __init__(self):
    self.wkwebview = WKWebView.alloc()
    self.wwvconf = WKWebViewConfiguration.new()
    self.loadView()
    self.viewDidLoad()

  @on_main_thread
  def loadView(self):
    _frame = ((0.0, 0.0), (100.0, 100.0))
    self.wkwebview.initWithFrame_configuration_(_frame, self.wwvconf)
    self.wkwebview.setAutoresizingMask_((1 << 1) | (1 << 4))

  @on_main_thread
  def viewDidLoad(self):
    #myURL = nsurl('https://www.apple.com')
    myURL = nsurl('https://qiita.com/syunyo/items/d03a714af4dadd0727a6')
    req = NSURLRequest.requestWithURL_(myURL)
    self.wkwebview.loadRequest_(req)


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.wk = WkWeb()
    self.objc_instance.addSubview_(self.wk.wkwebview)


if __name__ == '__main__':
  view = View()
  view.present(style='panel')

