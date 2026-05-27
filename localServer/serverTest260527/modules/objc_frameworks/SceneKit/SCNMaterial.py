from enum import IntEnum, IntFlag

from .constants import _get_const


class SCNLightingModel:
  blinn = _get_const('SCNLightingModelBlinn')
  constant = _get_const('SCNLightingModelConstant')
  lambert = _get_const('SCNLightingModelLambert')
  phong = _get_const('SCNLightingModelPhong')
  physicallyBased = _get_const('SCNLightingModelPhysicallyBased')
  shadowOnly = _get_const('SCNLightingModelShadowOnly')


class SCNFillMode(IntEnum):
  fill = 0
  lines = 1
