from pathlib import Path


class ManagedMLModel:
  def __init__(self, url: Path, configuration):
    self.modelURL: Path
    self.configuration: None
    self.loadedModel: None  # MLModel?
    self.queue: None  # DispatchQueue
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    self.modelURL = _url
    self.configuration = _configuration
    self.loadedModel = None
