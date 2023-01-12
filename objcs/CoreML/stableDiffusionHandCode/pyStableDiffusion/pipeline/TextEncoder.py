from pathlib import Path

try:
  from ..tokenizer.BPETokenizer_Reading import BPETokenizer
except:
  import sys
  sys.path.append(str(Path.cwd() / '..'))

  from tokenizer.BPETokenizer_Reading import BPETokenizer

from .ManagedMLModel import ManagedMLModel

class TextEncoder:
  def __init__(self, tokenizer: BPETokenizer, url: Path):
    self.tokenizer: BPETokenizer
    self.model = None
    self.init_tokenizer_modelAt_configuration_(tokenizer, url)

  def init_tokenizer_modelAt_configuration_(self,
                                            _tokenizer: BPETokenizer,
                                            _url: Path):
    self.tokenizer = _tokenizer

