from pathlib import Path
import glob
import json


def main(root_path:Path):
  for g in root_path.rglob('*'):
    print(g)


if __name__ == '__main__':
  target_path_str = './docs'
  save_path_srt = './docs'
  
  
  target_path = Path(target_path_str)
  
  

  main(target_path)

