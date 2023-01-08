from pathlib import Path
from objc_util import ObjCClass, NSBundle, nsurl

import pdbg

MLModelConfiguration = ObjCClass('MLModelConfiguration')

models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'


class ResourceURLs:
  def __init__(self, root_paths):
    self.textEncoderURL: nsurl
    self.unetURL: nsurl
    self.unetChunk1URL: nsurl
    self.unetChunk2URL: nsurl
    self.decoderURL: nsurl
    self.safetyCheckerURL: nsurl
    self.vocabURL: nsurl
    self.mergesURL: nsurl

  def _init(self, paths):
    pass


i = [
  'TextEncoder.mlmodelc',
  'Unet.mlmodelc',
  'UnetChunk1.mlmodelc',
  'UnetChunk2.mlmodelc',
  'VAEDecoder.mlmodelc',
  'SafetyChecker.mlmodelc',
  'vocab.json',
  'merges.txt',
]

root_path = Path(models_root_path)

print(list(root_path.iterdir()))

