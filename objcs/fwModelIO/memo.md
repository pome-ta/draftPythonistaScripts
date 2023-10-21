# 📝 2023/10/21


## error


```
raise TypeError('expected %i arguments, got %i' % (len(argtypes) - 2, len(args)))
TypeError: expected 3 arguments, got 5

```


## `new()`

```.py

MDLMesh = ObjCClass('MDLMesh')
mdlMesh = MDLMesh.new()
```


```
# --- name______
<b'MDLMesh': <<MDLMesh: 0x16f58bf58>, Name: Obj0, VertexCount: 0, VertexBufferCount: 0>>
# --- vars( )______
{'_as_parameter_': 10772961328,
 '_cached_methods': {'retain': <objc_util.ObjCInstanceMethodProxy object at 0x10f687370>},
 'ptr': 10772961328,
 'weakrefs': <WeakValueDictionary at 0x10f6873a0>}
# --- dir( )______
['_calculateFaceNormalsFromPositions_positionStride_normals_normalStride_creaseThreshold_',
 '_calculateTangentBasisFromPositions_positionStride_positionsBufferSize_normals_normalStride_normalsBufferSize_uvs_uvStride_uvsBufferSize_tangents_tangentsStride_tangentsBufferSize_bitagents_bitangentStride_bitangentsBufferSize_tangentFormat_selector_',
 '_createWithVertexBuffer_vertexCount_descriptor_submeshes_',
 '_enumerateSubmeshesUsingBlock_stopPointer_',
 'addAttributeWithName_format_',
 'addAttributeWithName_format_type_data_stride_',
 'addAttributeWithName_format_type_data_stride_time_',
 'addChild_',
 'addNormalsWithAttributeNamed_creaseThreshold_',
 'addOrthTanBasisForTextureCoordinateAttributeNamed_normalAttributeNamed_tangentAttributeNamed_',
 'addTangentBasisForTextureCoordinateAttributeNamed_normalAttributeNamed_tangentAttributeNamed_',
 'addTangentBasisForTextureCoordinateAttributeNamed_tangentAttributeNamed_bitangentAttributeNamed_',
 'addUnwrappedTextureCoordinatesForAttributeNamed_',
 'addVertexBuffer_',
 'allocator',
 'boundingBox',
 'boundingBoxAtTime_',
 'children',
 'componentConformingToProtocol_',
 'components',
 'controlNodeForINdex_',
 'copy',
 'copyDataVector_toAttr_',
 'createSourceDataVector_attr_srcElementCount_dstElementCount_',
 'dealloc',
 'debugPrintToFile_',
 'description',
 'enumerateChildObjectsOfClass_root_usingBlock_stopPointer_',
 'enumerateSubmeshesUsingBlock_',
 'flipTextureCoordinatesInAttributeNamed_',
 'generateAmbientOcclusionTextureWithQuality_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_',
 'generateAmbientOcclusionTextureWithSize_raysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_',
 'generateAmbientOcclusionVertexColorsWithQuality_attenuationFactor_objectsToConsider_vertexAttributeNamed_',
 'generateAmbientOcclusionVertexColorsWithRaysPerSample_attenuationFactor_objectsToConsider_vertexAttributeNamed_',
 'generateLightMapTextureWithQuality_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_',
 'generateLightMapTextureWithTextureSize_lightsToConsider_objectsToConsider_vertexAttributeNamed_materialPropertyNamed_',
 'generateLightMapVertexColorsWithLightsToConsider_objectsToConsider_vertexAttributeNamed_',
 'hidden',
 'init',
 'initBoxWithExtent_segments_inwardNormals_geometryType_allocator_',
 'initCapsuleWithExtent_cylinderSegments_hemisphereSegments_inwardNormals_geometryType_allocator_',
 'initConeWithExtent_segments_inwardNormals_cap_geometryType_allocator_',
 'initCylinderWithExtent_segments_inwardNormals_topCap_bottomCap_geometryType_allocator_',
 'initHemisphereWithExtent_segments_inwardNormals_cap_geometryType_allocator_',
 'initIcosahedronWithExtent_inwardNormals_geometryType_allocator_',
 'initMeshBySubdividingMesh_submeshIndex_subdivisionLevels_allocator_',
 'initPlaneWithExtent_segments_geometryType_allocator_',
 'initSphereWithExtent_segments_inwardNormals_geometryType_allocator_',
 'initWithBufferAllocator_',
 'initWithVertexBuffer_vertexCount_descriptor_submeshes_',
 'initWithVertexBuffers_vertexCount_descriptor_submeshes_',
 'instance',
 'inverseBasePoseForIndex_',
 'makeVerticesUnique',
 'makeVerticesUniqueAndReturnError_',
 'mutableCopy',
 'name',
 'objectAtPath_',
 'objectForKeyedSubscript_',
 'parent',
 'path',
 'performSelectorInBackground_withObject_',
 'performSelectorOnMainThread_withObject_waitUntilDone_',
 'performSelector_withObject_afterDelay_',
 'recursiveDescription',
 'removeAttributeNamed_',
 'replaceAttributeNamed_withData_',
 'setChildren_',
 'setComponent_forProtocol_',
 'setHidden_',
 'setInstance_',
 'setName_',
 'setObject_forKeyedSubscript_',
 'setParent_',
 'setSubdivisionScheme_',
 'setSubmeshes_',
 'setTransform_',
 'setVertexBuffers_',
 'setVertexCount_',
 'setVertexDescriptor_',
 'subdivisionScheme',
 'submeshCount',
 'submeshes',
 'transform',
 'triangulate',
 'updateAttributeNamed_withData_',
 'vertexAttributeDataForAttributeNamed_',
 'vertexAttributeDataForAttributeNamed_asFormat_',
 'vertexBuffers',
 'vertexCount',
 'vertexDescriptor']

```

# 📝 2023/10/20

## encoding 調査


[Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html)


よくわかってない ↑ を理解することになるのか、、、

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
