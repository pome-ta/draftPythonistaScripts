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

