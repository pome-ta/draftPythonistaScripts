from pathlib import Path
import json
# from objc_util import ObjCClass, NSBundle, nsurl

# import pdbg

# MLModelConfiguration = ObjCClass('MLModelConfiguration')

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


class TokenPair:
  def __init__(self, first: str, second: str):
    self.first: str
    self.second: str
    self._init(first, second)

  def _init(self, _first: str, _second: str):
    self.first = _first
    self.second = _second

  def __str__(self) -> str:
    return f'(first: "{self.first}", second: "{self.second}")'


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

  def readVocabulary_url(self, url: Path):
    pass

  def readMerges_url_(self, url: Path):
    pass


root_path = Path(models_root_path)
#root_path = Path('./objcs/CoreML/stableDiffusion', models_root_path)

urls = ResourceURLs(root_path)
# config = MLModelConfiguration.new()

content_url = urls.mergesURL
content = content_url.read_text(encoding='utf-8')
# lines = content.split('\n')
lines = content.splitlines()
'''
with content_url.open(encoding='utf-8') as f:
  lines = f.readlines()
'''
merges = []

for index, line in enumerate(lines):
  if line[0] == '#':
    continue
  pair = line.split(' ')
  if len(pair) != 2:
    raise
  merges.append((TokenPair(pair[0], pair[1]), index))

# print(merges)
#print(len(merges))

json_url = urls.vocabURL
#content_json = json_url.read_text(encoding='utf-8')
#vocabulary_json = json.loads(content_json)
with open(json_url, encoding='utf-8') as f:
  vocabulary_json = json.load(f)

