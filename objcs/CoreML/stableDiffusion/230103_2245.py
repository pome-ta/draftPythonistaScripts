from pathlib import Path
from objc_util import ObjCClass, NSBundle

import pdbg

MLModelConfiguration = ObjCClass('MLModelConfiguration')

models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'

class ResourceURLs:
  def __init__(self):
    pass

root_path = Path(models_root_path)

print(list(root_path.iterdir()))

