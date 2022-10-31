[[iOS] WWDC2020で紹介されたVision frameworkのbody pose検出を使ってみる | DevelopersIO](https://dev.classmethod.jp/articles/vision-body-pose/)


[iOS 14 Vision Body Pose Detection: Count Squat Reps in a SwiftUI Workout App | by Philipp Gehrke | Better Programming](https://betterprogramming.pub/ios-14-vision-body-pose-detection-count-squat-reps-in-a-workout-c88991f7cad4)


# 📝 2022/10/31


## `frame` と`bounds`

親のサイズ継承をする場合、`frame` と`bounds` どっちをどっちに投げればいいのだろうか？


### `layout` メソッドを独自に生やす


`ui.View` の継承として、考えてみている。

`layout` を親の`ui.View` が処理された時に呼び出されるようにして、画面サイズを取り敢えず調整している

``` .py
  def layout(self):
    self.previewLayer.frame = self.cameraView.bounds()
    print(f'cam: {parseCGRect(self.cameraView.frame())}')
    print(f'pre: {parseCGRect(self.previewLayer.frame())}')
```

今のところ、問題は出ていないし、すっきりするので「取り敢えずヨシ！」してる


## キャプチャの画面比率


(現状)気にしてないけど、アスペクト比とかどうなんやろ？あってる？


## カメラのフロント・バック

いまの呼び出しでは、バックしか適用できないのでは？

``` .py
videoDevice = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
```



[face_detector.py strange behavior | omz:forum](https://forum.omz-software.com/topic/6434/face_detector-py-strange-behavior/22)


前は、ダメだったきがするのだけど、なぜかできた、、、`vide` の所かしら？


``` .py
    _builtInWideAngleCamera = 'AVCaptureDeviceTypeBuiltInWideAngleCamera'
    _video = 'vide'
    _front = 2  # back -> 1
    videoDevice = AVCaptureDevice.defaultDeviceWithDeviceType_mediaType_position_(
      _builtInWideAngleCamera, _video, _front)

```


# 📝 2022/10/30

顔も手も、キャプチャで実装できてないけどやってみる😂


## 書き方

本来`private` のものは、`_hoge` として書き進めた方が良さそう。しかし、`self._hoge` を呼び出すのにPythonista だと予測が出ないので、`self.hoge` と書く



[UIViewControllerのライフサイクル - Qiita](https://qiita.com/motokiee/items/0ca628b4cc74c8c5599d)

[UIViewControllerまとめ - Qiita](https://qiita.com/edo_m18/items/189acd18f1ecc368b5b0)
