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
    self.textEncoderURL: Path
    self.unetURL: Path
    self.unetChunk1URL: Path
    self.unetChunk2URL: Path
    self.decoderURL: Path
    self.safetyCheckerURL: Path
    self.vocabURL: Path
    self.mergesURL: Path
    self._init(root_paths)

  def _init(self, _root):
    self.textEncoderURL = Path(_root, 'TextEncoder.mlmodelc')
    self.unetURL = Path(_root, 'Unet.mlmodelc')
    self.unetChunk1URL = Path(_root, 'UnetChunk1.mlmodelc')
    self.unetChunk2URL = Path(_root, 'UnetChunk2.mlmodelc')
    self.decoderURL = Path(_root, 'VAEDecoder.mlmodelc')
    self.safetyCheckerURL = Path(_root, 'SafetyChecker.mlmodelc')
    self.vocabURL = Path(_root, 'vocab.json')
    self.mergesURL = Path(_root, 'merges.txt')


class BPETokenizer:
  def __init__(self):
    self.merges: list
    self.vocabulary: list
    self.startToken: str = '<|startoftext|>'
    # The end token.
    self.endToken: str = '<|endoftext|>'
    # The token used for padding
    self.padToken: str = '<|endoftext|>'
    # The unknown token.
    self.unknownToken: str = '<|endoftext|>'
    
  def readMerges_url_(self):
    pass


root_path = Path(models_root_path)

urls = ResourceURLs(root_path)
config = MLModelConfiguration.new()

content_url = urls.mergesURL
content = content_url.read_text(encoding='utf-8')


