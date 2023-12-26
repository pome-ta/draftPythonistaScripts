from pathlib import Path
import plistlib

CoreGlyphs_ROOT = '/System/Library/CoreServices/CoreGlyphs.bundle/'

CoreGlyphs_names: dict = {}
CoreGlyphs_path: dict = {}

pickup_plists = [
  'categories.plist',
  'symbol_categories.plist',
  'symbol_search.plist',
]


class DictDotNotation(dict):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__dict__ = self


#paths = [bundle.name for bundle in Path(CoreGlyphs_ROOT).iterdir() if bundle.is_file() and bundle.suffix != '.car']
ignore_suffix = [
  '.car',
]

ignore_name = [
  'Info.plist',
]


def get_data(path: Path | str) -> list | dict:
  _data_path = Path(path) if type(path) == 'str' else path
  _loads = plistlib.loads(_data_path.read_bytes())
  return _loads


def is_ignore(path: Path) -> bool:
  return not path.is_file() or (path.suffix
                                in ignore_suffix) or (path.name in ignore_name)


paths = {
  bundle.stem: get_data(bundle)
  for bundle in Path(CoreGlyphs_ROOT).iterdir() if not is_ignore(bundle)
}

bundles = DictDotNotation(paths)

print(bundles.categories)

