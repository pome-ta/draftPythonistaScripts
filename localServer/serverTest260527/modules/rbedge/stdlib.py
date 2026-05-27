'''
rubicon の`libc` 依存ではなく、c で処理
'''

import ctypes

_libc = ctypes.CDLL(None)


def arc4random_uniform(value: int) -> int:
  if value < 0:
    raise ValueError('value must be >= 0')
  try:
    _func = arc4random_uniform._cfunc
  except AttributeError:
    _func = _libc.arc4random_uniform
    _func.restype = ctypes.c_uint32
    _func.argtypes = [
      ctypes.c_uint32,
    ]
    arc4random_uniform._cfunc = _func

  return _func(value)


def drand48() -> float:
  try:
    _func = drand48._cfunc
  except AttributeError:
    _func = _libc.drand48
    _func.restype = ctypes.c_double
    _func.argtypes = []
    drand48._cfunc = _func

  return _func()


if __name__ == '__main__':
  pass

