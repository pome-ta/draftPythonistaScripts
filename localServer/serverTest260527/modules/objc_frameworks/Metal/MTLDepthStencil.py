from enum import IntEnum


class MTLCompareFunction(IntEnum):
  #[doc(alias = "MTLCompareFunctionNever")]
  never = 0
  #[doc(alias = "MTLCompareFunctionLess")]
  less = 1
  #[doc(alias = "MTLCompareFunctionEqual")]
  equal = 2
  #[doc(alias = "MTLCompareFunctionLessEqual")]
  lessEqual = 3
  #[doc(alias = "MTLCompareFunctionGreater")]
  greater = 4
  #[doc(alias = "MTLCompareFunctionNotEqual")]
  notEqual = 5
  #[doc(alias = "MTLCompareFunctionGreaterEqual")]
  greaterEqual = 6
  #[doc(alias = "MTLCompareFunctionAlways")]
  always = 7

