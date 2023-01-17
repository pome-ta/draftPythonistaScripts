from pathlib import Path


class TokenPair:
  def __init__(self, first: str, second: str):
    self.first: str = first
    self.second: str = second

  def __eq__(self, other):
    if not isinstance(other, TokenPair):
      return False
    return self.first == other.first and self.second == other.second

  def __hash__(self):
    return hash((self.first, self.second))


class _BPETokenizer:
  def __init__(self):
    self.merges: dict
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
    self.encode_input_(' cat dogs ')

  def encode_input_(self, input_str: str) -> list:
    normalized = input_str.strip().lower()
    words = normalized.split()
    #print(words)
    # xxx: `map` をやりたいだけ
    h = list(map(lambda w: self.encode_word_(w), words))
    #print(h)

  def encode_word_(self, word: str) -> list:
    tokens = [str(w) for w in word]
    if len(tokens):
      tokens[-1] = tokens[-1] + '</w>'
    #print(tokens)
    pairs = self.pairs_for_(tokens)
    canMerge = list(filter(lambda p: self.merges[p], pairs))
    #print(self.merges)
    print(canMerge)
    '''
    for i in pairs:
      print(i)
    return tokens
    '''

  def pairs_for_(self, tokens: str):
    if len(tokens) <= 1:
      return set()
    pairs = set()
    prev = tokens[0]
    tokens.pop(0)
    for current in tokens[:]:
      pairs.add(TokenPair(prev, current))
      #print(prev, current)
      tokens.pop(0)
      prev = current
    return pairs

  @staticmethod
  def readVocabulary_url_(url: Path) -> dict:
    pass

  @staticmethod
  def readMerges_url_(url: Path) -> list:
    pass

