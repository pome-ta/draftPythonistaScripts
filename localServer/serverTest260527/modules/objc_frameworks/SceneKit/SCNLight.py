from .constants import _get_const


class SCNLightType:
  IES = _get_const('SCNLightTypeIES')
  ambient = _get_const('SCNLightTypeAmbient')
  directional = _get_const('SCNLightTypeDirectional')
  omni = _get_const('SCNLightTypeOmni')
  probe = _get_const('SCNLightTypeProbe')
  spot = _get_const('SCNLightTypeSpot')
  area = _get_const('SCNLightTypeArea')

