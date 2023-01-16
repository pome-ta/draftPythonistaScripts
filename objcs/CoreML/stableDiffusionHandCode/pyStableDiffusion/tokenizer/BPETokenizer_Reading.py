from pathlib import Path
import json

from .BPETokenizer import _BPETokenizer


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


class BPETokenizer(_BPETokenizer):
  def __init__(self):
    super().__init__()

  @staticmethod
  def readVocabulary_url_(url: Path) -> dict:
    with open(url, encoding='utf-8') as f:
      vocabulary = json.load(f)
    return vocabulary

  @staticmethod
  def readMerges_url_(url: Path) -> list:
    content = url.read_text(encoding='utf-8')
    lines = content.splitlines()

    merges = []
    for index, line in enumerate(lines):
      if line[0] == '#':
        continue
      pair = line.split(' ')
      if len(pair) != 2:
        raise
      merges.append((TokenPair(pair[0], pair[1]), index))
    return merges

