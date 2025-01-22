'''
print(__name__)
print(__file__)
print(__cached__)
'''
from pprint import pprint
import os
import sys

#pprint(os.environ)
environ = os.environ

for e in environ:
  print(f'{e}: {environ[e]}\n')
