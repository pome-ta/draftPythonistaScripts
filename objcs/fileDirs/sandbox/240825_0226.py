import re
import webbrowser
from objc_util import ObjCClass

root_path_str = str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath())

'''
prog = re.compile(r'\s')
root_path_list = root_path_str.split('/')
root_path_match = '/'.join([rf'"{p}"' if  prog.search(p) else p for p in root_path_list])

webbrowser.open('pythonista3:/' + '/..' * 9 + f'{root_path_match}/')

'''
target = 'Library'
index = root_path_str.find(target)
path = root_path_str[:index + len(target)]
#/var/mobile/Containers/Data/Application/C8DAFCB2-8FD3-488A-ADBC-1AD0B09FD88A/Library

#/var/mobile/Containers/Data/Application/C8DAFCB2-8FD3-488A-ADBC-1AD0B09FD88A/Library/Application Support/Themes


#print(path)
#print(root_path_str)

url = '/var/mobile/Containers/Data/Application/C8DAFCB2-8FD3-488A-ADBC-1AD0B09FD88A/Library/Application%20Support'
#url = '/var/mobile/Containers/Data/Application/C8DAFCB2-8FD3-488A-ADBC-1AD0B09FD88A/Library/WebKit'

webbrowser.open('pythonista3:/' + '/..' * 9 + f'{url}')

#webbrowser.open('pythonista3:/' + '/..' * 9 + f'{path}')
#webbrowser.open(r'pythonista3:/' + '/..' * 9 + rf'{obj_path}')

