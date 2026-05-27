from enum import IntEnum


class NSTextAlignment(IntEnum):
  #[doc(alias = "NSTextAlignmentLeft")]
  left = 0
  # ref: [text.rs - source](https://docs.rs/objc2-ui-kit/latest/src/objc2_ui_kit/text.rs.html#26)
  #[doc(alias = "NSTextAlignmentCenter")]
  center = 1  # wip: `TARGET_ABI_USES_IOS_VALUES`
  #[doc(alias = "NSTextAlignmentRight")]
  right = 2  # wip: `TARGET_ABI_USES_IOS_VALUES`
  #[doc(alias = "NSTextAlignmentJustified")]
  justified = 3
  # Resolved to either ``left`` or ``right`` based on the natural alignment resolution type active in the associated component.
  #
  # There are two types of natural alignment resolution behavior. The natural alignment is resolved based on either the UI language or the base writing direction.
  # The behavior is selected by the ``resolvesNaturalAlignmentWithBaseWritingDirection`` property for ``NSTextLayoutManager``.
  # ``NSStringDrawingOptions.resolvesNaturalAlignmentWithBaseWritingDirection`` specifies the base writing direction based resolution for ``NSStringDrawing``.
  #[doc(alias = "NSTextAlignmentNatural")]
  natural = 4

