from pathlib import Path
from pprint import pprint


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
    #self.encode_input_('cat dogs')
    #self.encode_input_('dogs')
    #self.encode_input_('asparagus')
    #self.encode_input_('elephant')
    #self.encode_input_('dog')
    #self.encode_input_('cat')
    tokens += self.encode_input_(input_str)
    tokens.append(self.endToken)

    minLen = [self.padToken for _ in range(minCount-len(tokens))] if minCount>len(tokens) else None
    if minLen:
      tokens += minLen

    ids = [self.__is_key(tkn) for tkn in tokens]
    #return (tokens: tokens, tokenIDs: ids)
    return [tokens, ids]

  def __is_key(self, token: str) -> dict:
    # xxx: `TokenPair` か `False` 投げ返すのはキモい
    # xxx: dict の例外ハンドリングを調べる
    try:
      return self.vocabulary[token]
    except KeyError as e:
      pass
    return self.vocabulary[self.unknownTokenID]




  def encode_input_(self, input_str: str) -> list:
    normalized = input_str.strip().lower()
    words = normalized.split()
    # xxx: `map` をやりたいだけ
    _words = list(map(lambda w: self.encode_word_(w), words))
    # note: [Python 3 で flatten する方法いろいろ - Qiita](https://qiita.com/hoto17296/items/e1f80fef8536a0e5e7db)
    flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

    return flatten(_words)

  def encode_word_(self, word: str) -> list:
    tokens = [str(w) for w in word]
    if len(tokens):
      tokens[-1] = tokens[-1] + '</w>'
    while True:
      pairs = self.pairs_for_(tokens[:])
      canMerge = list(filter(lambda p: self.__is_merge(p), pairs))

      if not (len(canMerge)):
        break

      shouldMerge = min(canMerge, key=lambda cm: self.merges[cm])
      tokens = self.update_tokens_merging_(tokens[:], shouldMerge)

    return tokens

  def __is_merge(self, pair: TokenPair) -> TokenPair:
    # xxx: `TokenPair` か `False` 投げ返すのはキモい
    # xxx: dict の例外ハンドリングを調べる
    try:
      return self.merges[pair]
    except KeyError as e:
      pass
    return False

  def pairs_for_(self, tokens: str):
    if len(tokens) <= 1:
      return set()

    pairs = set()
    prev = tokens[0]
    tokens.pop(0)

    for current in tokens[:]:
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
      remainingTokens = [
        token if n >= index else None for n, token in enumerate(tokens)
      ]
      startMatchIndex = remainingTokens.index(
        bigram.first) if bigram.first in remainingTokens else None

      if startMatchIndex != None:
        if tokens[index:startMatchIndex]:
          newTokens += tokens[index:startMatchIndex]

        if index < (len(tokens) - 1) and tokens[startMatchIndex +
                                                1] == bigram.second:
          newTokens.append(bigram.first + bigram.second)
          index = startMatchIndex + 2
        else:
          newTokens.append(bigram.first)
          index = startMatchIndex + 1
      else:
        newTokens.extend(list(filter(lambda t: t, remainingTokens)))
        break

    return newTokens

  @staticmethod
  def readVocabulary_url_(url: Path) -> dict:
    pass

  @staticmethod
  def readMerges_url_(url: Path) -> list:
    pass

