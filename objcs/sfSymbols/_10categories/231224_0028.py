from pathlib import Path
import webbrowser

import editor


def get_toplevel_path(up_level: int=9) -> str:
  origin_path = './'
  parent_level = lambda l: '../' * int(l)
  return origin_path + parent_level(up_level)

CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphs_dir = Path(get_toplevel_path(),CoreGlyphs_path)
#webbrowser.open(f'pythonista3:/{coreGlyphs_dir}')

#coreGlyphs_dir = Path(CoreGlyphs_path, 'name_aliases.strings')

#editor.open_file(coreGlyphs_dir.resolve())

#print(coreGlyphs_dir.resolve())
coreGlyphs_dir  = Path(CoreGlyphs_path)
for i in coreGlyphs_dir.iterdir():
  #print(i)
  #print(i.read_text(encode='utf8'))
  print(i.read_bytes())
