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



p_glob = p1.rglob(f'*{extension}')
base_list = sorted(list(p_glob))
name_list = ['*/' + p.name for p in base_list]


a = filecmp.cmpfiles(p1, p2, name_list)

'''


for pb in base_list:
  print(f'p:  {pb.name}')
  for p in p2.rglob(pb.name):
    if filecmp.cmp(p, pb):
      print(f't: {p.name}')
    else:
      print(f'f: {p.name}')
'''
