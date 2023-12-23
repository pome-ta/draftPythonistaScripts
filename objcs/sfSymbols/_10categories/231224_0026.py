from pathlib import Path
import plistlib


CoreGlyphs_path = '/System/Library/CoreServices/CoreGlyphs.bundle/'

coreGlyphs = Path(CoreGlyphs_path)

for i in coreGlyphs.iterdir():
  print(i)
  print('')
