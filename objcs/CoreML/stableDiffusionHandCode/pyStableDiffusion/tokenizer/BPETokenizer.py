from pathlib import Path


class _BPETokenizer:
  def __init__(self):
    self.merges: list
    self.vocabulary: dict
    self.startToken: str = '<|startoftext|>'
    # The end token.
    self.endToken: str = '<|endoftext|>'
    # The token used for padding
    self.padToken: str = '<|endoftext|>'
    # The unknown token.
    self.unknownToken: str = '<|endoftext|>'
    self.unknownTokenID: int = 0

  @classmethod
  def init_mergesAt_vocabularyAt_(cls, mergesURL: Path, vocabularyURL: Path):
    _cls = cls()
    _cls.merges = cls.readMerges_url_(mergesURL)
    _cls.vocabulary = cls.readVocabulary_url_(vocabularyURL)
    return _cls

  def tokenize(self, input_str: str, minCount: int=None):
    # xxx: property ?
    self.unknownTokenID = self.vocabulary[self.unknownToken]
    tokens: list = []
    tokens.append(self.startToken)
    tokens.append(input_str)
    tokens.append(self.endToken)
    self.encode_input_(' cat dog ')

  def encode_input_(self, input_str: str) -> list:
    normalized = input_str.strip().lower()
    words = normalized.split()
    print(words)
    # xxx: `map` をやりたいだけ
    h = list(map(lambda w: self.encode_word_(w), words))
    print(h)

  def encode_word_(self, word: str) -> list:
    tokens = [str(w) for w in word]
    tokens[-1] = tokens[-1] + '</w>'
    print(tokens)
    return tokens

  def pairs(self):
    pass

  @staticmethod
  def readVocabulary_url_(url: Path) -> dict:
    pass

  @staticmethod
  def readMerges_url_(url: Path) -> list:
    pass

