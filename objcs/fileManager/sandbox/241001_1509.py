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

attributes_array = [
  NSFileManager.defaultManager().attributesOfItemAtPath_error_(
    str(sound_path), None) for sound_path in all_files
]
'''
fileModificationDate_array = [
  attributes.fileModificationDate() for attributes in attributes_array
]
set_array = set(fileModificationDate_array)
'''

fileCreationDate_array = [
  attributes.fileCreationDate() for attributes in attributes_array
]
set_array = set(fileCreationDate_array)

