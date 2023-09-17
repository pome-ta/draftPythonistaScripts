import requests
import json
import clipboard

url = 'https://raw.githubusercontent.com/tdamdouni/Pythonista/master/objc/ObjCUtil.py'


_ = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py'#?rawLines'


res = requests.get(_)
code_raw = res.text
j = json.loads(code_raw)

a=j['payload']['blob']['displayUrl']
print(a)

from pprint import pprint
#pprint(code_raw)
#clipboard.set(code_raw)

