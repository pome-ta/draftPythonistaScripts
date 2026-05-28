import threading
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

    class CustomHandler(SimpleHTTPRequestHandler):

      def log_message(handler_self, format: str, *args) -> None:
        # verboseがTrueの時だけ元のログ出力処理を呼ぶ
        if self.verbose:
          super().log_message(format, *args)

      def end_headers(handler_self) -> None:
        # HTML/JS/CSS開発に必須のキャッシュ完全無効化ヘッダー
        handler_self.send_header(
          'Cache-Control',
          'no-cache, no-store, must-revalidate',
        )
        handler_self.send_header('Pragma', 'no-cache')
        handler_self.send_header('Expires', '0')
        super().end_headers()

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

