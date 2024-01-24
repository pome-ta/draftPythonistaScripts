from pathlib import Path
import clipboard


module_root_uri = './objcista'
module_root_path = Path(module_root_uri)

for p in module_root_path.iterdir():
  print(p)
  if p.suffix  == '.icloud':
    p.unlink()
