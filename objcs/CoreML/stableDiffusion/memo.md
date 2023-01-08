# 📝 2023/01/08


[【Swift】iOSでStableDiffusionを使ってみた - Qiita](https://qiita.com/SNQ-2001/items/2d33dc535cf106189f75)


## 調査流れ


`./iOSproj/iOSstableDiffusionDEMO/ViewModel.swift`

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

