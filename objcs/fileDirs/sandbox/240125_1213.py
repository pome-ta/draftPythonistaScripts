from pathlib import Path
from datetime import datetime
import webbrowser
from objc_util import ObjCClass
from pprint import pprint

NSFileManager = ObjCClass('NSFileManager')


def get_temporaryDirectory_path() -> str:
  nsFileManager = NSFileManager.new()
  # todo: `file://` で取得してしまうため、`uri` 呼び出し
  temp_dir = nsFileManager.temporaryDirectory().uri()
  return str(temp_dir)


def get_toplevel_path(up_level: int = 9) -> str:
  origin_path = './'
  parent_level = lambda l: '../' * int(l)
  return origin_path + parent_level(up_level)


if __name__ == '__main__':
  # todo: 1番上まで戻り、tmp ディレクトリへ
  path = get_temporaryDirectory_path()
  tmp_path = Path(path)

  #webbrowser.open(f'pythonista3://{path}')

  tmp_list = list(tmp_path.iterdir())

  for i in tmp_list:
    print(i.name)

    #pprint(f' {datetime.fromtimestamp(i.stat())}')
    stat_result = i.stat()
    #st_mtime=1691897088
    print(f' {datetime.fromtimestamp(stat_result.st_mtime)}')
    for j in i.iterdir():
      print(f'  {j.name}')

