from pathlib import Path

root_path = Path().home()
cwd = Path().cwd()

print(root_path)
for f in root_path.glob('*.json'):
  print(f)


