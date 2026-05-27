import asyncio
from pyrubicon.objc.eventloop import RubiconEventLoop

__all__ = [
  'loop',
]

loop = RubiconEventLoop()
asyncio.set_event_loop(loop)
'''
import asyncio
#import logging

from pyrubicon.objc.eventloop import EventLoopPolicy

__all__ = [
  'loop',
]

# wip: asyncio
#logging.basicConfig(level=logging.DEBUG)
print('flat s: loop')
asyncio.set_event_loop_policy(EventLoopPolicy())
#loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
#loop.set_debug(True)
print('flat e: loop')
'''

