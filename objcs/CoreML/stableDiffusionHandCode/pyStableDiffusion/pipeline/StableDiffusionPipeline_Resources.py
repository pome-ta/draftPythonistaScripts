from pathlib import Path
from objc_util import ObjCClass
try:
  from ..tokenizer.BPETokenizer_Reading import BPETokenizer
except:
  import sys
  sys.path.append(str(Path.cwd() / '..'))

  from tokenizer.BPETokenizer_Reading import BPETokenizer

from .TextEncoder import TextEncoder
from .Unet import Unet

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
      self,
      _baseURL: Path,
      config=MLModelConfiguration.new(),
      disableSafety=False,
      reduceMemory=False):
    self.urls = ResourceURLs(_baseURL)
    self.tokenizer = BPETokenizer(self.urls.mergesURL, self.urls.vocabURL)
    self.textEncoder = TextEncoder(self.tokenizer, self.urls.textEncoderURL,
                                   config)

    self.unet: None
    if self.urls.unetChunk1URL.exists() and self.urls.unetChunk2URL.exists():
      print('12')
    else:
      self.unet = Unet(self.urls.unetURL, config)

  def init(self):
    # todo: 最後に全部`self.` する
    pass

