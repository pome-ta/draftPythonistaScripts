from pathlib import Path

from objc_util import ObjCClass, NSURL, nsurl, on_main_thread, ns

import pdbg

#load_framework('CoreML')
MLModel = ObjCClass('MLModel')

NSFileManager = ObjCClass('NSFileManager')

NSApplicationSupportDirectory = 14
NSUserDomainMask = 1


class ManagedMLModel:
  def __init__(self, url: Path, configuration):
    self.modelURL: NSURL
    self.configuration: None
    self.loadedModel: MLModel  # MLModel?
    self.queue: None  # DispatchQueue
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    url_path = str(_url.resolve())
    compiledModelURL = NSURL.alloc().initFileURLWithPath_isDirectory_(
      url_path, 0)

    '''
    fileManager = NSFileManager.defaultManager()
    appSupportURL = fileManager.URLsForDirectory_inDomains_(
      NSApplicationSupportDirectory, NSUserDomainMask).firstObject()

    compiledModelName = compiledModelURL.lastPathComponent()

    permanentURL = appSupportURL.URLByAppendingPathComponent_(
      compiledModelName)

    _ = fileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_(
      permanentURL, compiledModelURL, None, 2, None, None)
    '''

    self.modelURL = compiledModelURL
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

