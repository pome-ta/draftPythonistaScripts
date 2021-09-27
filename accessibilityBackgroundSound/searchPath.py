from pathlib import Path
import re

root_path = Path('/..' * str(Path.cwd()).count('/') + '/System/Library')

library_files = root_path.glob('**/*')

for f in library_files:
  if re.search('Ocean', f.name):
    print(f)