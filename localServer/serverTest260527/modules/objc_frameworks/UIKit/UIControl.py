from enum import IntEnum


class UIControlEvents(IntEnum):

  #[doc(alias = "UIControlEventTouchDown")]
  touchDown = 1 << 0
  #[doc(alias = "UIControlEventTouchDownRepeat")]
  touchDownRepeat = 1 << 1
  #[doc(alias = "UIControlEventTouchDragInside")]
  touchDragInside = 1 << 2
  #[doc(alias = "UIControlEventTouchDragOutside")]
  touchDragOutside = 1 << 3
  #[doc(alias = "UIControlEventTouchDragEnter")]
  touchDragEnter = 1 << 4
  #[doc(alias = "UIControlEventTouchDragExit")]
  touchDragExit = 1 << 5
  #[doc(alias = "UIControlEventTouchUpInside")]
  touchUpInside = 1 << 6
  #[doc(alias = "UIControlEventTouchUpOutside")]
  touchUpOutside = 1 << 7
  #[doc(alias = "UIControlEventTouchCancel")]
  touchCancel = 1 << 8
  #[doc(alias = "UIControlEventValueChanged")]
  valueChanged = 1 << 12
  #[doc(alias = "UIControlEventPrimaryActionTriggered")]
  primaryActionTriggered = 1 << 13
  #[doc(alias = "UIControlEventMenuActionTriggered")]
  menuActionTriggered = 1 << 14
  #[doc(alias = "UIControlEventEditingDidBegin")]
  editingDidBegin = 1 << 16
  #[doc(alias = "UIControlEventEditingChanged")]
  editingChanged = 1 << 17
  #[doc(alias = "UIControlEventEditingDidEnd")]
  editingDidEnd = 1 << 18
  #[doc(alias = "UIControlEventEditingDidEndOnExit")]
  editingDidEndOnExit = 1 << 19
  #[doc(alias = "UIControlEventAllTouchEvents")]
  allTouchEvents = 0x00000FFF
  #[doc(alias = "UIControlEventAllEditingEvents")]
  allEditingEvents = 0x000F0000
  #[doc(alias = "UIControlEventApplicationReserved")]
  applicationReserved = 0x0F000000
  #[doc(alias = "UIControlEventSystemReserved")]
  systemReserved = 0xF0000000
  #[doc(alias = "UIControlEventAllEvents")]
  allEvents = 0xFFFFFFFF

