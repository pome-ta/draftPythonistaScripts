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
  (StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "l"), 51),

  (StableDiffusion.BPETokenizer.TokenPair(first: "un", second: "decided</w>"), 48857),
  (StableDiffusion.BPETokenizer.TokenPair(first: "so", second: "wn</w>"), 48858),
  (StableDiffusion.BPETokenizer.TokenPair(first: "rc", second: "n</w>"), 48859),
  (StableDiffusion.BPETokenizer.TokenPair(first: "north", second: "wales</w>"), 48860),
  (StableDiffusion.BPETokenizer.TokenPair(first: "htt", second: "r</w>"), 48861),
  (StableDiffusion.BPETokenizer.TokenPair(first: "fu", second: "mble</w>"), 48862),
  (StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "its</w>"), 48863),
  (StableDiffusion.BPETokenizer.TokenPair(first: "comp", second: "elled</w>"), 48864),
  (StableDiffusion.BPETokenizer.TokenPair(first: "popu", second: "list</w>"), 48865),
  (StableDiffusion.BPETokenizer.TokenPair(first: "min", second: "ted</w>"), 48866),
  (StableDiffusion.BPETokenizer.TokenPair(first: "blan", second: "chett</w>"), 48867),
  (StableDiffusion.BPETokenizer.TokenPair(first: ".", second: "\'\'</w>"), 48868),
  (StableDiffusion.BPETokenizer.TokenPair(first: "pro", second: "pulsion</w>"), 48869),
  (StableDiffusion.BPETokenizer.TokenPair(first: "m", second: "illa</w>"), 48870),
  (StableDiffusion.BPETokenizer.TokenPair(first: "au", second: "berg"), 48871),
  (StableDiffusion.BPETokenizer.TokenPair(first: "her", second: "tz</w>"), 48872),
  (StableDiffusion.BPETokenizer.TokenPair(first: "h", second: "ta</w>"), 48873),
  (StableDiffusion.BPETokenizer.TokenPair(first: "u", second: "daipur</w>"), 48874),
  (StableDiffusion.BPETokenizer.TokenPair(first: "serendip", second: "ity</w>"), 48875),
  (StableDiffusion.BPETokenizer.TokenPair(first: "azte", second: "cs</w>"), 48876),
  (StableDiffusion.BPETokenizer.TokenPair(first: "als", second: "ace</w>"), 48877),
  (StableDiffusion.BPETokenizer.TokenPair(first: "ðŁĲ", second: "ĳ</w>"), 48878),
  (StableDiffusion.BPETokenizer.TokenPair(first: "lu", second: "n</w>"), 48879),
  (StableDiffusion.BPETokenizer.TokenPair(first: "sho", second: "es"), 48880),
  (StableDiffusion.BPETokenizer.TokenPair(first: "char", second: "li</w>"), 48881),
  (StableDiffusion.BPETokenizer.TokenPair(first: "gar", second: "za</w>"), 48882),
  (StableDiffusion.BPETokenizer.TokenPair(first: "ðŁĴ", second: "Ł"), 48883),
  (StableDiffusion.BPETokenizer.TokenPair(first: "pro", second: "biotics</w>"), 48884),
  (StableDiffusion.BPETokenizer.TokenPair(first: "fox", second: "tv</w>"), 48885),
  (StableDiffusion.BPETokenizer.TokenPair(first: "ol", second: "is</w>"), 48886),
  (StableDiffusion.BPETokenizer.TokenPair(first: "mi", second: "ff"), 48887),
  (StableDiffusion.BPETokenizer.TokenPair(first: "loc", second: "alized</w>"), 48888),
  (StableDiffusion.BPETokenizer.TokenPair(first: "diffu", second: "ser</w>"), 48889),
  (StableDiffusion.BPETokenizer.TokenPair(first: "si", second: "gue</w>"), 48890),
  (StableDiffusion.BPETokenizer.TokenPair(first: "fun", second: "ko"), 48891),
  (StableDiffusion.BPETokenizer.TokenPair(first: "rend", second: "ous</w>"), 48892),
  (StableDiffusion.BPETokenizer.TokenPair(first: "ðŁĴ", second: "ĳ</w>"), 48893),
  (StableDiffusion.BPETokenizer.TokenPair(first: "jeky", second: "ll</w>"), 48894)],
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

[【Swift】Arrayの便利な変換関数たち | 2速で歩くヒト](https://www.2nd-walker.com/2020/09/02/swift-convenient-transforming-functions-of-array/#compactMap)

`compactMap` は、`null` 入れない

`for` で回せないと思っていたら、最終空行でエラー喰ってただけでした

# 📝 2023/01/08

[【Swift】iOSでStableDiffu

[【Swift】Arrayの便利な変換関数たち | 2速で歩くヒト](https://www.2nd-walker.com/2020/09/02/swift-convenient-transforming-functions-of-array/#compactMap)

`compactMap` は、`null` 入れない

```python
from objc_util import NSBundle
import pdbg

pdbg.state(NSBundle.mainBundle())
# `Pythonista3.App` がloaded

```

`./iproj/iOSstableDiffusionDEMO/ViewModel.swift`

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

## `let pipeline` を取る

`./ml-stable-diffusion/swift/StableDiffusion/pipeline/StableDiffusionPipeline+Resources.swift`

# 📝 2023/01/05

データ取得側からか、処理側からかわからんくなってきてる

# 📝 2023/01/03

xcode からでも遅いし、本機だと落ちるけどやってみる
