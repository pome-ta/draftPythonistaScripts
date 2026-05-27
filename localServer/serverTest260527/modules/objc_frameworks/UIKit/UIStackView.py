from enum import IntEnum


class UIStackViewDistribution(IntEnum):
  #[doc(alias = "UIStackViewDistributionFill")]
  fill = 0
  #[doc(alias = "UIStackViewDistributionFillEqually")]
  fillEqually = 1
  #[doc(alias = "UIStackViewDistributionFillProportionally")]
  fillProportionally = 2
  #[doc(alias = "UIStackViewDistributionEqualSpacing")]
  equalSpacing = 3
  #[doc(alias = "UIStackViewDistributionEqualCentering")]
  equalCentering = 4


class UIStackViewAlignment(IntEnum):
  #[doc(alias = "UIStackViewAlignmentFill")]
  fill = 0
  #[doc(alias = "UIStackViewAlignmentLeading")]
  leading = 1
  #[doc(alias = "UIStackViewAlignmentTop")]
  top = leading
  #[doc(alias = "UIStackViewAlignmentFirstBaseline")]
  firstBaseline = 2
  #[doc(alias = "UIStackViewAlignmentCenter")]
  center = 3
  #[doc(alias = "UIStackViewAlignmentTrailing")]
  trailing = 4
  #[doc(alias = "UIStackViewAlignmentBottom")]
  bottom = trailing
  #[doc(alias = "UIStackViewAlignmentLastBaseline")]
  lastBaseline = 5

