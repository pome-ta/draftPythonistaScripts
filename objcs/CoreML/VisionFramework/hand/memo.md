# 📝 2022/10/31

[iOS 14 Vision Body Pose Detection: Count Squat Reps in a SwiftUI Workout App | by Philipp Gehrke | Better Programming](https://betterprogramming.pub/ios-14-vision-body-pose-detection-count-squat-reps-in-a-workout-c88991f7cad4)


[Visionで身体や手のポーズを検出する – WWDC2020│](https://plum-plus.jp/2020/11/06/vision%e3%81%a7%e8%ba%ab%e4%bd%93%e3%82%84%e6%89%8b%e3%81%ae%e3%83%9d%e3%83%bc%e3%82%ba%e3%82%92%e6%a4%9c%e5%87%ba%e3%81%99%e3%82%8b-wwdc2020/)


### `VNSequenceRequestHandler`

> 概要
> このハンドラをインスタンス化すると、一連の画像に対してVisionリクエストを実行することができる。VNImageRequestHandlerとは異なり、作成時に画像を指定することはない。その代わり、performメソッドの1つを呼び続けるときに、各画像フレームを1つずつ供給する。

``` .log
availableJointNames: (
    VNHLKRPIP,
    VNHLKTMP,
    VNHLKMTIP,
    VNHLKRMCP,
    VNHLKRDIP,
    VNHLKITIP,
    VNHLKMPIP,
    VNHLKTTIP,
    VNHLKTIP,
    VNHLKIPIP,
    VNHLKPTIP,
    VNHLKWRI,
    VNHLKPPIP,
    VNHLKMMCP,
    VNHLKMDIP,
    VNHLKTCMC,
    VNHLKIMCP,
    VNHLKIDIP,
    VNHLKPMCP,
    VNHLKPDIP,
    VNHLKRTIP
)
availableJointsGroupNames(
    VNHLRKT,
    VNHLRKM,
    VNHLRKI,
    VNHLRKR,
    VNHLRKP,
    VNIPOAll
)

```



``` .log
# VNIPOAll
{
    VNHLKIDIP = "[0.350816; 0.344648]";
    VNHLKIMCP = "[0.203235; 0.273218]";
    VNHLKIPIP = "[0.255140; 0.318929]";
    VNHLKITIP = "[0.430193; 0.372914]";
    VNHLKMDIP = "[0.401088; 0.339046]";
    VNHLKMMCP = "[0.214535; 0.259824]";
    VNHLKMPIP = "[0.311639; 0.300414]";
    VNHLKMTIP = "[0.467750; 0.365228]";
    VNHLKPDIP = "[0.441783; 0.296928]";
    VNHLKPMCP = "[0.196608; 0.222184]";
    VNHLKPPIP = "[0.293252; 0.243112]";
    VNHLKPTIP = "[0.500727; 0.321662]";
    VNHLKRDIP = "[0.422160; 0.319209]";
    VNHLKRMCP = "[0.205185; 0.249156]";
    VNHLKRPIP = "[0.326009; 0.285425]";
    VNHLKRTIP = "[0.477980; 0.343198]";
    VNHLKTCMC = "[0.173057; 0.244838]";
    VNHLKTIP = "[0.339841; 0.309450]";
    VNHLKTMP = "[0.231377; 0.279885]";
    VNHLKTTIP = "[0.412918; 0.348824]";
    VNHLKWRI = "[0.144244; 0.148627]";
}
```

[Body Anatomy: Upper Extremity Joints | The Hand Society](https://www.assh.org/handcare/safety/joints)


#### `VNImageRequestHandler`

> 概要
> このハンドラをインスタンス化すると、1つの画像に対してVisionリクエストを実行できる。作成時に画像と、オプションで完了ハンドラを指定し、リクエストの実行を開始するために performRequests:error: を呼び出す。

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
