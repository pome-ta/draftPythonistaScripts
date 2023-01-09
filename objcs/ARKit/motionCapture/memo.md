# 📝 2023/01/07

RealityKit がPythonista3 だと呼び出せない？

## xcode から実機テストしてみる

14.2.0

iPhone11 16.2

Team 入れてなかったから怒られた？

### 実機

まいかい、信頼されてないないデベロッパ確認があるのね

（てか、デベロッパーではなくデベロッパなんだ。。。）

設定 → 一般 → VPNとデバイス管理 → デベロッパAPP

とりあえず動いた

``` dialog
Do you want to continue upgrading to the latest recommended settings and performing project cleanup? It may not be possible to undo this operation.
```

> 最新の推奨設定へのアップグレードとプロジェクトのクリーンアップの実行を続行しますか?この操作を元に戻すことはできない場合があります。

最新のセッティング的なのはしない

### ARView と ARSCNView

[ARView.DebugOptions | Apple Developer Documentation](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct)

DEbugOptions で気がついたけど、ARView とARSCNView 違うんね

書き換えてみてもいいかもな

## ARSCNView

face tracking の要領で取れるか？

# 📝 2023/01/05

[Capturing Body Motion in 3D | Apple Developer Documentation](https://developer.apple.com/documentation/arkit/content_anchors/capturing_body_motion_in_3d?language=objc)
