# 📝 2023/01/11

mac 側で、実機log 確認

```swift
/// Read merges.txt file at URL into a dictionary mapping bigrams to the line number/rank/priority
static func readMerges(url: URL) throws -> [TokenPair: Int] {
    let content = try String(contentsOf: url)
    let lines = content.split(separator: "\n")

    let merges: [(TokenPair, Int)] = try lines.enumerated().compactMap { (index, line) in
        if line.hasPrefix("#") {
            return nil
        }
        let pair = line.split(separator: " ")
        if pair.count != 2 {
            print("FileReadError")
            print(FileReadError.invalidMergeFileLine(index+1))
            throw FileReadError.invalidMergeFileLine(index+1)
        }
        return (TokenPair(String(pair[0]), String(pair[1])),index)
    }
    print("merges")
    print(merges[0...50])
    print(type(of: merges))
    return [TokenPair : Int](uniqueKeysWithValues: merges)
}
```

```log
merges
[
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "n"), 1),
  (StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "h"), 2),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "n"), 3),
  (StableDiffusion.BPETokenizer.TokenPair(first: "r", second: "e"), 4),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "r"), 5),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "r"), 6),
  (StableDiffusion.BPETokenizer.TokenPair(first: "th", second: "e</w>"), 7),
  (StableDiffusion.BPETokenizer.TokenPair(first: "in", second: "g</w>"), 8),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "u"), 9),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "n"), 10),
  (StableDiffusion.BPETokenizer.TokenPair(first: "s", second: "t"), 11),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "r"), 12),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "n"), 13),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "n</w>"), 14),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "l"), 15),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t"), 16),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "r</w>"), 17),
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "t"), 18),
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "n</w>"), 19),
  (StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "o</w>"), 20),
  (StableDiffusion.BPETokenizer.TokenPair(first: "r", second: "o"), 21),
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "s</w>"), 22),
  (StableDiffusion.BPETokenizer.TokenPair(first: "l", second: "e"), 23),
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "c"), 24),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"), 25),
  (StableDiffusion.BPETokenizer.TokenPair(first: "an", second: "d</w>"), 26),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "d</w>"), 27),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "f</w>"), 28),
  (StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "h"), 29),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "r</w>"), 30),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "s</w>"), 31),
  (StableDiffusion.BPETokenizer.TokenPair(first: "i", second: "l"), 32),
  (StableDiffusion.BPETokenizer.TokenPair(first: "e", second: "l"), 33),
  (StableDiffusion.BPETokenizer.TokenPair(first: "s", second: "t</w>"), 34),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "c"), 35),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "m"), 36),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "m"), 37),
  (StableDiffusion.BPETokenizer.TokenPair(first: "l", second: "o"), 38),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "n</w>"), 39),
  (StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "y</w>"), 40),
  (StableDiffusion.BPETokenizer.TokenPair(first: "s", second: "h"), 41),
  (StableDiffusion.BPETokenizer.TokenPair(first: "r", second: "i"), 42),
  (StableDiffusion.BPETokenizer.TokenPair(first: "l", second: "i"), 43),
  (StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "i"), 44),
  (StableDiffusion.BPETokenizer.TokenPair(first: "f", second: "or</w>"), 45),
  (StableDiffusion.BPETokenizer.TokenPair(first: "n", second: "e"), 46),
  (StableDiffusion.BPETokenizer.TokenPair(first: "ð", second: "Ł"), 47),
  (StableDiffusion.BPETokenizer.TokenPair(first: "r", second: "a"), 48),
  (StableDiffusion.BPETokenizer.TokenPair(first: "h", second: "a"), 49),
  (StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "e"), 50),
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "l"), 51)
]
Array<(TokenPair, Int)>
```

`throw FileReadError.invalidMergeFileLine(index+1)` は出ていないかな？

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
