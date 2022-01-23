import pathlib

from objc_util import ObjCClass, on_main_thread, nsurl
import ui

import pdbg


uri = pathlib.Path('./public/index.html')

NSURLRequest = ObjCClass('NSURLRequest')

WKWebView = ObjCClass('WKWebView')
WKWebViewConfiguration = ObjCClass('WKWebViewConfiguration')


class WkWeb(ui.View):
  #@on_main_thread
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    
    self.wkwebview = WKWebView.alloc()
    self.wwvconf = WKWebViewConfiguration.new()
    self.loadView()
    self.viewDidLoad()
    #self.wkwebview.reload()
    #pdbg.state(self.wkwebview)
    self.objc_instance.addSubview_(self.wkwebview)

  @on_main_thread
  def loadView(self):
    _frame = ((0.0, 0.0), (100.0, 100.0))
    self.wwvconf.preferences().setValue_forKey_(True, 'allowFileAccessFromFileURLs')
    self.wkwebview.initWithFrame_configuration_(_frame, self.wwvconf).autorelease()
    self.wkwebview.setAutoresizingMask_((1 << 1) | (1 << 4))

  @on_main_thread
  def viewDidLoad(self):
    #myURL = nsurl('https://www.apple.com')
    #myURL = nsurl('http://localhost:8000/')
    url = 'file://' + str(uri.resolve()).replace(' ', '%20')
    #myURL = nsurl(str(url))
    myURL = nsurl(str(uri))
    req = NSURLRequest.requestWithURL_(myURL)
    #iniReq = NSURLRequest.alloc().initWithURL_(myURL)
    
    #iniReq = NSURLRequest.alloc().initWithURL_cachePolicy_timeoutInterval_(myURL, 0, 100)
    
    
    
    #initWithURL:cachePolicy:timeoutInterval:
    #pdbg.state(iniReq)
    #req = NSURLRequest.requestWithURL_cachePolicy_timeoutInterval_(myURL, 0, 10)
    self.wkwebview.loadRequest_(req)
    #self.wkwebview.loadRequest_(iniReq)
    #pdbg.state(self.wkwebview)
    


class View(ui.View):
  #@on_main_thread
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.wk = WkWeb()
    self.wk.flex = 'WH'
    self.add_subview(self.wk)
    self.wk.wkwebview.reload()
    self.reload_btn()
    
    
    #self.wk.wkwebview.reload()
    #self.wk.viewDidLoad()
  def reload_btn(self):
    self.close_btn = self.create_btn('iob:ios7_refresh_outline_32')
    self.close_btn.action = (lambda sender: self.reload())
    self.right_button_items = [self.close_btn]
    #self.add_subview(self.close_btn)

  def create_btn(self, icon):
    btn_icon = ui.Image.named(icon)
    return ui.ButtonItem(image=btn_icon)
    
  def reload(self):
    self.wk.wkwebview.reload()

  def will_close(self):
    self.wk.wkwebview.reload()
    self.remove_subview(self.wk)


if __name__ == '__main__':
  view = View()
  view.present(style='panel')
  #view.wk.wkwebview.reload()
  
  #pdbg.state(view.wk.wkwebview)
  #view.present()

