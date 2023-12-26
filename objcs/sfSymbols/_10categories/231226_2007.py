from pathlib import Path
import plistlib

CoreGlyphs_ROOT = '/System/Library/CoreServices/CoreGlyphs.bundle/'

IGNORE_SUFFIXS = [
  '.car',
]
IGNORE_NAMES = [
  'Info.plist',
]


class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self


def get_plistdata(path: Path | str) -> list | dict:
  _data_path = Path(path) if type(path) == 'str' else path
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def is_ignore(path: Path) -> bool:
  return not path.is_file()\
    or path.suffix in IGNORE_SUFFIXS\
    or path.name in IGNORE_NAMES


paths = {
  bundle.stem: get_plistdata(bundle)
  for bundle in Path(CoreGlyphs_ROOT).iterdir() if not is_ignore(bundle)
}

bundles = DictDotNotation(paths)

print(bundles.categories)

