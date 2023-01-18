from pathlib import Path
import json

from .BPETokenizer import _BPETokenizer, TokenPair


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

    merges = {}
    for index, line in enumerate(lines):
      if line[0] == '#':
        continue
      pair = line.split(' ')
      if len(pair) != 2:
        raise
      same = merges.setdefault(TokenPair(pair[0], pair[1]), index)
      #merges.update({TokenPair(pair[0], pair[1]): index})
      #print(d)
      if not same:
        print(same)
    return merges

