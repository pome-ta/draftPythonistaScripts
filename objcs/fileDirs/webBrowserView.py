from objc_util import ObjCClass
import os
from pathlib import Path
import webbrowser

uri_path = ObjCClass('NSBundle').mainBundle().resourcePath()

#webbrowser.open('pythonista3:/' + '/..' * os.getcwd().count('/') + str(uri_path))
#webbrowser.open('pythonista3://../..')
PA2UITheme = ObjCClass('PA2UITheme')

theme_dict = PA2UITheme.sharedTheme().userThemesPath()
theme_dict_path = str(theme_dict) + '/..'

webbrowser.open('pythonista3:' + theme_dict_path)
