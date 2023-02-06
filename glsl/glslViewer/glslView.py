import sys
from pathlib import Path

import ui
import editor

sys.path.append(str(Path.cwd()) + '/pythonista-webview')
from wkwebview import WKWebView


def set_shader_code(source_code: str) -> str:
  _code = f'window.shader_code = () => `{source_code}`;'
  _code = f'''const source_code = document.createTextNode(`{source_code}`)
  const _node = document.querySelector(`#shaderCode`);
  _node.appendChild(source_code);
  
  '''

  return _code


class View(ui.View):
  def __init__(self, index_url: str, shader_str: str, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.wv = WKWebView()
    self.wv.load_url(str(index_url))
    self.wv.shader_source_code = shader_str
    self.wv.delegate = MyWebViewDelegate()

    self.wv.flex = 'WH'
    self.add_subview(self.wv)

    
    self.wv.clear_cache()
    # self.wv.add_script(set_shader_code(shader_str))
    #self.wv.eval_js('wktest()')

  def will_close(self):
    self.wv.reload()


class MyWebViewDelegate:
  def webview_should_start_load(self, webview, url, nav_type):
    """
    See nav_type options at
    https://developer.apple.com/documentation/webkit/wknavigationtype?language=objc
    """
    # print('Will start loading', url)
    return True

  def webview_did_start_load(self, webview):
    # print('Started loading')
    pass

  @ui.in_background
  def webview_did_finish_load(self, webview):
    js_code = f'let hoge = `{webview.shader_source_code}`'
    #print('Finished loading ' + str(webview.eval_js('document.title')))
    # self.wv.eval_js_async
    #pdbg.state(webview)
    #webview.eval_js(js_code)
    #webview.eval_js_async(js_code)
    #print(dir(webview))
    #webview.add_script(js_code)
    print(webview.eval_js('add(1,2)'))
    #webview.eval_js_async('wktest()')
    


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

