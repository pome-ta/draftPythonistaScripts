import os
import webbrowser
from pathlib import Path

from objc_util import ObjCInstance, ObjCClass


def get_target_root():

  PA2UITheme = ObjCClass('PA2UITheme')
  theme_dict = PA2UITheme.sharedTheme().userThemesPath()
  theme_path = Path(str(theme_dict))
  abs_path = theme_path.resolve()
  #root = os.path.expanduser(f'/{abs_path}/../../../tmp')
  root = os.path.expanduser(f'/{abs_path}/../../../')
  return root


def parent_level(level_int):
  return '../' * level_int


root = get_target_root()
origin_path = './'

level = 9
target_url = origin_path + parent_level(level)

_root = str(Path(root).resolve())

_url = str(target_url) + _root
url = f'pythonista3://{_url}'
webbrowser.open(url)
