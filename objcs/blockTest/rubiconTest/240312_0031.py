class BlockConsts:
  HAS_COPY_DISPOSE = 1 << 25
  HAS_CTOR = 1 << 26
  IS_GLOBAL = 1 << 28
  HAS_STRET = 1 << 29
  HAS_SIGNATURE = 1 << 30


flags = BlockConsts.HAS_STRET | BlockConsts.HAS_SIGNATURE | BlockConsts.HAS_COPY_DISPOSE

