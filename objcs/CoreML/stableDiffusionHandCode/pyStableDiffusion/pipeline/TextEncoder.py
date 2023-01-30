from pathlib import Path
import ctypes

from objc_util import ObjCClass, NSMutableDictionary, ns, load_framework

from ..tokenizer.BPETokenizer_Reading import BPETokenizer
from .ManagedMLModel import ManagedMLModel

import pdbg

#load_framework('CoreML')
MLMultiArray = ObjCClass('MLMultiArray')
MLDictionaryFeatureProvider = ObjCClass('MLDictionaryFeatureProvider')


class TextEncoder:
  def __init__(self, tokenizer: BPETokenizer, url: Path, configuration):
    self.tokenizer: BPETokenizer
    self.model = ManagedMLModel

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
    (tokens, ids) = self.tokenizer.tokenize('cat', inputLength)

    if len(ids) > inputLength:
      # xxx: あとで書く
      pass
    self.encode_ids_(ids)

  def encode_ids_(self, ids: list):
    _inputDescription = self._inputDescription()
    inputName = _inputDescription.name()
    inputShape = self._inputShape()
    floatIds = [float(id) for id in ids]

    inputArray = MLMultiArray.alloc().initWithShape_dataType_error_(
      inputShape, 16, None)

    [
      inputArray.setObject_atIndexedSubscript_(obj, index)
      for index, obj in enumerate(floatIds)
    ]

    #pdbg.state(ObjCInstance(inputArray.dataPointer().value))

    #inputDict = NSMutableDictionary.alloc().initWithObject_forKey_(inputArray, inputName)

    inputFeatures = MLDictionaryFeatureProvider.alloc(
    ).initWithDictionary_error_(ns({
      inputName: inputArray
    }), None)
    '''
    inputFeatures = MLDictionaryFeatureProvider.alloc(
    ).initWithDictionary_error_(({
      inputName: inputArray
    }), None)
    '''

    #inputFeatures = MLDictionaryFeatureProvider.alloc().initWithDictionary_error_(ctypes.pointer(inputDict).contents, None)

    #print('inputFeatures ---')
    #pdbg.state(inputFeatures)

    #pdbg.state(self.model)
    #pdbg.state(inputFeatures)
    #pdbg.state(self.model)
    #result = self.model.predictionFromFeatures_error_(inputFeatures, None)
    #print(self.model)
    #pdbg.state(self.model.perform())
    #model = self.model.perform()
    #print(model)

    #pdbg.state(self.perform)
    #pdbg.state(self.model)
    result = self.perform.predictionFromFeatures_error_(inputFeatures, None)

    #result = self.model.predictionFromFeatures_error_(inputFeatures, None)
    #pdbg.state(model)
    #pdbg.state(self.model)

    #pdbg.state(result)
    #perform = self.model.perform()
    #result = perform.predictionFromFeatures_error_(inputFeatures, None)
    #predictionFromFeatures_error_
    
    #pdbg.state(self.perform.predictionEvent())
    #pdbg.state(self.perform)
    pdbg.state(self.model)

  def _inputDescription(self):
    # xxx: getter/setter ?
    self.perform = self.model.perform()
    # todo: `model.modelDescription.inputDescriptionsByName.first!.value`
    _inputDescription = self.perform.modelDescription(
    ).inputDescriptionsByName().allValues()[0]
    return _inputDescription

  def _inputShape(self):
    inputDescription: MLFeatureDescription
    inputDescription = self._inputDescription()
    _inputShape = [
      i.intValue() for i in inputDescription.multiArrayConstraint().shape()
    ]
    return _inputShape

