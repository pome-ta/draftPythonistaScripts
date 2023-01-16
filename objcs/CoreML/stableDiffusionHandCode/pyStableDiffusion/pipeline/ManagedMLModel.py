from pathlib import Path

from objc_util import ObjCClass, nsurl

import pdbg

MLModel = ObjCClass('MLModel')


class ManagedMLModel:
  def __init__(self, url: Path, configuration):
    self.modelURL: Path
    self.configuration: None
    self.loadedModel: MLModel  # MLModel?
    self.queue: None  # DispatchQueue
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    self.modelURL = _url
    self.configuration = _configuration
    self.loadedModel = None

  def loadModel(self):
    modelURL = nsurl(str(self.modelURL.resolve()))
    self.loadedModel = MLModel.modelWithContentsOfURL_configuration_error_(
      modelURL, self.configuration, None)
    pdbg.state(self.loadedModel.modelDescription().inputDescriptionsByName().allValues()[0].multiArrayConstraint().shape())

