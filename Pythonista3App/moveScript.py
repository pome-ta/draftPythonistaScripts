from pathlib import Path
import shutil
import sys


def get_pythonista_modules_path(sys_paths: list[str]) -> str:
  _mp, *_ = [_sp for _sp in sys_paths if _sp.endswith('pythonista')]
  return _mp


pythonista_modules_path = get_pythonista_modules_path(sys.path)

