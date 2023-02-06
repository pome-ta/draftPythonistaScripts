import sys
from pathlib import Path

import ui
import editor

sys.path.append(str(Path.cwd()) + '/pythonista-webview')
from wkwebview import WKWebView


class View(ui.View):
  def __init__(self, index_url: str, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.wv = WKWebView()

    self.wv.load_url(str(index_url))
    self.wv.flex = 'WH'
    self.add_subview(self.wv)
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


def rewrite_index(index_uri: Path, shader_source_code: str) -> Path:
  _base_text = index_uri.read_text()
  _top, _end = _base_text.split('<body></body>')
  _insertion_text = f'''
  <body>
    <textarea id="shaderCode" style="display: none;">{shader_source_code}</textarea>
  </body>'''

  _build_text = _top + _insertion_text + _end
  build_file = Path(index_uri.parent, '_build.html')
  build_file.write_text(_build_text, encoding='utf-8')
  return build_file


if __name__ == '__main__':
  index_path = Path('./src/index.html')

  shader_name, shader_code = get_shader_name_code()
  build_path = rewrite_index(index_path, shader_code)

  view = View(index_url=build_path, name=shader_name)
  view.present(style='fullscreen', orientations=['portrait'])

