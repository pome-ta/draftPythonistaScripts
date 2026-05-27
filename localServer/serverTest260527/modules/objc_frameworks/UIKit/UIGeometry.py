'''
//! Inlined from UIUtilities' UIGeometry.h, was moved from UIKit to there in
//! Xcode 26 (but it is unclear whether UIUtilities is intended to be
//! publicly exposed).
'''
# [geometry.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/geometry.rs.html#17-32)

from enum import IntEnum, IntFlag


# ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
class UIRectEdge(IntFlag):
  none = 0
  top = 1 << 0
  left = 1 << 1
  bottom = 1 << 2
  right = 1 << 3
  all = top | left | bottom | right

