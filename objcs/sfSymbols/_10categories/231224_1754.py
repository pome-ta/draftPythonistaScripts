from pathlib import Path
import plistlib


def get_data(path: Path | str) -> list | dict:
  _data_path = Path(path)
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def copy_write_data(path: Path | str, base_path: str = 'CoreGlyphs') -> None:
  if not (path.is_file() and path.suffix == '.car'):
    return
  print(path.name)


CoreGlyphs_root = '/System/Library/CoreServices/CoreGlyphs.bundle/'

root_path = Path(CoreGlyphs_root)
bundles = list(root_path.iterdir())

for bundle in bundles:

  print(i.name)

  if i.is_file():
    try:
      get_data(i)
    except:
      pass
  print(i.is_file())
  print('')

