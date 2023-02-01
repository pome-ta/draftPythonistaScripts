from pathlib import Path

from objc_util import ObjCClass, NSMutableDictionary, ns, load_framework, ObjCInstance, autoreleasepool, create_objc_class, sel, NSDictionary

from ..tokenizer.BPETokenizer_Reading import BPETokenizer
from .ManagedMLModel import ManagedMLModel

import pdbg

#load_framework('CoreML')
MLMultiArray = ObjCClass('MLMultiArray')
MLDictionaryFeatureProvider = ObjCClass('MLDictionaryFeatureProvider')
MLFeatureValue = ObjCClass('MLFeatureValue')


def featureValueForName_(_self, _cmd, featureName):
  if featureName:
    #pdbg.state(ObjCInstance(featureName))
    #return ObjCInstance(featureName)
    #return str(ObjCInstance(featureName))
    this = ObjCInstance(_self)
    dictionary = this.dictionary()
    #pdbg.state(ObjCInstance(_self))
    #pdbg.state(dictionary)

    _value = dictionary.objectForKey_(ObjCInstance(featureName))
    pdbg.state(_value)

    #featureValue = MLFeatureValue.featureValueWithString_(ObjCInstance(featureName))
    #return sel(ObjCInstance(featureName))
    #pdbg.state(featureValue)
    #return featureValue
    #return ns(value)
    value = MLFeatureValue.featureValueWithMultiArray_(_value)
    #pdbg.state(value)
    #return value
  else:
    print('kita---------?')
    raise


_methods = [featureValueForName_]
_protocols = ['MLFeatureProvider']

myMLDictionaryFeatureProvider = create_objc_class(
  name='myMLDictionaryFeatureProvider',
  superclass=MLDictionaryFeatureProvider,
  methods=_methods,
  protocols=_protocols)


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

    #pdbg.state(inputArray)

    #inpitDict = NSDictionary.alloc().initWithObjects_forKeys_([inputArray], [inputName])

    #pdbg.state(inpitDict)

    inpitDict = NSMutableDictionary.dictionaryWithObject_forKey_(
      inputArray, inputName)
    #pdbg.state(inpitDict)

    #inputFeatures = MLDictionaryFeatureProvider.alloc().initWithDictionary_error_(inpitDict, None)
    
    inputFeatures = myMLDictionaryFeatureProvider.alloc().initWithDictionary_error_(inpitDict, None)

    #inputFeatures
    #pdbg.state(inputFeatures)

    #inputFeatures = MLDictionaryFeatureProvider.new()
    #inputFeatures.setDictionary_(inpitDict)

    #pdbg.state(inputFeatures.dictionary())
    #pdbg.state(inputFeatures)
    #pdbg.state(self.perform)
    #pdbg.state(self.model)

    result = self.perform.predictionFromFeatures_error_(inputFeatures, None)

    #pdbg.state(result)

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

