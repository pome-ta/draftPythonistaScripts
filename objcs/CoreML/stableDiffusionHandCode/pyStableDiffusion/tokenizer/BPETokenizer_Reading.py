from pathlib import Path
import json


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
  def __init__(self, mergesURL: Path, vocabularyURL: Path):
    self.merges: list
    self.vocabulary: dict
    self.startToken: str = '<|startoftext|>'
    # The end token.
    self.endToken: str = '<|endoftext|>'
    # The token used for padding
    self.padToken: str = '<|endoftext|>'
    # The unknown token.
    self.unknownToken: str = '<|endoftext|>'

    self.merges = self.readMerges_url_(mergesURL)
    self.vocabulary = self.readVocabulary_url(vocabularyURL)

  def readVocabulary_url(self, url: Path) -> dict:
    with open(url, encoding='utf-8') as f:
      vocabulary = json.load(f)
    return vocabulary

  def readMerges_url_(self, url: Path) -> list:
    content = url.read_text(encoding='utf-8')
    lines = content.splitlines()

    merges = []
    for index, line in enumerate(lines):
      if line[0] == '#': continue
      pair = line.split(' ')
      if len(pair) != 2: raise
      merges.append((TokenPair(pair[0], pair[1]), index))
    return merges

