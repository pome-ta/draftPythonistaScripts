
import pathlib
import ui

import wkwebview

uri = pathlib.Path('./public/index.html')
print(uri.resolve())


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.wv = wkwebview.WKWebView(delegate=MyWebViewDelegate())
    self.wv = wkwebview.WKWebView()
    #self.present(style='fullscreen', orientations=['portrait'])
    url = 'file://' + str(uri.resolve()).replace(' ', '%20')
    self.wv.load_url(url)
    self.wv.flex = 'WH'
    self.add_subview(self.wv)
    
  
  def will_close(self):
    self.wv.clear_cache()


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])
  #view.wv.clear_cache()

