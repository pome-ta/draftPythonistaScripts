from enum import IntFlag


class UIMenuElementAttributes(IntFlag):
  #[doc(alias = "UIMenuElementAttributesDisabled")]
  disabled = 1 << 0
  #[doc(alias = "UIMenuElementAttributesDestructive")]
  destructive = 1 << 1
  #[doc(alias = "UIMenuElementAttributesHidden")]
  hidden = 1 << 2
  '''
  /// Indicates that the menu should remain presented after firing
  /// the element's action rather than dismissing as it normally does.
  /// This attribute has no effect on Mac Catalyst.
  '''
  #[doc(alias = "UIMenuElementAttributesKeepsMenuPresented")]
  keepsMenuPresented = 1 << 3

