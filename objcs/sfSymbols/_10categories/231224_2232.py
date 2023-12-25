from pathlib import Path
import plistlib
import json

CoreGlyphs_ROOT = '/System/Library/CoreServices/CoreGlyphs.bundle/'
HOME_PATH = Path().cwd()
ROOT_PATH = Path(CoreGlyphs_ROOT)


def get_data(path: Path | str) -> list | dict:
  _data_path = Path(path)
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def copy_write_data(path: Path, base_path: Path) -> None:
  if not (path.is_file() and path.suffix != '.car'):
    return
  print(path.name)

  file_data = None

  try:
    file_data = json.dumps(get_data(path), ensure_ascii=False, indent=2)

  except:
    pass

  if not file_data:
    return
  file_name = path.name
  new_file_path = Path(base_path, file_name)
  #new_file_path.write_text(file_data, encoding='utf-8')


if __name__ == '__main__':
  target_parent = 'CoreGlyphs'
  parent_path = Path(target_parent)
  None if parent_path.exists() else parent_path.mkdir()

  for bundle in ROOT_PATH.iterdir():
    copy_write_data(bundle, parent_path)

