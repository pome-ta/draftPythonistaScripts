# 📝 2023/10/20

## encoding 調査

```.py
device = MTLCreateSystemDefaultDevice()
allocator = MTKMeshBufferAllocator.alloc().initWithDevice_(device)
```

`device` が引数の場合。


`encoding` はどうなってるか？

```
'encoding': b'@24@0:8@16'
```



```
# --- name______
<objc_util.ObjCInstanceMethod object at 0x110d31e10>
# --- vars( )______
{'_objc_msgSend': None,
 'encoding': b'@24@0:8@16',
 'method': 8977835473,
 'obj': <b'MTKMeshBufferAllocator': <MTKMeshBufferAllocator: 0x283b30440>>,
 'sel_name': 'initWithDevice:'}
# --- dir( )______
['__call__',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_objc_msgSend',
 'encoding',
 'method',
 'obj',
 'sel_name']


```

## `initSphereWithExtent:segments:inwardNormals:geometryType:allocator:`

```
# --- name______
<objc_util.ObjCInstanceMethod object at 0x1113c8430>
# --- vars( )______
{'_objc_msgSend': None,
 'encoding': b'@60@0:81632B40q44@52',
 'method': 8834873001,
 'obj': <b'MDLMesh': <<MDLMesh: 0x16d7e78c8>, Name: Obj0, VertexCount: 0, VertexBufferCount: 0>>,
 'sel_name': 'initSphereWithExtent:segments:inwardNormals:geometryType:allocator:'}
# --- dir( )______
['__call__',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_objc_msgSend',
 'encoding',
 'method',
 'obj',
 'sel_name']

```

## `MDLMesh`


```.py
MDLMesh = ObjCClass('MDLMesh')
```

↓

```
# --- name______
<objc_util.ObjCClass object at 0x11467cfa0>
# --- vars( )______
{'_as_parameter_': 9900055248,
 '_cached_methods': {},
 'class_name': b'MDLMesh',
 'ptr': 9900055248}
# --- dir( )______
['alloc',
 'cancelPreviousPerformRequestsWithTarget_',
 'cancelPreviousPerformRequestsWithTarget_selector_object_',
 'description',
 'instancesRespondToSelector_',
 'isSubclassOfClass_',
 'new',
 'newBoxWithDimensions_segments_geometryType_inwardNormals_allocator_',
 'newCapsuleWithHeight_radii_radialSegments_verticalSegments_hemisphereSegments_geometryType_inwardNormals_allocator_',
 'newCylinderWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_',
 'newEllipsoidWithRadii_radialSegments_verticalSegments_geometryType_inwardNormals_hemisphere_allocator_',
 'newEllipticalConeWithHeight_radii_radialSegments_verticalSegments_geometryType_inwardNormals_allocator_',
 'newIcosahedronWithRadius_inwardNormals_allocator_',
 'newIcosahedronWithRadius_inwardNormals_geometryType_allocator_',
 'newPlaneWithDimensions_segments_geometryType_allocator_',
 'newSubdividedMesh_submeshIndex_subdivisionLevels_',
 'superclass']


```
