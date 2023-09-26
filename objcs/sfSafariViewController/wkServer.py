# coding: utf-8

# https://gist.github.com/omz/b39519b877c07dbc69f8 
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from objc_util import ObjCClass, ObjCInstance, on_main_thread, create_objc_class, sel, nsurl
from objc_util import UIApplication, UIImage

WKWebView = ObjCClass('WKWebView')
UIViewController = ObjCClass('UIViewController')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
NSURLRequest = ObjCClass('NSURLRequest')

os.chdir(os.path.join(os.path.dirname(__file__), 'public'))
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)


@on_main_thread
def main(url):
  app = UIApplication.sharedApplication()
  rootVC = app.keyWindow().rootViewController()
  tabVC = rootVC.detailViewController()
  methods = [goBack, goForward]
  protocols = ['OMTabContent']
  CustomViewController = create_objc_class(
    'CustomViewController',
    UIViewController,
    methods=methods,
    protocols=protocols)
  vc = CustomViewController.new().autorelease()
  vc.title = 'wkwebview'

  back_item = UIBarButtonItem.alloc().initWithImage_style_target_action_(
    UIImage.imageNamed_('Back'), 0, vc, sel('goBack'))
  fw_item = UIBarButtonItem.alloc().initWithImage_style_target_action_(
    UIImage.imageNamed_('Forward'), 0, vc, sel('goForward'))

  vc.navigationItem().rightBarButtonItems = [fw_item, back_item]
  webView = WKWebView.new().autorelease()
  request_path = NSURLRequest.requestWithURL_(nsurl(url))
  webView.loadRequest_(request_path)
  vc.view = webView
  tabVC.addTabWithViewController_(vc)


def goBack(_self, _cmd):
  view = ObjCInstance(_self).view()
  view.goBack()


def goForward(_self, _cmd):
  view = ObjCInstance(_self).view()
  view.goForward()


if __name__ == '__main__':
  main('http://localhost:8000/')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.shutdown()
    print('Server stopped')


