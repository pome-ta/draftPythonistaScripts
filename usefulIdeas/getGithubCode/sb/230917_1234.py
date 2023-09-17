import requests
import json
import clipboard

url = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py'

split_url = url.split('/')

boolen = True if ('github.com' in split_url
                  and '.' in split_url[-1]) else False

boolen = ('github.com' in split_url and '.' in split_url[-1])

parm = '?raw=true'

_ = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py'  #?rawLines'

#url = 'https://github.com/tdamdouni/Pythonista/blob/master/objc/ObjCUtil.py?raw=true'

b = url.split('/')

res = requests.get(url)
code_raw = res.text

