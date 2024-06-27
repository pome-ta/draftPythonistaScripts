from pathlib import Path
import webbrowser


def parent_level(level_int):
  return '../' * level_int


origin_path = Path()

level = 9
f_path = Path('System/Library/')
target_url = origin_path / parent_level(level) / f_path

webbrowser.open(f'pythonista3://{target_url}')

