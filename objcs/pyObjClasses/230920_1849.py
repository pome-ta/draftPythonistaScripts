# [https://github.com/tdamdouni/Pythonista/blob/master/objc/objc-get-names.py](https://github.com/tdamdouni/Pythonista/blob/master/objc/objc-get-names.py)

# coding: utf-8

# https://forum.omz-software.com/topic/2808/bug-objc_util-and-dir
from pprint import pprint
from objc_util import ObjCClass

class_names = ObjCClass.get_names('OM')
class_names.sort()

pprint(class_names)

#print('\n'.join(ObjCClass.get_names('OM')))

