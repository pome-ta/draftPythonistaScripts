from pathlib import Path
import shutil
import sys

parent_name = 'pythonista'


def get_pythonista_modules_path(sys_paths: list[str]) -> str:
  _mp, *_ = [_sp for _sp in sys_paths if _sp.endswith(parent_name)]
  return _mp


def move_items(from_path: str, to_path: str) -> None:
  shutil.copytree(from_path, to_path)


if __name__ == '__main__':
  pass2dir_name = 'modulesMaster'

  pythonista_modules_path = get_pythonista_modules_path(sys.path)

  root = Path.cwd()
  to_target = Path(root, pass2dir_name, parent_name)
  target_path = str(to_target)
  move_items(pythonista_modules_path, target_path)

