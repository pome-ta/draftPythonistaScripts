from pathlib import Path
from objc_util import ObjCClass

try:
  from ..tokenizer.BPETokenizer_Reading import hoge
except:
  import sys
  sys.path.append(str(Path.cwd() / '..'))

  from tokenizer.BPETokenizer_Reading import hoge

MLModelConfiguration = ObjCClass('MLModelConfiguration')


class ResourceURLs:
  def __init__(self, baseURL: Path):
    self.textEncoderURL: Path
    self.unetURL: Path
    self.unetChunk1URL: Path
    self.unetChunk2URL: Path
    self.decoderURL: Path
    self.safetyCheckerURL: Path
    self.vocabURL: Path
    self.mergesURL: Path
    self._init(baseURL)

  def _init(self, _baseURL):
    self.textEncoderURL = Path(_baseURL, 'TextEncoder.mlmodelc')
    self.unetURL = Path(_baseURL, 'Unet.mlmodelc')
    self.unetChunk1URL = Path(_baseURL, 'UnetChunk1.mlmodelc')
    self.unetChunk2URL = Path(_baseURL, 'UnetChunk2.mlmodelc')
    self.decoderURL = Path(_baseURL, 'VAEDecoder.mlmodelc')
    self.safetyCheckerURL = Path(_baseURL, 'SafetyChecker.mlmodelc')
    self.vocabURL = Path(_baseURL, 'vocab.json')
    self.mergesURL = Path(_baseURL, 'merges.txt')


class StableDiffusionPipeline:
  def __init__(self, baseURL: Path):
    self.init_resourcesAt_configuration_disableSafety_reduceMemory_(baseURL)

  def init_resourcesAt_configuration_disableSafety_reduceMemory_(
      self, _baseURL: Path):
    self.urls = ResourceURLs(_baseURL)
    self.aaa = hoge()

