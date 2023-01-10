# 📝 2023/01/09

`FileManager.default.fileExists`


- UnetChunk1
- UnetChunk2

持ってないけど、途中で処理する


ギリギリまで、Python の`Path` で持たせて、呼び出す時に`nsurl` にする方針にしてみる



`BPETokenizer` struct で`init` が2つある。


[pythonで良い感じのシングルトンを書く - Blanktar](https://blanktar.jp/blog/2016/07/python-singleton)


[Python の __new__ ってなに？ | 民主主義に乾杯](https://python.ms/new/#_1-new-%E3%81%A8-init-%E3%81%AE%E9%81%95%E3%81%84)


[クラスメソッドの使いどころを考えたけど分からなかった - Qiita](https://qiita.com/tagtagtag/items/6aa430e813b146047a5b)



[【Swift】Arrayの便利な変換関数たち | 2速で歩くヒト](https://www.2nd-walker.com/2020/09/02/swift-convenient-transforming-functions-of-array/#compactMap)

`compactMap` は、`null` 入れない


# 📝 2023/01/08


[【Swift】iOSでStableDiffusionを使ってみた - Qiita](https://qiita.com/SNQ-2001/items/2d33dc535cf106189f75)


[【SwiftUI】Core ML Stable Diffusionをアプリに実装する サンプルコード | thwork](https://thwork.net/2022/12/07/swiftui_core-ml-stable-diffusion_app_sample/)




## 調査流れ

### `guard let resourceURL = Bundle.main.resourceURL` をしれっと取得したい


```python
from objc_util import NSBundle
import pdbg

pdbg.state(NSBundle.mainBundle())
# `Pythonista3.App` がloaded

```




`.ひ/iproj/iOSstableDiffusionDEMO/ViewModel.swift`

```ViewModel.swift
func loadModels() async {
  guard let resourceURL = Bundle.main.resourceURL else { return }
  do {
    Task.detached { @MainActor in
      self.status = .loadStart
    }
    let pipeline = try StableDiffusionPipeline(resourcesAt: resourceURL)
    Task.detached { @MainActor in
      self.pipeline = pipeline
      self.status = .loadFinish
    }
  } catch {
    Task.detached { @MainActor in
      self.status = .error
    }
  }
}
    
```

### `let pipeline` を取る


`./ml-stable-diffusion/swift/StableDiffusion/pipeline/StableDiffusionPipeline+Resources.swift`




# 📝 2023/01/05


データ取得側からか、処理側からかわからんくなってきてる


# 📝 2023/01/03

xcode からでも遅いし、本機だと落ちるけどやってみる

