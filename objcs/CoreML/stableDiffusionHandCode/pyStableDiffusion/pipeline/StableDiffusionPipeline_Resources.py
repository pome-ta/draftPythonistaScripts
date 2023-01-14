from pathlib import Path

from objc_util import ObjCClass

from .StableDiffusionPipeline import _StableDiffusionPipeline
'''
try
  from ..tokenizer.BPETokenizer_Reading import BPETokenizer
except:
  import sys
  sys.path.append(str(Path.cwd() / '..'))

  from tokenizer.BPETokenizer_Reading import BPETokenizer
'''
from ..tokenizer.BPETokenizer_Reading import BPETokenizer
from .TextEncoder import TextEncoder
from .Unet import Unet
from .Decoder import Decoder
from .SafetyChecker import SafetyChecker

MLModelConfiguration = ObjCClass('MLModelConfiguration')

# class MLModelConfiguration:
#   @classmethod
#   def new(cls):
#     return None


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


class StableDiffusionPipeline(_StableDiffusionPipeline):
  def __init__(self):
    super().__init__()

  @classmethod
  def init_resourcesAt_configuration_(cls,
                                      baseURL: Path,
                                      config=MLModelConfiguration.new(),
                                      disableSafety=False,
                                      reduceMemory=False):
    urls = ResourceURLs(baseURL)
    tokenizer = BPETokenizer.init_mergesAt_vocabularyAt_(
      urls.mergesURL, urls.vocabURL)
    textEncoder = TextEncoder(tokenizer, urls.textEncoderURL, config)

    unet: None
    if urls.unetChunk1URL.exists() and urls.unetChunk2URL.exists():
      print('unetChunk1URL, unetChunk2URL')
    else:
      unet = Unet(urls.unetURL, config)

    decoder = Decoder(urls.decoderURL, config)

    safetyChecker: None
    if not (disableSafety) and urls.safetyCheckerURL.exists():
      safetyChecker = SafetyChecker(urls.safetyCheckerURL, config)

    _cls = cls()
    _cls.init_textEncoder_unet_decoder_safetyChecker_reduceMemory(
      textEncoder, unet, decoder, safetyChecker, reduceMemory)
    return _cls

