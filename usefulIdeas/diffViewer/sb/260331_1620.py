import difflib
import filecmp
from pathlib import Path


def print_simple_diff(file_old_path: Path, file_new_path: Path):

  old_dir_list = str(file_old_path.resolve()).split('/')
  new_dir_list = str(file_new_path.resolve()).split('/')

  old_root_str = '/'.join(
    list(filter(lambda f: not f in new_dir_list, old_dir_list)))
  new_root_str = '/'.join(
    list(filter(lambda f: not f in old_dir_list, new_dir_list)))

  old_file_name = f'{old_root_str}/{file_old_path.name}'
  new_file_name = f'{new_root_str}/{file_new_path.name}'

  with (
      file_old_path.open('r', encoding='utf-8') as f1,
      file_new_path.open('r', encoding='utf-8') as f2,
  ):
    a = f1.readlines()
    b = f2.readlines()

  diff = list(
    difflib.unified_diff(
      a,
      b,
      fromfile=old_file_name,
      tofile=new_file_name,
      n=0,
    ))

  print(f'### {file_new_path.name}\n')
  print(f'- File Diff: `{old_file_name}` vs `{new_file_name}`\n')

  if not diff:
    print('- 差分なし\n\n')
    return

  ext = file_old_path.suffix[1:] if file_old_path.suffix else 'text'

  print(f'```diff {file_new_path.name}:{ext}')
  [print(line, end='') for line in diff]
  print('```\n\n')


def print_differences_extension(old_path: Path, new_path: Path, extension):
  new_glob_list = sorted(list(new_path.rglob(f'*{extension}')))

  for n_path in new_glob_list:
    new_file_flag = True

    for o_path in old_path.rglob(n_path.name):
      new_file_flag = False

      if not filecmp.cmp(o_path, n_path):
        print_simple_diff(o_path, n_path)
    else:
      if new_file_flag:

        print(f'### {n_path.name}\n')
        print(f'- new file\n\n')


if __name__ == '__main__':
  extension = 'swift'


  p1_str = '/private/var/mobile/Containers/Shared/AppGroup/690154A9-9FC9-4B1D-8CB8-AB398AC342C4/File Provider Storage/Downloads/BeginningMetal/12-BeginningMetal-DiffuseSpecularLighting/Challenge/'
  p2_str = '/private/var/mobile/Containers/Shared/AppGroup/690154A9-9FC9-4B1D-8CB8-AB398AC342C4/File Provider Storage/Downloads/BeginningMetal/13-BeginningMetal-MakingAGamePart1/Final/'

  p1 = Path(p1_str)
  p2 = Path(p2_str)

  print_differences_extension(p1, p2, extension)

