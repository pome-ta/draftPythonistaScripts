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
    #self.modelURL = _url
    self.modelURL = nsurl(str(_url.resolve()))
    self.configuration = _configuration
    self.loadedModel = None

  def perform(self):
    self._loadModel()
    return self.loadedModel

  def _loadModel(self):
    #modelURL = nsurl(str(self.modelURL.resolve()))
    #modelURL = self.modelURL
    self.loadedModel = MLModel.modelWithContentsOfURL_configuration_error_(
      self.modelURL, self.configuration, None)

