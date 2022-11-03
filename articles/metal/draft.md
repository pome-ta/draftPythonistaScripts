# Metal for Pythonista3

Pythonista3 で、Metal Framework を呼び出し実行する

## Pythonista のModules

### `ui` — Native GUI for iOS

UI を作成。

### `objc_util` — Utilities for bridging Objective-C APIs

Pythonista の`ui`module で呼び出せないものを呼び出す。

Metal の処理を呼ぶ。

## Metal Framework を呼び出す

ui で、`ViewController` 機能を作りそのView に背景色を設定。

### `ui` の初期設定

Metal を表示させるView

``` .py
class PyMetal(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    # `view` の背景
    self.bg_color = 'slategray'

if __name__ == '__main__':
  view = PyMetal()
  view.present(style='fullscreen', orientations=['portrait'])

```

`self.bg_color = 'slategray'` は、`ViewController` の背景のため、今後この色が出ることはない

### Metal を呼び出せるようにする

`clearColor` を設定し、`ui` の背景をMetal のView にさせる

#### `MTLCreateSystemDefaultDevice`

いきなり裏技的な呼び出しとなる。

``` .py
MTLCreateSystemDefaultDevice = c.MTLCreateSystemDefaultDevice
MTLCreateSystemDefaultDevice.argtypes = []
MTLCreateSystemDefaultDevice.restype = ctypes.c_void_p
```

[MTLCreateSystemDefaultDevice](https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice?language=objc) は、Function なので、`ctypes` を使い定義。インスタンス化することで、Pythonista で使えるようになる。

詳細は後述予定だが、`objc_util.c` で引っ張ってこれる

#### `MTKView`

Pythonistaの `ui.View` を`objc_util` 連動できるようにインスタンス化し、`self.objc_instance.addSubview_(mtkView)`

[MTKView](https://developer.apple.com/documentation/metalkit/mtkview?language=objc) は、Class なので`MTKView = ObjCClass('MTKView')`

`objc_util` は、objc の書き方に近い

#### `MTKViewDelegate`

Metal 側は、毎フレームのループ処理をするので`delegate` を作成

`objc_util.create_objc_class` を使い生成。`NSObject` を`superclass` として、`protocols` に、`MTKViewDelegate` を指定

[MTKViewDelegate](https://developer.apple.com/documentation/metalkit/mtkviewdelegate?language=objc) にあるように、Required のインスタンスメソッドを関数定義し、`methods` に、配列で格納

Swift の`override` や、`extension` での、イニシャライズ宣言が難しかったので

`PyMetal(ui.View)` 内のメソッドで事前に定義し、イニシャライズを代用

``` .py

  def delegate_init(self, delegate_cls, mtk_view):
    renderer = delegate_cls.alloc().init()
    device = mtk_view.device()
    renderer.commandQueue = device.newCommandQueue()
    return renderer

```

#### `MTLClearColor`

[MTLClearColor](https://developer.apple.com/documentation/metal/mtlclearcolor?language=objc) のように、実態はPython でも表現できるような構造体は、(自分が判断できる程度で)直接指定

``` .py
                  # red, green, blue, alpha
wenderlichGreen = ( 0.0,   0.4, 0.21,   1.0)
```

今後、Vertices 等のPython の型ではフォローアップが難しい場合には、`ctypes` より型を指定する

## `ui` module の補足

`ui` を継承して、コードを書いていく

``` .py

ui.present()

```

でView が出せる

### `present` の引数

- `style='fullscreen'`
  - フルスクリーンで描画。iPhone の端末だと気がつかないが、iPad だと、小さなView になる
  - document だと、`full_screen` だけど、`fullscreen` が正っぽい
- `orientations=['portrait']`
  - 縦向きで固定
  - 横向き(Landscape) レイアウトを考えるのが面倒なため
