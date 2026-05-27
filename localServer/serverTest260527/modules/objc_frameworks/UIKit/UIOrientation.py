from enum import IntEnum


class UIDeviceOrientation(IntEnum):
  #[doc(alias = "UIDeviceOrientationUnknown")]
  unknown = 0
  #[doc(alias = "UIDeviceOrientationPortrait")]
  portrait = 1
  #[doc(alias = "UIDeviceOrientationPortraitUpsideDown")]
  portraitUpsideDown = 2
  #[doc(alias = "UIDeviceOrientationLandscapeLeft")]
  landscapeLeft = 3
  #[doc(alias = "UIDeviceOrientationLandscapeRight")]
  landscapeRight = 4
  #[doc(alias = "UIDeviceOrientationFaceUp")]
  faceUp = 5
  #[doc(alias = "UIDeviceOrientationFaceDown")]
  faceDown = 6


class UIInterfaceOrientation(IntEnum):
  #[doc(alias = "UIInterfaceOrientationUnknown")]
  unknown = UIDeviceOrientation.unknown
  #[doc(alias = "UIInterfaceOrientationPortrait")]
  portrait = UIDeviceOrientation.portrait
  #[doc(alias = "UIInterfaceOrientationPortraitUpsideDown")]
  portraitUpsideDown = UIDeviceOrientation.portraitUpsideDown
  #[doc(alias = "UIInterfaceOrientationLandscapeLeft")]
  landscapeLeft = UIDeviceOrientation.landscapeRight
  #[doc(alias = "UIInterfaceOrientationLandscapeRight")]
  landscapeRight = UIDeviceOrientation.landscapeLeft


'''
# wip: 拾えない？
def UIInterfaceOrientationIsPortrait(
    orientation: UIInterfaceOrientation) -> bool:
  pass

  _function = UIKit.UIInterfaceOrientationIsPortrait
  _function.restype = bool
  _function.argtypes = [
    UIInterfaceOrientation,
  ]
  return _function(orientation)
'''

