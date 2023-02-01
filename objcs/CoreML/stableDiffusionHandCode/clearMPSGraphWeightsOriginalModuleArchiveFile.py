import os
from shutil import rmtree
from pathlib import Path

from objc_util import ObjCClass

PA2UITheme = ObjCClass('PA2UITheme')
theme_dict = PA2UITheme.sharedTheme().userThemesPath()
theme_path = Path(str(theme_dict))
abs_path = theme_path.resolve()

# xxx: ハードコードすぎるからなんとかしたい
'''
root = os.path.expanduser(
  f'/{abs_path}/../../../tmp/com.apple.MetalPerformanceShadersGraph')
'''

root = os.path.expanduser(
  f'/{abs_path}/../../../tmp/')
rmtree(root)

