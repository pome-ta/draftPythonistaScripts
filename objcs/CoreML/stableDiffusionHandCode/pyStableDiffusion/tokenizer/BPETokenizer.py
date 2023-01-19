from pathlib import Path
from itertools import combinations


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

  def __str__(self):
    return f'{repr(self)}\n\t(first: "{self.first}", second: "{self.second}")'


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
    #self.encode_input_('cat dogs')
    self.encode_input_('dogs')
    #self.encode_input_('cat')

  def encode_input_(self, input_str: str) -> list:
    normalized = input_str.strip().lower()
    words = normalized.split()
    # xxx: `map` をやりたいだけ
    h = list(map(lambda w: self.encode_word_(w), words))
    #print(h)

  def encode_word_(self, word: str) -> list:
    tokens = [str(w) for w in word]
    if len(tokens):
      tokens[-1] = tokens[-1] + '</w>'
    while True:
      pairs = self.pairs_for_(tokens[:])
      print('pairs')
      print(*pairs)
      print('---')
      canMerge = list(filter(lambda p: self.merges[p], pairs))
      print('canMerge')
      print(*canMerge)
      print('---')
      if not (len(canMerge)):
        break
      print('min')
      for cm in canMerge:
        print(cm)
        print(f'\t{self.merges[cm]}')
      shouldMerge = min(canMerge, key=lambda cm: self.merges[cm])
      print('shouldMerge')
      print(shouldMerge)
      print('----')
      tokens = self.update_tokens_merging_(tokens[:], shouldMerge)
    print('update tokens')
    print(tokens)
    return tokens

  def pairs_for_(self, tokens: str):
    if len(tokens) <= 1:
      return set()

    pairs = set()
    prev = tokens[0]
    tokens.pop(0)

    for current in tokens[:]:
      print('pairs_for_ for')
      print(prev, current)
      print('---')
      pairs.add(TokenPair(prev, current))
      tokens.pop(0)
      prev = current
    return pairs

  def update_tokens_merging_(self, tokens: str, bigram: TokenPair):
    if len(tokens) <= 1:
      return []

    newTokens: list = []
    index = 0
    while index < len(tokens):
      remainingTokens = tokens[0:]
      startMatchIndex = remainingTokens.index(
        bigram.first) if bigram.first in remainingTokens else None

      if startMatchIndex != None:
        if tokens[index:startMatchIndex]:
          newTokens.append(*tokens[index:startMatchIndex])

        if index < (len(tokens) - 1) and tokens[startMatchIndex +
                                                1] == bigram.second:
          newTokens.append(bigram.first + bigram.second)
          index = startMatchIndex + 2
        else:
          newTokens.append(bigram.first)
          index = startMatchIndex + 1
      else:
        newTokens.extend(remainingTokens)
        break
    return newTokens

  @staticmethod
  def readVocabulary_url_(url: Path) -> dict:
    pass

  @staticmethod
  def readMerges_url_(url: Path) -> list:
    pass

