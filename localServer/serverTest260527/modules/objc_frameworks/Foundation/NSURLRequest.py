from enum import IntEnum


class NSURLRequestCachePolicy(IntEnum):
  #[doc(alias = "NSURLRequestUseProtocolCachePolicy")]
  useProtocolCachePolicy = 0
  #[doc(alias = "NSURLRequestReloadIgnoringLocalCacheData")]
  reloadIgnoringLocalCacheData = 1
  #[doc(alias = "NSURLRequestReloadIgnoringLocalAndRemoteCacheData")]
  reloadIgnoringLocalAndRemoteCacheData = 4
  #[doc(alias = "NSURLRequestReloadIgnoringCacheData")]
  reloadIgnoringCacheData = reloadIgnoringLocalCacheData
  #[doc(alias = "NSURLRequestReturnCacheDataElseLoad")]
  returnCacheDataElseLoad = 2
  #[doc(alias = "NSURLRequestReturnCacheDataDontLoad")]
  returnCacheDataDontLoad = 3
  #[doc(alias = "NSURLRequestReloadRevalidatingCacheData")]
  reloadRevalidatingCacheData = 5

