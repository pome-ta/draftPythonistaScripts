from pathlib import Path

from objc_util import ObjCClass, nsurl, autoreleasepool, load_framework

import pdbg

#load_framework('CoreML')
MLModel = ObjCClass('MLModel')


class ManagedMLModel:
  def __init__(self, url: Path, configuration):
    self.modelURL: Path
    self.configuration: None
    self.loadedModel: MLModel  # MLModel?
    self.queue: None  # DispatchQueue
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    url = str(_url.resolve())
    ns_url = nsurl(url)
    print(ns_url)
    self.modelURL = ns_url
    self.configuration = _configuration
    self.loadedModel = None

  def perform(self) -> MLModel:
    self._loadModel()
    return self.loadedModel

  def _loadModel(self):
    if not (self.loadedModel):
      self.loadedModel = MLModel.modelWithContentsOfURL_configuration_error_(
        self.modelURL, self.configuration, None)

