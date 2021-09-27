import webbrowser
import os

webbrowser.open('pythonista3:/' + '/..' * os.getcwd().count('/') + '/System/Library')

