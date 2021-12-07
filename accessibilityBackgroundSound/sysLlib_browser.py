# Pythonista で、i(Pad)OS のlibrary(？) を表示

import webbrowser
import os

webbrowser.open('pythonista3:/' + '/..' * os.getcwd().count('/') + '/System/Library')

