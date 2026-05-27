from enum import IntEnum, IntFlag


# ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
class UIModalPresentationStyle(IntEnum):
  automatic = -2
  none = -1
  fullScreen = 0
  pageSheet = 1
  formSheet = 2
  currentContext = 3
  custom = 4
  overFullScreen = 5
  overCurrentContext = 6
  popover = 7
  blurOverFullScreen = 8

