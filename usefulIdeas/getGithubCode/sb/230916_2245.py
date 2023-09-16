from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://raw.githubusercontent.com/tdamdouni/Pythonista/master/objc/ObjCUtil.py'

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

