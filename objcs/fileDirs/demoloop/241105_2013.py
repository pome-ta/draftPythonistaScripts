from pathlib import Path

root = Path('/private/var/')

#print(root.is_file())

for i in root.iterdir():
  print(i.name)
