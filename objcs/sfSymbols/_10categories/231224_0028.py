from pathlib import Path
import webbrowser


def get_toplevel_path(up_level: int=9) -> str:
  origin_path = './'
  parent_level = lambda l: '../' * int(l)
  return origin_path + parent_level(up_level)

CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphs_dir = Path(get_toplevel_path(),CoreGlyphs_path)

webbrowser.open(f'pythonista3://{coreGlyphs_dir}')
