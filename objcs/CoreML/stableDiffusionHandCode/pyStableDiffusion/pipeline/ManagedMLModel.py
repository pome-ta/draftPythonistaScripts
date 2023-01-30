from pathlib import Path

from objc_util import ObjCClass, NSURL, nsurl, on_main_thread

import pdbg

#load_framework('CoreML')
MLModel = ObjCClass('MLModel')


class ManagedMLModel:
  def __init__(self, url: Path, configuration):
    self.modelURL: NSURL
    self.configuration: None
    self.loadedModel: MLModel  # MLModel?
    self.queue: None  # DispatchQueue
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    url_path = str(_url.resolve())
    nsurl_path = NSURL.alloc().initFileURLWithPath_isDirectory_(url_path, 0)
    #nsurl_path = nsurl(url_path)

    self.modelURL = nsurl_path
    self.configuration = _configuration
    self.loadedModel = None

  #@on_main_thread
  def perform(self) -> MLModel:
    self._loadModel()
    return self.loadedModel

  def _loadModel(self):
    if not (self.loadedModel):
      self.loadedModel = MLModel.modelWithContentsOfURL_configuration_error_(
        self.modelURL, self.configuration, None)
      #pdbg.state(self.loadedModel)

