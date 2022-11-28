from pathlib import Path


def parent_level(level_int):
  return '../' * level_int


def is_access(index):
  _level = index + 1
  _path = cwd_path / parent_level(deep - _level)
  return True if list(_path.glob('*')) else False


cwd_path = Path().cwd()

directly_list = str(cwd_path).split('/')
deep = len(directly_list)

for n, d in enumerate(directly_list):
  access = '🙆‍♂️' if is_access(n) else '🙅‍♀️'
  if not d:
    d = 'root'
  output = f'{access}({deep - n -1}: {d}'
  if n:
    tab = ' ' * n
    print(f'{tab} └ {output}')
  else:
    print(f'{output}')


