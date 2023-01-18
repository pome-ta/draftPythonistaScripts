# 📝 2023/01/18

## `merges` 同士のなにを比較しているのか

index の部分か？

```log
cat
  ["cat"]
pairs
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"),
    StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")
  ]
canMerge
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"),
    StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")
  ]
min
  $0
    25
  $1
    261
should
  TokenPair(first: "a", second: "t</w>")
update tokens
  [
    "c",
    "at</w>"
  ]
--- --- ---
pairs
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")
  ]
canMerge
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")
  ]
should
  TokenPair(first: "c", second: "at</w>")
update tokens
  ["cat</w>"]
--- --- ---
pairs
  []
canMerge
  []
tokens
  ["cat</w>"]
```

```log
dogs
  ["dogs"]
pairs
  [StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "g"),
  StableDiffusion.BPETokenizer.TokenPair(first: "g", second: "s</w>"),
  StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "o")
]
canMerge
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "g"),
    StableDiffusion.BPETokenizer.TokenPair(first: "g", second: "s</w>"),
    StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "o")
  ]
min
  $0
    11031
  $1
    834
  $0
    128
  $1
    834
should
  TokenPair(first: "d", second: "o")
update tokens
  [
    "do",
    "g",
    "s</w>"
  ]
--- --- ---
pairs
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "g"),
    StableDiffusion.BPETokenizer.TokenPair(first: "g", second: "s</w>")
  ]
canMerge
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "g"),
    StableDiffusion.BPETokenizer.TokenPair(first: "g", second: "s</w>")
  ]
min
  $0
    834
  $1
  3815
should
  TokenPair(first: "g", second: "s</w>")
update tokens
  [
    "do",
    "gs</w>"
  ]
--- --- ---
pairs
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "gs</w>")
  ]
canMerge
  [
    StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "gs</w>")
  ]
should
  TokenPair(first: "do", second: "gs</w>")
update tokens
  ["dogs</w>"]
--- --- ---
pairs
  []
canMerge
  []
tokens
  ["dogs</w>"]
```

# 📝 2023/01/17

## 実機実行調査

```log
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
should
TokenPair(first: "a", second: "t</w>")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
should
TokenPair(first: "c", second: "at</w>")
pairs
[]
canMerge
[]
tokens
["cat</w>"]
```

結局同じものが帰ってきている？

```log
caaaatttttt
["caaaatttttt"]
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
should
TokenPair(first: "a", second: "t")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
should
TokenPair(first: "c", second: "a")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "ca", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "t", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "t")]
should
TokenPair(first: "t", second: "t")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "tt"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "ca", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "tt"), StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "t</w>")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "at")]
should
TokenPair(first: "a", second: "a")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "tt"), StableDiffusion.BPETokenizer.TokenPair(first: "ca", second: "aa"), StableDiffusion.BPETokenizer.TokenPair(first: "aa", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "tt"), StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "t</w>")]
canMerge
[StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "t</w>")]
should
TokenPair(first: "tt", second: "t</w>")
pairs
[StableDiffusion.BPETokenizer.TokenPair(first: "ca", second: "aa"), StableDiffusion.BPETokenizer.TokenPair(first: "aa", second: "at"), StableDiffusion.BPETokenizer.TokenPair(first: "at", second: "tt"), StableDiffusion.BPETokenizer.TokenPair(first: "tt", second: "ttt</w>")]
canMerge
[]
tokens
["ca", "aa", "at", "tt", "ttt</w>"]
```

分割方法は変わるのか。。。

```log
tokens
["c", "a", "t</w>"]
tokens
["c", "at</w>"]
tokens
["cat</w>"]
```

```log
forEach
TokenPair(first: "c", second: "a")
TokenPair(first: "a", second: "t</w>")
```

```log
TokenPair(first: "c", second: "a")
261
```

## 実行調査メモ

Package として取り込んだものを、`[Show in Finder]`

Vim より、ゴリゴリと編集

`:w!` で強制上書き

もっと気軽な方法ないんかい。。。

# 📝 2023/01/16

```log
cat docs
["cat", "docs"]
encode tokens
["c", "a", "t"]
0..<3
if last
["c", "a", "t</w>"]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a"), StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>")]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
while
[]
[]
encode tokens
["d", "o", "c", "s"]
0..<4
if last
["d", "o", "c", "s</w>"]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "o"), StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "c"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "s</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "d", second: "o"), StableDiffusion.BPETokenizer.TokenPair(first: "o", second: "c"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "s</w>")]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "c"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "s</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "c"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "s</w>")]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "cs</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "do", second: "cs</w>")]
while
[]
[]

```

```log
while
[StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
[StableDiffusion.BPETokenizer.TokenPair(first: "a", second: "t</w>"), StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "a")]
while
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
[StableDiffusion.BPETokenizer.TokenPair(first: "c", second: "at</w>")]
while
[]
[]
```

```.swift
// cat `0..<3`
// docs `0..<4`
if let last = tokens.indices.last {
  tokens[last] = tokens[last] + "</w>"
}
```

```log
cat dog
["cat", "dog"]
encode tokens
["c", "a", "t"]
if last
["c", "a", "t</w>"]
encode tokens
["d", "o", "g"]
if last
["d", "o", "g</w>"]
bool
tokens
["<|startoftext|>", "cat</w>", "dog</w>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>"]
ids
[49406, 2368, 1929, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407]
```

```log
cat
["cat"]
encode tokens
["c", "a", "t"]
if last
["c", "a", "t</w>"]
bool
tokens
["<|startoftext|>", "cat</w>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>"]
ids
[49406, 2368, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407]
```

```log
cat
["cat"]
bool
tokens
["<|startoftext|>", "cat</w>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>", "<|endoftext|>"]
ids
[49406, 2368, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407, 49407]
```

# 📝 2023/01/14

## `@classmethod` してみる

呼び出し時、取り回し変数が解決？しかし、class 内部で処理というより、class 設計上の上をツルツルと動いている感覚

## TextEncoder の`encode`

### `encode` が2つある？

`public func` と、そのままの`func` 、、、

`public` 呼んでから、内部処理として呼ぶんか？

Python としては、`_encode` として、呼ぼうかな

```TextEncoder.swift
/// Encode input text/string
///
///  - Parameters:
///     - text: Input text to be tokenized and then embedded
///  - Returns: Embedding representing the input text
public func encode(_ text: String) throws -> MLShapedArray<Float32> {

    // Get models expected input length
    let inputLength = inputShape.last!

    // Tokenize, padding to the expected length
    var (tokens, ids) = tokenizer.tokenize(input: text, minCount: inputLength)

    // Truncate if necessary
    if ids.count > inputLength {
        tokens = tokens.dropLast(tokens.count - inputLength)
        ids = ids.dropLast(ids.count - inputLength)
        let truncated = tokenizer.decode(tokens: tokens)
        print("Needed to truncate input '\(text)' to '\(truncated)'")
    }

    // Use the model to generate the embedding
    return try encode(ids: ids)
}

/// Prediction queue
let queue = DispatchQueue(label: "textencoder.predict")

func encode(ids: [Int]) throws -> MLShapedArray<Float32> {
    let inputName = inputDescription.name
    let inputShape = inputShape

    let floatIds = ids.map { Float32($0) }
    let inputArray = MLShapedArray<Float32>(scalars: floatIds, shape: inputShape)
    let inputFeatures = try! MLDictionaryFeatureProvider(
        dictionary: [inputName: MLMultiArray(inputArray)])

    let result = try model.perform { model in
        try model.prediction(from: inputFeatures)
    }

    let embeddingFeature = result.featureValue(for: "last_hidden_state")
    return MLShapedArray<Float32>(converting: embeddingFeature!.multiArrayValue!)
}
```

### `inputShape` ってどこ？

下の方に定義してあったけど、

[MLFeatureDescription | Apple Developer Documentation](https://developer.apple.com/documentation/coreml/mlfeaturedescription?language=objc)

ここいらで何かをする感じか？

# 📝 2023/01/12

Python でclass 化を進めてみる

ディレクトリ名を`stableDiffusionHandCode` とrename して、`stableDiffusion` にモジュールとして突っ込む予定。

一つ一つ、写経のように丁寧にswift からPython へ書き換えているという意味で、`HandCode` とした。Hard Coding ではないので。

## class 化にあたり

- `BPETokenizer+Reading.swift`
- `StableDiffusionPipeline+Resources.swift`

と、`+` で合体していることとかあるから、色々と考えないと

モジュール作るの下手くそなので頑張る

[【Python】構造体をなにかで代用する方法 | ゆうまるブログ](https://yumarublog.com/python/struct/amp/)

### 親や兄弟階層のモジュール

正しい読み込み方法がわからん、単体で確認するものではない？

## モデルデータ管理

AirDrop で前飛ばなかったけなぁ。。

今回は、iPhone を繋いでどこかのApp につっこんでゴニョゴニョした

# 📝 2023/01/11

mac 側で、実機log 確認

`Dictionary<String, Int>`

```log
[
  "rugby": 15091, "arvo</w>": 45726, "mckinsey</w>": 48143, "oche</w>": 33045, "sible</w>": 14507, "usair": 36742, "))))</w>": 34181, "lof": 15011, "used": 32289, "elite": 32277, "ilian</w>": 10272, "marilyn</w>": 18489, "braves</w>": 14422, "lll</w>": 27177, "sall</w>": 20883, "counters</w>": 46170, "clemente</w>": 42461, "nando": 46044, "antigua</w>": 39910, "famed</w>": 23302, "infringe": 44882, "sentiments</w>": 47450, "yu": 3371, "chi</w>": 4039, "tuc</w>": 43871, "variety</w>": 8396, "circulating</w>": 42980, "huawei</w>": 21128, "commando</w>": 31361, "awesomeness</w>": 22430, "org</w>": 5593, "surrey</w>": 14315, "kurt</w>": 14527, "gta</w>": 15338, "relentless</w>": 27207, "ypg</w>": 37386, "comb": 3587, "gol": 1537, "dul": 6738, "provider</w>": 14409, "tris</w>": 29690, "adel": 4434, "carver</w>": 28850, "unders</w>": 20376, "going": 25787, "kamp</w>": 29522, "barnett</w>": 27650, "varun": 48120, "steamed</w>": 29007, "sakh</w>": 43945, "arche": 22474, "daan</w>": 44814, "outra": 14262, "ðŁİħ": 17685, "pieces</w>": 6194, "advancing</w>": 21355, "lum": 18112, "tues</w>": 12113, "misconduct</w>": 30601, "ddles</w>": 33901, "antv</w>": 47520, "dih</w>": 43089, "immense</w>": 22722, "ore</w>": 1423, "ritz": 39151, "oman": 22088, "huar": 46916, "smithsonian</w>": 31209, "vica</w>": 46168, "boulevard</w>": 19504, "kni": 6312, "gather": 36345, "salle</w>": 23738, "baking</w>": 11467, "ðŁ¤ĺðŁı»": 46449, "pope</w>": 9283, "dier</w>": 16394, "akest</w>": 46679, "bash</w>": 10972, "hl": 8297, "lpc</w>": 44092, "exclusion</w>": 40219, "raid</w>": 6877, "dman</w>": 18826, "meaningless</w>": 48932, "veen</w>": 22432, "peri": 12618, "equipped</w>": 18331, "candies</w>": 46305, "dera</w>": 20696, "hanley</w>": 47284, "reels</w>": 48127, "advertisement</w>": 18713, "noles</w>": 40569, "clio</w>": 46889, "lodge</w>": 10504, "vai</w>": 36802, "fight</w>": 2757, "grosven": 46911, "baba</w>": 12631, "deco</w>": 16422, "rean</w>": 48477, "pancre": 27708, "tron": 19057, "republic</w>": 7185, "crou": 31206, "ssic": 27774, "named</w>": 3194, "hud": 7169, "instruction</w>": 19407, "advocacy</w>": 14443, "trophy": 42676, "shakespeare</w>": 12488, "vengeance</w>": 32057, "tary</w>": 5065, "fsa</w>": 33373, "aml</w>": 43185, "coriander</w>": 37491, "berry": 15334, "sanford</w>": 32330, "bru</w>": 31028, "frigh": 34831, "moth": 33208, "peng</w>": 39200, "ÿ</w>": 443, "ero": 3211, "leo</w>": 8312, "thurst</w>": 33970, "idan</w>": 17929, "speak</w>": 4208, "bandic": 44400, "insulated</w>": 42051, "rhin": 12269, "collective</w>": 10162, "rÃ©": 29106, "grads</w>": 17811, "horror": 13787, "peth</w>": 48920, "ringed</w>": 44712, "amig": 40294, "lowry</w>": 27444, "hac": 20343, "matchday</w>": 15947, "uch</w>": 22394, "movember</w>": 23474, "nc": 5021, "lene</w>": 17628, "mol": 4246, "spade</w>": 32562, "novak</w>": 26465, "ðŁĻıðŁı¼</w>": 18952, "himself</w>": 4530, "android</w>": 5191, "hardro": 28126, "py": 4005, "qa</w>": 16360, "lynn": 25303, "nant</w>": 22526, "Q": 48, "notification</w>": 22512, "missionaries</w>": 40580, "kcr": 46181, "techno": 2599, "kyung</w>": 41058, "sureshpprabhu</w>": 42050, "guardian": 23713, "morph": 23915, "loco</w>": 25555, "chfield</w>": 41619, "spoon": 27001, "born</w>": 2683, "sotu</w>": 32286, "cinema": 38251, "rone</w>": 32763, "somali</w>": 26231, "csr": 32105, "port": 1641, "wartime</w>": 42998, "ncc</w>": 36686, "eart": 7086, "exo</w>": 5842, "distribu": 6138, "alin": 42746, "guern": 29277, "tomat": 12041, "atp</w>": 19817, "mann": 19396, "googled</w>": 40345, "mullins</w>": 41265, "sweet</w>": 2418, "slaughtered</w>": 46615, "gh</w>": 790, "troll</w>": 17103, "gula</w>": 27426, "iney</w>": 30254, "kaepernick</w>": 30713, "shen</w>": 31098, "(": 7, "myanmar</w>": 14764, "stitutes</w>": 40479, "crosby</w>": 21095, "tubes</w>": 22870, "pius</w>": 39988, "enyc</w>": 39520, "chou": 16960, "coordin": 8187, "really</w>": 1414, "knowledge</w>": 5510, "shat": 12169, "monoxide</w>": 49314, "Ē</w>": 462, "peaks</w>": 14067, "giggle</w>": 36426, "terribly</w>": 34558, "haci": 40674, "agen": 10101, "bhushan</w>": 40884, "ruth": 15798, "mainst": 42102, "boris</w>": 15704, "fueled</w>": 28792, "serbia</w>": 19038, "rusty": 43966, "¬</w>": 361, "î</w>": 426, "aloe</w>": 30728, "servant</w>": 20810, "stana</w>": 33311, "massachusetts</w>": 14756, "yd</w>": 9534, "womenintech</w>": 31470, "rotun": 42970, "combination</w>": 11312, "magic</w>": 3778, "tuni": 16270, "eday": 39258, "pickled</w>": 21705, "ðŁĴį": 35850, "package</w>": 7053, "rij": 41097, "oldie</w>": 35280, "priyan": 16488, "mulator</w>": 17463, "ronaldo</w>": 13463, "mimo": 45551, "tabs</w>": 29163, "committing</w>": 21937, "mv": 10580, "intelligence</w>": 6846, "quakes</w>": 24572, "utterly</w>": 21353, "ucc</w>": 29138, "ðŁĺĤðŁĺĤ</w>": 4112, "hydra": 44414, "hgtv</w>": 47657, "cough</w>": 18498, "candace</w>": 45623, "kaye</w>": 33003, "anfield</w>": 26993, "roto": 34698, "elfie</w>": 39955, "mauro</w>": 41691, "nara</w>": 33823, "sauces</w>": 40367, "vance</w>": 31447, "minority</w>": 16210, "nd</w>": 1764, "fern": 10747, "screened</w>": 31450, "president": 19900, "happiest</w>": 13811, "lesn": 39568, "courtney": 33601, "mc": 1278, "skel": 36564, "wat": 800, "analyst</w>": 14198, "margar": 16838, "thisi": 7299, "âŀĸ</w>": 34902, "oscill": 38272, "ishq": 27996, "influ": 4835, "recycled</w>": 16829, "positioned</w>": 34482, "tamil</w>": 14033, "consistency</w>": 25683, "degrees</w>": 8000, "bethel</w>": 33410, "blasted</w>": 38976, "joanne": 43736, "sht</w>": 44210, "ake</w>": 5776, "uss</w>": 9260, "visions</w>": 13804, "hairdresser</w>": 47468, "installing</w>": 18301, "ď</w>": 459, "portage</w>": 32087, "dogsoftwitter</w>": 19415, "aties</w>": 40060, "Ñģ": 23669, "joong</w>": 26544, "outine</w>": 35452, "jinyoung</w>": 38051, "moby</w>": 47219, "gav": 8966, "ultr": 25636, "gig": 26981, "pendleton</w>": 44272, "beauties</w>": 14874, "zon": 15109, "ãĥ³": 17671, "ennis": 48923, "tick</w>": 15617, "drag</w>": 12463, "shay": 10778, "lonely</w>": 12368, "osm": 31626, "cristo</w>": 38315, "sadler</w>": 45600, "val</w>": 1560, "abad": 33444, "americani": 39726, "servic": 27115, "ae</w>": 4542, "tos</w>": 6094, "kardashi": 13619, "stom": 2343, "medusa</w>": 44216, "stuck</w>": 6596, "sessions</w>": 6327, "anews</w>": 20919, "spride</w>": 26685, "visualization</w>": 28500, "ðŁĩ¹ðŁĩ": 36250, "combine</w>": 12919, "holic</w>": 16348, "inform": 10241, "recalling</w>": 47855, "recognize</w>": 10905, "abstractart</w>": 31170, "demand</w>": 5650, "flyo": 33506, "showers</w>": 9893, "turquoise</w>": 19899, "rei</w>": 26033, "wight": 41278, "christian": 11792, "jac": 2293, "turmeric</w>": 34044, "moment": 12197, "jang</w>": 22074, "«": 104, "alis</w>": 20114, "vani": 15396, "aho": 28114, "apocalypse</w>": 17571, "ðŁĳŃ</w>": 27943, "aco": 9463, "books</w>": 2161, "frequency</w>": 18825, "maas": 43332, "david</w>": 2259, "spani": 16721, "ios</w>": 6614, "tuf": 44510, "hoover</w>": 25691, "onpoli</w>": 20708, "grounded</w>": 27799, "karma</w>": 17658, "cad</w>": 20166, "driver": 27563, "ĸï¸ı</w>": 28877, "cbp</w>": 46723, "inen</w>": 44365, "warmest</w>": 30910, "tags</w>": 11606, "straigh": 31016, "cyclist</w>": 20686, "gest</w>": 2033, "sler</w>": 14066, "riyadh</w>": 33577, "mnd</w>": 44776, "pam": 8228, "camden": 38735, "happens</w>": 4988, "names</w>": 6130, "survives</w>": 30927, "essentially</w>": 30042, "uman</w>": 27112, "shazam</w>": 29063, "hir</w>": 14728, "elix": 32926, "elected</w>": 8828, "piedmont</w>": 39691, "project": 15911, "clap": 30037, "malnutrition</w>": 41153, "delle</w>": 35963, "centime": 48687, "puma</w>": 20858, "otti</w>": 36721, "swans</w>": 19516, "rack": 24600, "transplant</w>": 18771, "kesh</w>": 19751, "gone</w>": 3601, "ðŁĺ½</w>": 45156, "sheeran</w>": 18561, "horses</w>": 8809, "naia</w>": 31340, "sown</w>": 49369, "definition</w>": 11405, "ango</w>": 19090, "âľĶï¸ı</w>": 9191, "mainly</w>": 15280, "sketches</w>": 17622, "playground</w>": 15861, "fiercely</w>": 49039, "catholic</w>": 7757, "coates</w>": 36899, "chea</w>": 39580, "rofl</w>": 48228, "miler</w>": 44680, "suspicious</w>": 19862, "zania</w>": 15059, "stick</w>": 4987, "likes</w>": 4724, "author</w>": 4358, "onion</w>": 10985, "woolly</w>": 47722, "thumb": 19514, "geom": 46135, "dled</w>": 23494, "fart</w>": 34664, "flamin": 42693, "khu": 14041, "ðŁįº": 31081, "pharaoh</w>": 40437, "fiawec</w>": 39485, "liberalism</w>": 40018, "touts</w>": 41274, "convince</w>": 20351, "technews</w>": 31787, "momo": 48490, "face</w>": 1710, "abdel": 46511, "your</w>": 695, "exhibition</w>": 4219, "goog": 18581, "yur": 42533, "brotha</w>": 33974, "pires</w>": 14988, "trustees</w>": 28853, "sending</w>": 6985, "folder</w>": 25717, "volcanoes</w>": 38055, "viva</w>": 17399, "clutch</w>": 13953, "rhetor": 24359, "ï¸ıâĥ£": 17394, "complement</w>": 36624, "email": 33537, "shag": 22439, "mington</w>": 23119, "billsmafia</w>": 48845, "bridesmaids</w>": 47754, "horrifying</w>": 38901, "vap": 10462, "masi": 35965, "lexi": 44231, "roughs</w>": 37598, "atf</w>": 28013, "hues</w>": 38003, "losange": 14037, "retrogamer</w>": 47220, "jammin</w>": 35223, "cherry</w>": 7325, "ferreira</w>": 48686, "month</w>": 1924, "ÙĬ</w>": 23853, "ofc</w>": 19877, "patil</w>": 49187, "consolation</w>": 38888, "zimbabwe": 45668, "stev": 11640, "takes</w>": 2633, "railway": 27614, "ese</w>": 2260, "~!</w>": 31181, "schen": 22738, "ðŁĺĤðŁĺĤðŁĺĤðŁĺĤðŁĺĤðŁĺĤðŁĺĤðŁĺĤ": 28504, "setlist</w>": 33141, "anatomy</w>": 15376, "goodwill</w>": 24902, "oris</w>": 37064, "lotta</w>": 29125, "learn</w>": 1768, "landscape</w>": 5727, "ademy</w>": 49123, "functional</w>": 12885, "hobbies</w>": 36370, "wot</w>": 24863, "nx</w>": 16997, "autonom": 17870, "ðŁĺĮ</w>": 12163, "acmilan</w>": 36500, "strack</w>": 46861, "exquis": 16575, "ivf</w>": 39159, "prefer</w>": 11450, "view</w>": 1093, "sover</w>": 31876, "regional</w>": 5552, "philipp</w>": 47591, "kins": 31060, "iser": 23080, "snooker</w>": 25657, "taxes</w>": 11462, "mister</w>": 18895, "ires</w>": 12435, "dts</w>": 46233, "ducks</w>": 11202, "immigrant</w>": 16474, "ici</w>": 22189, "âĿ¤ï¸ı@</w>": 31187, "drif": 33585, "cape": 10288, "viet</w>": 13128, "scicom": 28606, "mbo</w>": 11319, "ove": 8649, "primal</w>": 36604, "plaid</w>": 23291, "supplement</w>": 19924, "âłĢ</w>": 8621, "âľĤ": 38602, "tora</w>": 45147, "rosÃ©</w>": 28006, "morro</w>": 48363, "strangers</w>": 20684, "staircase</w>": 22777, "sheep</w>": 9629, "sunscreen</w>": 29355, "copernic": 45519, "nifty</w>": 25604, "maxim": 19892, "chf</w>": 33021, "tourism</w>": 6556, "tracy</w>": 15508, "clemens</w>": 45896, "smashes</w>": 45657, "ucd</w>": 43514, "niti</w>": 45355, "ipad": 39067, "witnessing</w>": 33618, "regular</w>": 6307, "gopher": 47750, "Ùħ": 12986, "corner</w>": 5253, "contributor</w>": 24553, "kia</w>": 8712, "far</w>": 2384, "kirby</w>": 17065, "trains</w>": 9541, "tallest</w>": 19774, "moisture</w>": 20412, "royalties</w>": 48660, "waiter</w>": 32946, "dats</w>": 48674, "waltz</w>": 35982, "took</w>": 2280,
]
```

Python 通常の`json` で持ってきてええんかな？

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
