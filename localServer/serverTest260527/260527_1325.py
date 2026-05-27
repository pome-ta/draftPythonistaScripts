from http.server import HTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import threading


class RequestHandler(SimpleHTTPRequestHandler):

  def do_GET(self):
    print('request:', self.path)
    super().do_GET()


class LocalServer:

  def __init__(self, host='127.0.0.1', port=8000, root_dir='.'):
    # 変更: root_dir を絶対パスに正規化(cwd依存排除)
    root_path = Path(root_dir).resolve()

    # 変更: handler に directory を固定
    #handler = partial(SimpleHTTPRequestHandler, directory=str(root_path))
    handler = partial(RequestHandler, directory=str(root_path))

    self.server = HTTPServer((host, port), handler)
    self.thread = None

  def start(self):
    # 変更: スレッドで非ブロッキング起動
    self.thread = threading.Thread(target=self.server.serve_forever)
    self.thread.daemon = True
    self.thread.start()

  def stop(self):
    # 変更: 安全停止シーケンス
    self.server.shutdown()
    self.server.server_close()
    if self.thread:
      self.thread.join()


if __name__ == '__main__':
  # 例: 一つ上の public を指定(../ もOK)
  #server = LocalServer(root_dir='../public')
  server = LocalServer(root_dir='./')

  server.start()
  #print('started: http://127.0.0.1:8000')
  print('started: http://localhost:8000')

  import time
  #time.sleep(5)

  #server.stop()
  print('stopped')

