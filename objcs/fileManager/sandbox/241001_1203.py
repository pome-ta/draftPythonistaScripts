"""
note: file のmeta 情報
"""

from pathlib import Path

from objc_util import ObjCClass
import pdbg

NSFileManager = ObjCClass('NSFileManager')

#attributesOfItemAtPath_error_
#attributesOfItemAtPath_error_
#pdbg.state(NSFileManager.defaultManager())

root_str = '/System/Library/Audio/UISounds/'
root_path = Path(root_str)

all_files = list(root_path.glob('**/*.*'))
'''
sound_path = all_files[0]
attributes = NSFileManager.defaultManager().attributesOfItemAtPath_error_(str(sound_path), None)
'''
'''
for sound_path in all_files:
  attributes = NSFileManager.defaultManager().attributesOfItemAtPath_error_(
    str(sound_path), None)
'''

attributes = [
  NSFileManager.defaultManager().attributesOfItemAtPath_error_(
    str(sound_path), None) for sound_path in all_files
]

