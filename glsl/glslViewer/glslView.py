import sys
from pathlib import Path

import ui
import editor

sys.path.append(str(Path.cwd()) + '/pythonista-webview')
from wkwebview import WKWebView


class View(ui.View):
  def __init__(self, index_url: str, shader_str: str, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.wv = WKWebView()
    self.wv.flex = 'WH'
    self.add_subview(self.wv)

    self.wv.load_url(str(index_url))
    self.wv.clear_cache()

  def will_close(self):
    self.wv.reload()


def get_shader_name_code() -> list:
  # todo: `editor.get_path()` するところ
  _uri = str(Path('./testFragmentCode.js').resolve())
  _path = Path(_uri)
  _name = _path.name
  _code = _path.read_text(encoding='utf-8')
  return [_name, _code]


if __name__ == '__main__':
  index_path = Path('./src/index.html')
  shader_name, shader_code = get_shader_name_code()

  view = View(index_url=index_path, shader_str=shader_code, name=shader_name)
  view.present(style='fullscreen', orientations=['portrait'])

