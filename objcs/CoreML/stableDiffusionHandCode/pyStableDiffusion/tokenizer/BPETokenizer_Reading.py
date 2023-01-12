from pathlib import Path

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
