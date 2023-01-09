from pathlib import Path
from objc_util import ObjCClass, NSBundle, nsurl

import pdbg

MLModelConfiguration = ObjCClass('MLModelConfiguration')

models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'

"""
'TextEncoder.mlmodelc',
'Unet.mlmodelc',
'UnetChunk1.mlmodelc',
'UnetChunk2.mlmodelc',
'VAEDecoder.mlmodelc',
'SafetyChecker.mlmodelc',
'vocab.json',
'merges.txt',
"""


class ResourceURLs:
  def __init__(self, root_paths: Path):
    self.resource_models = [
      'TextEncoder.mlmodelc',
      'Unet.mlmodelc',
      'UnetChunk1.mlmodelc',
      'UnetChunk2.mlmodelc',
      'VAEDecoder.mlmodelc',
      'SafetyChecker.mlmodelc',
      'vocab.json',
      'merges.txt',
    ]
    self.textEncoderURL: Path
    self.unetURL: Path
    self.unetChunk1URL: Path
    self.unetChunk2URL: Path
    self.decoderURL: Path
    self.safetyCheckerURL: Path
    self.vocabURL: Path
    self.mergesURL: Path

  def _init(self, _root_paths):
    self.textEncoderURL = nsurl(str(Path(
      _root_paths, )))

  def __appending_path(self, file_name):
    return


root_path = Path(models_root_path)

#print(list(root_path.iterdir()))
#pdbg.state(NSBundle)
#pdbg.state(NSBundle.mainBundle())
#pdbg.state(NSBundle.loadedBundles())
#pdbg.state(NSBundle.mainBundle().sharedSupportPath())
pdbg.state(NSBundle.allBundles())

