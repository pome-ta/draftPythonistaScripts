from enum import IntFlag


class NSKeyValueObservingOptions(IntFlag):
  #[doc(alias = "NSKeyValueObservingOptionNew")]
  new = 0x01
  #[doc(alias = "NSKeyValueObservingOptionOld")]
  old = 0x02
  #[doc(alias = "NSKeyValueObservingOptionInitial")]
  initial = 0x04
  #[doc(alias = "NSKeyValueObservingOptionPrior")]
  prior = 0x08

