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

from objc_frameworks.UIKit import UIModalPresentationStyle

from rbedge.lifeCycle import loop
from rbedge.objcMainThread import onMainThread
from rbedge.utils import nsurl

SFSafariViewController = ObjCClass('SFSafariViewController')
UIApplication = ObjCClass('UIApplication')
NSURL = ObjCClass('NSURL')


def get_rootViewController() -> None:
  sharedApplication = UIApplication.sharedApplication
  objectEnumerator = sharedApplication.connectedScenes.objectEnumerator()

  while (windowScene := objectEnumerator.nextObject()):

    if windowScene.activationState == 0:
      break
  rootViewController = windowScene.keyWindow.rootViewController
  return rootViewController


def main_loop() -> None:
  try:
    loop.run_forever()
  except Exception as e:
    loop.stop()
  finally:
    loop.close()


def main(url, modalPresentationStyle):

  rootViewController = get_rootViewController()

  @onMainThread(sync=True)
  def present_viewController(url, style: int) -> None:

    presentViewController = SFSafariViewController.alloc().initWithURL_(nsurl(url))
    #presentViewController = SFSafariViewController.alloc().initWithURL_(url)
    presentViewController.setModalPresentationStyle_(style)

    rootViewController.presentViewController(
      presentViewController,
      animated=True,
      completion=None,
    )
    #rootViewController.release()

  present_viewController(url, modalPresentationStyle)
  main_loop()


if __name__ == '__main__':
  import threading
  from functools import partial
  from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
  from pathlib import Path

  from rbedge.app import App
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
    presentation_style = UIModalPresentationStyle.fullScreen
  
    main(server.url, presentation_style)

