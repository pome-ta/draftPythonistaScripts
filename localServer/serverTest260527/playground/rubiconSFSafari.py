_TOP_DIR_NAME = 'serverTest260527'
_MODULES_DIR_NAME = 'modules'

# todo: `./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME}` にあるpackage のimport 準備
if __name__ == '__main__' and not __file__[:__file__.rfind('/')].endswith(
    _TOP_DIR_NAME):
  import pathlib
  import sys
  __parents = pathlib.Path(__file__).resolve().parents
  for __dir_path in __parents:
    if __dir_path.name == _TOP_DIR_NAME and (__modules_path := __dir_path /
                                             _MODULES_DIR_NAME).exists():
      sys.path.insert(0, str(__modules_path))
      break
  else:
    import warnings
    with warnings.catch_warnings():
      warnings.simplefilter('always', ImportWarning)
      __warning_message = f'./{_TOP_DIR_NAME}/{_MODULES_DIR_NAME} not found in parent directories'
      warnings.warn(__warning_message, ImportWarning)

from pyrubicon.objc.api import ObjCClass
from pyrubicon.objc.api import objc_method
from pyrubicon.objc.runtime import send_super, objc_id, load_library

from rbedge.lifeCycle import loop
from rbedge import pdbr

load_library('SafariServices')

UINavigationController = ObjCClass('UINavigationController')
SFSafariViewController = ObjCClass('SFSafariViewController')


class NavigationController(UINavigationController):

  @objc_method
  def initWithRootViewController_(self, rootViewController):
    send_super(__class__,
               self,
               'initWithRootViewController:',
               rootViewController,
               argtypes=[
                 objc_id,
               ])

    self.setNavigationBarHidden_animated_(True, True)
    return self

  @objc_method
  def dealloc(self):
    # xxx: 呼ばない-> `send_super(__class__, self, 'dealloc')`
    loop.stop()

  @objc_method
  def didReceiveMemoryWarning(self):
    send_super(__class__, self, 'didReceiveMemoryWarning')
    print(f'{NSStringFromClass(__class__)}: didReceiveMemoryWarning')


if __name__ == '__main__':
  import threading
  from functools import partial
  from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
  from pathlib import Path

  from rbedge.app import App
  from rbedge.utils import nsurl
  from objc_frameworks.UIKit import UIModalPresentationStyle

  class LocalServer:

    def __init__(
      self,
      host: str = '127.0.0.1',
      port: int = 8000,
      root_dir: str | Path = '.',
      verbose: bool = False,
    ) -> None:
      self.host = host
      self.port = port
      self.root_path = Path(root_dir).resolve()
      self.verbose = verbose

      # 内部でハンドラーを定義し、ログ出力を制御する
      class CustomHandler(SimpleHTTPRequestHandler):

        def log_message(handler_self, format: str, *args) -> None:
          # verboseがTrueの時だけ元のログ出力処理を呼ぶ
          if self.verbose:
            super().log_message(format, *args)
          # Falseの時は何もせず破棄する(pass)

      # 拡張した CustomHandler を使うように変更
      handler = partial(CustomHandler, directory=str(self.root_path))

      self.server = ThreadingHTTPServer((self.host, self.port), handler)
      self._thread: threading.Thread | None = None

    def __enter__(self) -> 'LocalServer':
      self.start()
      return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
      self.stop()

    def start(self) -> None:
      if self._thread is not None and self._thread.is_alive():
        return

      self._thread = threading.Thread(
        target=self.server.serve_forever,
        daemon=True,
      )
      self._thread.start()

    def stop(self) -> None:
      self.server.shutdown()
      self.server.server_close()

      if self._thread is not None:
        self._thread.join()
        self._thread = None

    @property
    def url(self) -> str:
      return f'http://{self.host}:{self.port}'

  ROOT_PATH = Path(__file__).parents[0]
  index_path = ROOT_PATH / '../docs/'

  with LocalServer(
      host='127.0.0.1',
      port=8000,
      root_dir=str(index_path),
      verbose=False,
  ) as server:

    url = 'https://github.com/ColdGrub1384/Pyto'
    #url = server.url

    main_vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))

    presentation_style = UIModalPresentationStyle.fullScreen
    #presentation_style = UIModalPresentationStyle.pageSheet

    app = App(main_vc, presentation_style)
    app.present(NavigationController)

