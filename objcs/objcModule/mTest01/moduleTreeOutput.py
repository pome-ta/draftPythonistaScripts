from pathlib import Path
#from  glob import glob
import clipboard


module_root_uri = './objcista'
module_root_path = Path(module_root_uri)

for p in module_root_path.iterdir():
  print(p)
  

