from pathlib import Path
#from  glob import glob
import clipboard

module_root_uri = './objcista'
module_root_path = Path(module_root_uri)


def gene_tree(tree_path: Path, tree_depth: int = 0, tree_str: str = '') -> str:
  side_line = '|' + '─' * tree_depth + ' ' if tree_depth else None
  is_dir = tree_path.is_dir()
  tree_str += tree_path.name + ('/' if is_dir else None) + '\n'
  return tree_str


tree_path = gene_tree(module_root_path)

