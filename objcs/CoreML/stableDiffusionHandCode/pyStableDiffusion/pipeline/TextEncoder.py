from pathlib import Path

import pdbg

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

    self.inputDescription: None
    self.inputShape: None

    self.init_tokenizer_modelAt_configuration_(tokenizer, url, configuration)

  def init_tokenizer_modelAt_configuration_(self,
                                            _tokenizer: BPETokenizer,
                                            _url: Path,
                                            _configuration):
    self.tokenizer = _tokenizer
    self.model = ManagedMLModel(_url, _configuration)

  def encode(self):
    inputShape: list
    inputShape = self._inputShape()
    inputLength = inputShape[-1]
    print(inputLength)

  def _inputDescription(self):
    # xxx: getter/setter ?
    perform = self.model.perform()
    # todo: `model.modelDescription.inputDescriptionsByName.first!.value`
    _inputDescription = perform.modelDescription().inputDescriptionsByName(
    ).allValues()[0]
    #print(_inputDescription)
    return _inputDescription

  def _inputShape(self):
    inputDescription: MLFeatureDescription
    inputDescription = self._inputDescription()
    #_inputShape = inputDescription.multiArrayConstraint().shape()
    #print(_inputShape)
    #pdbg.state(_inputShape)
    #print(list(_inputShape))
    #_inputShape = [int(i) for i in inputDescription.multiArrayConstraint().shape()]
    #intValue

    #print(_inputShape)
    '''
    for n, i in enumerate(inputDescription.multiArrayConstraint().shape()):
      if n:
        pdbg.state(i)
    '''
    _inputShape = [
      i.intValue() for i in inputDescription.multiArrayConstraint().shape()
    ]
    #print(_inputShape)
    return _inputShape

