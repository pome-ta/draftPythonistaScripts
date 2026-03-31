import difflib
from pathlib import Path


def print_simple_diff(file_new_path: str, file_old_path: str):
  new_path = Path(file_new_path)
  old_path = Path(file_old_path)
  

  with (
      new_path.open('r', encoding='utf-8') as f1,
      old_path.open('r', encoding='utf-8') as f2,
  ):
    a = f1.readlines()
    b = f2.readlines()

  diff = list(
    difflib.unified_diff(a,
                         b,
                         fromfile=old_path.name,
                         tofile=new_path.name,
                         n=0))

  print(f'## File Diff: `{old_path.name}` vs `{new_path.name}`\n')
  
  if not diff:
    print('差分はありません。\n')
    return

  ext = old_path.suffix[1:] if old_path.suffix else 'text'

  print(f'```diff {ext}')
  for line in diff:
    print(line, end='')
  print('```\n')


# --- 実行 ---
if __name__ == '__main__':
  root_path = Path(__file__, '..', 'difftests')
  _old = root_path / 'sample_old.py'
  _new = root_path / 'sample_new.py'

  print_simple_diff(_old.resolve(), _new.resolve())

