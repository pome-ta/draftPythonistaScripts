import re
from pathlib import Path

root = Path().cwd()
parent = root.parent

for p in parent.glob('*.icloud'):
  
  print(p.name)
  p.unlink(missing_ok=False)
