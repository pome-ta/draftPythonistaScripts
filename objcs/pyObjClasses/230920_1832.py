# [https://github.com/pome-ta/draftPythonistaScripts/blob/main/objcs/fileDirs/search.py](https://github.com/pome-ta/draftPythonistaScripts/blob/main/objcs/fileDirs/search.py)

import re
from pathlib import Path


def search_frameworks(word: str):
  p = re.compile(f'{word}', re.IGNORECASE)
  search_area = ['Frameworks', 'PrivateFrameworks']
  for area in search_area:
    _search_print(area, p)


def _search_print(path_name, compiler):
  path_str = f'/System/Library/{path_name}'
  search_path = Path(path_str)
  if not search_path.exists():
    print('ファイルがありません:終了します')
    return
  fw_list = sorted(list(search_path.iterdir()))
  result = [fw for fw in fw_list if compiler.search(fw.name)]
  print(f'--- {path_name} :hit {len(result)}')
  print(*result, sep='\n')


if __name__ == '__main__':
  # xxx: これだと、デフォルトのやつしか取れない
  search_word = 'Graphics'
  search_frameworks(search_word)

