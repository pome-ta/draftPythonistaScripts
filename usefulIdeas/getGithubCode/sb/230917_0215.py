import requests
import clipboard

url = 'https://raw.githubusercontent.com/tdamdouni/Pythonista/master/objc/ObjCUtil.py'

res = requests.get(url)
code_raw = res.text

print(code_raw)
clipboard.set(code_raw)

