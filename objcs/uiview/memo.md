# 📝 2023/09/05

## `create_objc_class` のMethod

Python の型ヒントを書くと認識されない

```
ValueError: Function has keyword-only parameters or annotations, use inspect.signature() API which can support them

```

### NG

```.py
def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText) -> None:
  print(f'01 : searchBar_textDidChange_')
  pass
```

### OK

```.py
def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText):
  print(f'01 : searchBar_textDidChange_')
  pass
```

# 📝 2023/09/03

## `ui.View` と`UIView`

メソッドの違いは数箇所のみ

- `SUIView`
- `clipsToBounds`
- `stringRepresentation`
- `name`
- `pyObject`
- `setName_`
- `setPyObject_`
- `stringRepresentation`
- `willDismiss`

## `setAutoresizingMask_`

`frame = (0 0; 314 704); autoresize = W+H;`

# 📝 2023/09/02

`UIView` やら、`UIViewController` の調査

# 📝 2022/11/02

作成
