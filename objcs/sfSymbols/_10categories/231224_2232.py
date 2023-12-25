from pathlib import Path
import plistlib

CoreGlyphs_ROOT = '/System/Library/CoreServices/CoreGlyphs.bundle/'
HOME_PATH = Path().cwd()
ROOT_PATH = Path(CoreGlyphs_ROOT)

def get_data(path: Path | str) -> list | dict:
  _data_path = Path(path)
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def copy_write_data(path: Path, base_path: str = 'CoreGlyphs') -> None:
  if not (path.is_file() and path.suffix != '.car'):
    return
  print(path.name)





if __name__ == '__main__':
  target_parent = 'CoreGlyphs'
  parent_path = Path(target_parent)
  if parent_path.exists():
    print('ok')
  bundles = list(ROOT_PATH.iterdir())
  
  for bundle in bundles:
    copy_write_data(bundle)
