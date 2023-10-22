import ctypes

import numpy as np

from objc_util import c, ObjCClass, ObjCInstance, load_framework
import pdbg

MTKMeshBufferAllocator = ObjCClass('MTKMeshBufferAllocator')
MDLMesh = ObjCClass('MDLMesh')

vector_float3 = np.dtype(
  {
    'names': ['x', 'y', 'z'],
    'formats': [np.float32, np.float32, np.float32],
    'offsets': [_offset * 4 for _offset in range(3)],
    'itemsize': 16,
  },
  align=True)

vector_uint2 = np.dtype(
  {
    'names': ['x', 'y'],
    'formats': [np.uint32, np.uint32],
    'offsets': [_offset * 4 for _offset in range(2)],
    'itemsize': 8,
  },
  align=True)


def MTLCreateSystemDefaultDevice():
  _MTLCreateSystemDefaultDevice = c.MTLCreateSystemDefaultDevice
  _MTLCreateSystemDefaultDevice.argtypes = []
  _MTLCreateSystemDefaultDevice.restype = ctypes.c_void_p
  return ObjCInstance(_MTLCreateSystemDefaultDevice())


device = MTLCreateSystemDefaultDevice()
allocator = MTKMeshBufferAllocator.alloc().initWithDevice_(device)

extent = np.array((0.75, 0.75, 0.75), dtype=vector_float3)
segments = np.array((100, 100), dtype=vector_uint2)
triangle = 3

#mdlMesh = MDLMesh.alloc().initSphereWithExtent_segments_inwardNormals_geometryType_allocator_(extent, segments, False, 3, allocator)

#mdlMesh = MDLMesh.alloc().initSphereWithExtent_segments_inwardNormals_geometryType_allocator_

mdlMesh = MDLMesh.alloc()#.init(extent=extent, segments=segments, inwardNormals=False, geometryType=triangle, allocator=allocator)

pdbg.state(mdlMesh)

