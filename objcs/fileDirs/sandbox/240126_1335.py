import re
import webbrowser
from objc_util import ObjCClass

root_path_str = str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath())


prog = re.compile(r'\s')
root_path_list = root_path_str.split('/')
root_path_match = '/'.join([rf'"{p}"' if  prog.search(p) else p for p in root_path_list])

webbrowser.open('pythonista3:/' + '/..' * 9 + f'{root_path_match}/')

'''
target = 'Library'
index = obj_path.find(target)
path = obj_path[:index + len(target)]

#webbrowser.open('pythonista3:/' + '/..' * 9 + f'{path}')
webbrowser.open(r'pythonista3:/' + '/..' * 9 + rf'{obj_path}')
'''

