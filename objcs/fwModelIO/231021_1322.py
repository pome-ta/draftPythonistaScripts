import ctypes
from objc_util import ObjCClass, ObjCInstance, c
import pdbg

MTKMeshBufferAllocator = ObjCClass('MTKMeshBufferAllocator')
MDLMesh = ObjCClass('MDLMesh')


def MTLCreateSystemDefaultDevice():
  _MTLCreateSystemDefaultDevice = c.MTLCreateSystemDefaultDevice
  _MTLCreateSystemDefaultDevice.argtypes = []
  _MTLCreateSystemDefaultDevice.restype = ctypes.c_void_p
  return ObjCInstance(_MTLCreateSystemDefaultDevice())


device = MTLCreateSystemDefaultDevice()
allocator = MTKMeshBufferAllocator.alloc().initWithDevice_(device)

mdlMesh = MDLMesh.new()

pdbg.state(mdlMesh)
