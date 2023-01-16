from pathlib import Path

try:
  from ..tokenizer.BPETokenizer_Reading import BPETokenizer
except:
  import sys
  sys.path.append(str(Path.cwd() / '..'))

  from tokenizer.BPETokenizer_Reading import BPETokenizer

from .ManagedMLModel import ManagedMLModel


class TextEncoder:
  def __init__(self, tokenizer: BPETokenizer, url: Path, configuration):
    self.tokenizer: BPETokenizer
    self.model = None

    self._inputDescription: None
    self._inputShape: None

    self.init_tokenizer_modelAt_configuration_(tokenizer, url, configuration)

  def init_tokenizer_modelAt_configuration_(self,
                                            _tokenizer: BPETokenizer,
                                            _url: Path,
                                            _configuration):
    self.tokenizer = _tokenizer
    self.model = ManagedMLModel(_url, _configuration)

  def encode(self):
    inputDescription: MLFeatureDescription
    self.model.loadModel()

  @property
  def inputDescription(self):
    return self._inputDescription

  @inputDescription.setter
  def inputDescription(self):
    perform = self.model.perform()
    self._inputDescription = None

