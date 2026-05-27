from enum import IntEnum


class UILayoutConstraintAxis(IntEnum):
  horizontal = 0
  vertical = 1


class UIViewAutoresizing(IntEnum):
  #[doc(alias = "UIViewAutoresizingNone")]
  none = 0
  #[doc(alias = "UIViewAutoresizingFlexibleLeftMargin")]
  flexibleLeftMargin = 1 << 0
  #[doc(alias = "UIViewAutoresizingFlexibleWidth")]
  flexibleWidth = 1 << 1
  #[doc(alias = "UIViewAutoresizingFlexibleRightMargin")]
  flexibleRightMargin = 1 << 2
  #[doc(alias = "UIViewAutoresizingFlexibleTopMargin")]
  flexibleTopMargin = 1 << 3
  #[doc(alias = "UIViewAutoresizingFlexibleHeight")]
  flexibleHeight = 1 << 4
  #[doc(alias = "UIViewAutoresizingFlexibleBottomMargin")]
  flexibleBottomMargin = 1 << 5

