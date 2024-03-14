from ctypes import byref, cast, Structure

from objc import ObjCClass, ObjCInstance
from objc.runtime import objc_id, load_library
#from objc.eventloop import EventLoopPolicy, iOSLifecycle

#from objc_util import on_main_thread

import pdbr


libSystem = load_library('System')
libdispatch = libSystem

class struct_dispatch_queue_s(Structure):
    pass # No _fields_, because this is an opaque structure.

_dispatch_main_q = struct_dispatch_queue_s.in_dll(libdispatch, '_dispatch_main_q')


UIViewController = ObjCClass('UIViewController')
NSThread = ObjCClass('NSThread')

app = ObjCClass('UIApplication').sharedApplication
window = app.keyWindow if app.keyWindow else app.windows[0]
root_vc = window.rootViewController

while root_vc.presentedViewController:
  root_vc = root_vc.presentedViewController

vc = UIViewController.new()
vc.setModalPresentationStyle_(1)
#root_vc.presentViewController_animated_completion_(vc, True, None)

#pdbr.state(NSThread.isMainThread)
print(NSThread.isMainThread)
def dispatch_get_main_queue():
  return ObjCInstance(cast(byref(_dispatch_main_q), objc_id))
