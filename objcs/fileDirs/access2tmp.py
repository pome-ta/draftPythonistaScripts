import webbrowser
from objc_util import ObjCClass
import pdbg

NSFileManager = ObjCClass('NSFileManager')


def get_temporaryDirectory_path() -> str:
  nsFileManager = NSFileManager.new()
  # todo: `file://` で取得してしまうため、`uri` 呼び出し
  temp_dir = nsFileManager.temporaryDirectory().uri()
  return str(temp_dir)  # todo: 文字列キャスト


def get_toplevel_path(up_level: int=9) -> str:
  origin_path = './'
  parent_level = lambda l: '../' * int(l)
  return origin_path + parent_level(up_level)


if __name__ == '__main__':
  path = get_toplevel_path() + get_temporaryDirectory_path()
  webbrowser.open(f'pythonista3://{path}')
