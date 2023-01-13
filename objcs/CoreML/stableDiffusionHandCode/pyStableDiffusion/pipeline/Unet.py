from pathlib import Path
from .ManagedMLModel import ManagedMLModel


class Unet:
  def __init__(self, url: Path, configuration):
    self.models: ManagedMLModel
    self.init_modelAt_configuration_(url, configuration)

  def init_modelAt_configuration_(self, _url: Path, _configuration):
    self.models = ManagedMLModel(_url, _configuration)

