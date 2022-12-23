# sceneKit のsimd

[SCNMatrix4MakeRotation | Apple Developer Documentation](https://developer.apple.com/documentation/scenekit/1409686-scnmatrix4makerotation?language=objc)

[SCNMatrix4 | Apple Developer Documentation](https://developer.apple.com/documentation/scenekit/scnmatrix4?language=objc)

xcode のやつ

```swift
lightNode.position = SCNVector3(x: 0, y: 10, z: 10)
print("lightNode ---")
print(lightNode.transform)
print(lightNode.position)

planeNode.transform = SCNMatrix4MakeRotation(-Float.pi / 2.0, 1, 0, 0)
print("planeNode ---")
print(planeNode.transform)

```

```log
lightNode ---
SCNMatrix4(
 m11: 1.0, m12: 0.0, m13: 0.0, m14: 0.0,
 m21: 0.0, m22: 1.0, m23: 0.0, m24: 0.0,
 m31: 0.0, m32: 0.0, m33: 1.0, m34: 0.0,
 m41: 0.0, m42: 10.0, m43: 10.0, m44: 1.0
)
SCNVector3(x: 0.0, y: 10.0, z: 10.0)

planeNode ---
SCNMatrix4(
 m11: 0.9999999, m12: 0.0        , m13:  0.0        , m14: 0.0,
 m21: 0.0      , m22: 7.54979e-08, m23: -0.99999994 , m24: 0.0,
 m31: 0.0      , m32: 0.99999994 , m33:  7.54979e-08, m34: 0.0,
 m41: 0.0      , m42: 0.0        , m43:  0.0        , m44: 1.0
)

```

playground のやつ

```swift
import SceneKit
let rotateMat = SCNMatrix4MakeRotation(-.pi/2, 1, 0, 0)
print(rotateMat)

```

```log
SCNMatrix4(
 m11: 0.9999999, m12: 0.0        , m13:  0.0        , m14: 0.0,
 m21: 0.0      , m22: 7.54979e-08, m23: -0.99999994 , m24: 0.0,
 m31: 0.0      , m32: 0.99999994 , m33:  7.54979e-08, m34: 0.0,
 m41: 0.0      , m42: 0.0        , m43:  0.0        , m44: 1.0
)

```

```python
pdbg.state(geometryNode.transform())
```

```log
# --- name______
<objc_util._struct_class_from_fields.<locals>.AnonymousStructure object at 0x124be9c48>
# --- vars( )______
{}
# --- dir( )______
['__class__',
 '__ctypes_from_outparam__',
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
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_b_base_',
 '_b_needsfree_',
 '_fields_',
 '_objects',
 'a',
 'b',
 'c',
 'd',
 'e',
 'f',
 'from_tuple',
 'g',
 'h',
 'i',
 'j',
 'k',
 'l',
 'm',
 'n',
 'o',
 'p']


```

```python
def struct_from_tuple(cls, t):
 args = []
 for i, field_value in enumerate(t):
  if isinstance(field_value, tuple):
   args.append(struct_from_tuple(cls._fields_[i][1], field_value))
  else:
   args.append(field_value)
 return cls(*args)


def _struct_class_from_fields(fields):
 class AnonymousStructure (Structure):
  from_tuple = classmethod(struct_from_tuple)
 struct_fields = []
 for i, field in enumerate(fields):
  if isinstance(field, tuple):
   struct_fields.append(field)
  else:
   struct_fields.append((string_lowercase[i], _struct_class_from_fields(field)))
   i += 1
 AnonymousStructure._fields_ = struct_fields
 return AnonymousStructure
```
