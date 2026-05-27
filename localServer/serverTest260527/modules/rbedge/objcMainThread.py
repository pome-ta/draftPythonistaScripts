import functools

from pyrubicon.objc.api import Block, ObjCClass, ObjCInstance
from pyrubicon.objc.runtime import libobjc, objc_block, objc_id

from objc_frameworks.Dispatch import (
  dispatch_get_main_queue,
  dispatch_sync,
  dispatch_async,
)

NSThread = ObjCClass('NSThread')


def onMainThread(func=None, *, sync=True):
  if func is None:
    return functools.partial(onMainThread, sync=sync)

  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    if NSThread.isMainThread:
      return func(*args, **kwargs)

    queue = dispatch_get_main_queue()
    results = []  # 戻り値キャプチャ用

    def task():
      res = func(*args, **kwargs)
      results.append(res)

    block = Block(task, None)

    if sync:
      dispatch_sync(queue, block)
      return results[0] if results else None
    else:
      dispatch_async(queue, block)
      return None  # asyncは戻り値なし

  return wrapper

