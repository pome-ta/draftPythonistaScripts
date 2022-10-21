# 📝 2022/10/21


## デバイスのインプット関係を整理

[detector.py](https://gist.github.com/jsbain/424d4fe1a3c0b1ae3fd705d72f665c1e)


`AVCaptureDevice.defaultDeviceWithDeviceType_mediaType_position_(_builtInWideAngleCamera, _video, _front)`

だめだから、

`videoDevice = AVCaptureDevice.devices()[1]`

Pythonista がもう起動してるから？（読み込んでるから？）


`420f` = `1111970369`

ちゃんと確認する

> Bi-Planar Component Y'CbCr 8-bit 4:2:0, full-range (luma=[0,255] chroma=[1,255]). baseAddr points to a big-endian CVPlanarPixelBufferInfo_YCbCrBiPlanar struct.

[kCVPixelFormatType_420YpCbCr8BiPlanarFullRange | Apple Developer Documentation](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8biplanarfullrange?language=objc)

# 📝 2022/10/20


## 順番

- Pythonista のdraw 以外で描けるか確認
  - `CAShapeLayer`
  - `UIBezierPath`
- キャプチャ
  - `CameraViewController`
  - `AVCaptureSession` 関係
    - ただ画面上に出すことは成功



## `self.objc_instance.layer()`

実装の仕方ちがう


[Swift, Objective-C を Xamarin.iOS に移植する際のポイント（2）　UIView.Layerの差し替え - 個人的なメモ](https://hiro128.hatenablog.jp/entry/2017/09/30/234916)


余裕があったら調べる


## カメラをキャプチャする

色々なことろ参考にしながら、delegate まで実装

## `dispatch_get_main_queue`

`main` は、気軽に呼べない

[how can i access dispatch_get_main_queue | omz:forum](https://forum.omz-software.com/topic/6204/how-can-i-access-dispatch_get_main_queue/2)

## delegate をClass 内に配置？

buffer を変数として持つには、Class 内かしら？


メソッド化して、Class 内に設置して、`self` で呼び出すようにした


## `autorelease()` いるいらない問題

何を基準に必要なんだろうか？

delegate のところは、`autorelease()` を付けておく


## `recognizedPoints(.thumb)` の`.thumb` とかを探す

これか？`VNHumanHandPoseObservationJointsGroupNameThumb`

[VNHumanHandPoseObservationJointsGroupNameThumb | Apple Developer Documentation](https://developer.apple.com/documentation/vision/vnhumanhandposeobservationjointsgroupnamethumb?language=objc)


[VNHumanHandPoseObservationJointsGroupName | Apple Developer Documentation](https://developer.apple.com/documentation/vision/vnhumanhandposeobservationjointsgroupname?changes=_10_8&language=objc)



[.NET API Catalog](https://apisof.net/catalog/07929f76-9c5c-2bd2-50d0-6a477473f016)



うぬー`None` を取得するぅー


# 📝 2022/10/17


[Detect Body and Hand Pose with Vision - WWDC20 - Videos - Apple Developer](https://developer.apple.com/videos/play/wwdc2020/10653/)

[Detecting Hand Poses with Vision | Apple Developer Documentation](https://developer.apple.com/documentation/vision/detecting_hand_poses_with_vision?language=objc)







