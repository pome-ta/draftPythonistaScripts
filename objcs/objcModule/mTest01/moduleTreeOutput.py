from pathlib import Path
import os
#from  glob import glob
import clipboard
from pprint import pprint

module_root_uri = './objcista'
module_root_path = Path(module_root_uri)


def tree_dict(target_path: Path):
  pass


def gene_tree(tree_path: Path, tree_depth: int = 0, tree_str: str = '') -> str:
  side_line = '|' + '─' * tree_depth + ' ' if tree_depth else None
  is_dir = tree_path.is_dir()
  tree_str += tree_path.name + ('/' if is_dir else None) + '\n'
  return tree_str


def file_tree(path: str = '.'):
  dirs = os.listdir(path)
  pprint(dirs)
  print('___')
  buf_child = []
  root = {
    'path': path,
    'name': '' if path == '.' else path,
    'child': buf_child,
  }
  for dir in dirs:
    dir_path = os.path.join(path, dir)
    if os.path.isdir(dir_path):
      # dirの場合
      child = file_tree(dir_path)
      child['name'] = dir
      buf_child.append(child)
    else:
      # dir以外
      buf_child.append({
        'path': dir_path,
        'name': dir,
        'child': [],
      })
  return root


tree_path = gene_tree(module_root_path)
'''
'''
tree = file_tree(module_root_uri)
#pprint(tree)
for p in Path(module_root_path, 'metaClasses').iterdir():
  print(p)
  if p.name == 'objcView.py':
    p.unlink()
  if p.suffix  == '.icloud':
    p.unlink()
