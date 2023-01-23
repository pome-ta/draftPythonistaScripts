from pathlib import Path
import ctypes

from objc_util import ObjCClass


from ..tokenizer.BPETokenizer_Reading import BPETokenizer
from .ManagedMLModel import ManagedMLModel

import pdbg


MLMultiArray = ObjCClass('MLMultiArray')
MLDictionaryFeatureProvider = ObjCClass('MLDictionaryFeatureProvider')

class TextEncoder:
  def __init__(self, tokenizer: BPETokenizer, url: Path, configuration):
    self.tokenizer: BPETokenizer
    self.model = None

    # xxx: getter/setter ?
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
    #print(inputLength)
    (tokens, ids) = self.tokenizer.tokenize('cat', inputLength)

    if len(ids) > inputLength:
      # xxx: あとで書く
      pass
    self.encode_ids_(ids)

  def encode_ids_(self, ids: list):
    _inputDescription= self._inputDescription()
    inputName = _inputDescription.name()
    inputShape = self._inputShape()
    #floatIds = [ctypes.c_float(id) for id in ids]
    floatIds = [float(id) for id in ids]
    #self.hoge = MLMultiArray.alloc().initWithScalars_shape_dataType_(floatIds,inputShape, 16, None)
    #initWithScalars_shape_dataType_
    #pdbg.state(self.hoge)
    self.inputArray = MLMultiArray.alloc().initWithShape_dataType_error_(inputShape, 16, None)
    [self.inputArray.setObject_atIndexedSubscript_(obj, index) for index, obj in enumerate(floatIds)]

    #pdbg.state(self.inputArray)
    self.inputFeatures = MLDictionaryFeatureProvider.new().initWithDictionary_error_(({inputName: self.inputArray}), None)
    pdbg.state(self.inputFeatures.dictionary())
    
    
    



  def _inputDescription(self):
    # xxx: getter/setter ?
    perform = self.model.perform()
    # todo: `model.modelDescription.inputDescriptionsByName.first!.value`
    _inputDescription = perform.modelDescription().inputDescriptionsByName(
    ).allValues()[0]
    return _inputDescription

  def _inputShape(self):
    inputDescription: MLFeatureDescription
    inputDescription = self._inputDescription()
    _inputShape = [
      i.intValue() for i in inputDescription.multiArrayConstraint().shape()
    ]
    return _inputShape

