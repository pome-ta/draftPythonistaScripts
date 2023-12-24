from pathlib import Path
import plistlib


def get_data(path: str) -> list | dict:
  _data_path = Path(path)
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


CoreGlyphs_root = '/System/Library/CoreServices/CoreGlyphs.bundle/'

root_path = Path(CoreGlyphs_root)
bundles = list(root_path.iterdir())

for i in bundles:
  print(i.name)

  if i.is_file():

    get_data(i)
  print(i.is_file())
  print('')

