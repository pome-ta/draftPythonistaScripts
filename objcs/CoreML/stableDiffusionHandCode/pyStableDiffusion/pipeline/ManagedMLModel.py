from pathlib import Path


class ManagedMLModel:
  def __init__(self):
    self.modelURL: Path
    self.configuration: None
    self.loadedModel: None  # MLModel?
    self.queue: None  # DispatchQueue

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    self.modelURL = _url
    self.configuration = _configuration
    self.loadedModel = None
