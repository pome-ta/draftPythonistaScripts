import requests
import json
import clipboard

url = 'https://raw.githubusercontent.com/tdamdouni/Pythonista/master/objc/ObjCUtil.py'


_ = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py'#?rawLines'


url = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py?raw=true'

b = url.split('/')

res = requests.get(url)
code_raw = res.text

