import difflib
import filecmp
from pathlib import Path

extension = 'swift'

p1 = Path(
  '/private/var/mobile/Containers/Shared/AppGroup/690154A9-9FC9-4B1D-8CB8-AB398AC342C4/File Provider Storage/Downloads/BeginningMetal/10 - Instances/Final/'
)

p2 = Path(
  '/private/var/mobile/Containers/Shared/AppGroup/690154A9-9FC9-4B1D-8CB8-AB398AC342C4/File Provider Storage/Downloads/BeginningMetal/9 - Model IO/Challenge/'
)


def read_text(p: Path) -> str:
  return p.read_text(encoding='utf-8').splitlines(keepends=True)


p_glob = p1.rglob(f'*{extension}')
base_list = sorted(list(p_glob))
'''
for pb in base_list:
  new_flag = True
  for p in p2.rglob(pb.name):
    new_flag = False
    if filecmp.cmp(p, pb):
      print(f't: {p.name}')
    else:
      print(f'--- {pb.name}')
      diff = difflib.ndiff(read_text(pb), read_text(p))
      #print(list(diff))
  else:
    if new_flag:
      print(f'p:  {pb.name}')
'''
pb = list(filter(lambda x: x.name == 'ViewController.swift', base_list))[0]
p = list(p2.rglob(pb.name))[0]

p1s = read_text(pb)
p2s = read_text(p)
differ = difflib.Differ()
#diff = difflib.unified_diff(a=read_text(pb), b=read_text(p), fromfile=pb.name, n=0,lineterm='')
diff = difflib.unified_diff(
  a=read_text(pb),
  b=read_text(p),
  n=0,
)

for s in diff:
  print(s)

