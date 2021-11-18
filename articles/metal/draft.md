# Metal for Pythonista3

Pythonista3 で、Metal Framework を呼び出し実行する


## Pythonista のModules

### `ui` — Native GUI for iOS

UI を作成する


### `objc_util` — Utilities for bridging Objective-C APIs

Pythonista の`ui`module で呼び出せないものを呼び出す


## Metal Framework を呼び出す


ui で、`ViewController` 機能を作りそのView に背景色を設定。


### `ui` の初期設定


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





