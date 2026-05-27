import threading
import time
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


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
    return f"http://{self.host}:{self.port}"


if __name__ == '__main__':
  # verbose=False に設定することで、コンソールへのリクエストログを完全に消音できる
  with LocalServer(host='127.0.0.1', port=8000, root_dir='./docs',
                   verbose=False) as server:
    print(f'started: {server.url}')

    time.sleep(5)

  print('stopped')

