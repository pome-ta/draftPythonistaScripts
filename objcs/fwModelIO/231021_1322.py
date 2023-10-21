import ctypes

import numpy as np

from objc_util import ObjCClass, ObjCInstance, c,ns
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
mdlMesh.initSphereWithExtent_segments_inwardNormals_geometryType_allocator_([0.75,0.75,0.75], [10, 10], False, 3, allocator)

pdbg.state(mdlMesh)
