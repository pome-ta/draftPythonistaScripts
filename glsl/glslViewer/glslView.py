import sys
from pathlib import Path

import ui
import editor

sys.path.append(str(Path.cwd()) + '/pythonista-webview')
from wkwebview import WKWebView

# toto: title も持ってくる


class View(ui.View):
  def __init__(self, index_html, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.wv = WKWebView()
    self.wv.flex = 'WH'
    self.add_subview(self.wv)
    
    self.wv.load_url(str(index_html))


if __name__ == '__main__':
  index_path = Path('./src/index.html')

  view = View(index_path)
  view.present(style='fullscreen', orientations=['portrait'])

