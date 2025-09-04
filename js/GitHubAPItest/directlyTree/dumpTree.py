from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
import json

from pprint import pprint


@dataclass
class FileNode:
  name: str
  type: str
  children: list[FileNode] | None = None


def build_tree(path: Path) -> FileNode:
  if path.is_dir():
    children = [build_tree(child) for child in sorted(path.iterdir())]
    return FileNode(name=path.name, type='dir', children=children)
  else:
    return FileNode(name=path.name, type='file')


def main(root_path: Path):
  for g in root_path.rglob('*'):
    print(type(g))


if __name__ == '__main__':
  target_path_str = './sounds'
  save_path_srt = './docs'

  target_path = Path(target_path_str)

  #main(target_path)
  tree = build_tree(target_path)
  a = asdict(tree)
  s = json.dumps(a, ensure_ascii=False, indent=2)

  #pprint(a)
  print(s)

