import webbrowser
from objc_util import ObjCClass

obj_path = str(ObjCClass('PA2UITheme').sharedTheme().userThemesPath())
target = 'Library'
index = obj_path.find(target)
path = obj_path[:index]
print(path)

webbrowser.open('pythonista3:/' + '/..' * 9 + f'{path}')

