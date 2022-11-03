# 📝 2022/11/03

## delegate 呼べた？

`captureOutput_didOutputSampleBuffer_fromConnection_` のみ呼び出していたが、`captureOutput_didDropSampleBuffer_fromConnection_` も呼び出してみてる


[captureOutput:didDropSampleBuffer:fromConnection: | Apple Developer Documentation](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1388468-captureoutput?language=objc)




> ディスカッション

> 遅延ビデオフレームがドロップされるたびに、Delegate はこのメッセージを受け取ります。このメソッドは、ドロップされたフレームごとに 1 回呼び出されます。出力の sampleBufferCallbackQueue プロパティで指定されたディスパッチ キューで呼び出されます。

> sampleBuffer には、フレームがドロップされた理由の詳細を示す kCMSampleBufferAttachmentKey_DroppedFrameReason 添付ファイルが含まれます。フレームがドロップされた理由は、フレームが遅延したため (kCMSampleBufferDroppedFrameReason_FrameWasLate) で、通常クライアントの処理に時間がかかりすぎたために起こりました。また、フレームを提供するモジュールがバッファ不足のため、ドロップされることもあります（kCMSampleBufferDroppedFrameReason_OutOfBuffers）。サンプルバッファを提供するモジュールが不連続を経験し（kCMSampleBufferDroppedFrameReason_Discontinuity）、未知の数のフレームが失われた場合にも、フレームがドロップされることがあります。この状態は、通常、システムがビジー状態であることが原因です。

> このメソッドは、ビデオフレームの出力を担当する同じディスパッチキューで呼び出されるため、ドロップされたビデオフレームの追加など、キャプチャパフォーマンスの問題を防ぐために効率的である必要があります。




[captureOutput:didOutputSampleBuffer:fromConnection: | Apple Developer Documentation](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput?language=objc)


> ディスカッション

> videoSettings プロパティで指定された通りにデコードまたは再エンコードして、新しいビデオ フレームをキャプチャして出力すると、ディレゲートはこのメッセージを受信します。デリゲートは、提供されたビデオフレームを他の API と組み合わせて使用し、さらに処理することができます。

> このメソッドは、出力の sampleBufferCallbackQueue プロパティによって指定されたディスパッチ キューで呼び出されます。定期的に呼び出されるため、ドロップフレームを含むキャプチャパフォーマンスの問題を防ぐために効率的でなければなりません。
> このメソッドの範囲外でCMSampleBufferオブジェクトを参照する必要がある場合は、CFRetainし、それが終了したらCFReleaseする必要があります。

> 最適なパフォーマンスを維持するために、いくつかのサンプルバッファは、デバイスシステムと他のキャプチャ入力によって再使用される必要があるかもしれないメモリのプールを直接参照します。これは、非圧縮のデバイスネイティブキャプチャで、メモリブロックのコピーをできるだけ少なくする場合によくあることです。複数のサンプルバッファがそのようなメモリプールを長く参照していると、入力は新しいサンプルをメモリにコピーすることができなくなり、それらのサンプルはドロップされます。

> もしアプリケーションが提供された CMSampleBufferRef オブジェクトを長く保持することでサンプルのドロップを引き起こしているが、サンプルデータに長期間アクセスする必要がある場合、データを新しいバッファにコピーしてからサンプルバッファを解放し（以前に保持していた場合）、それが参照するメモリを再使用できるようにすることを検討してください。


# 📝 2022/11/02

## `delegate` を class 内に入れると、60 くらいで呼び出さなくなる

[face_detector.py strange behavior | omz:forum](https://forum.omz-software.com/topic/6434/face_detector-py-strange-behavior)

### pavlinb

> ここ([iPhone のカメラでリアルタイム顔検出（Pythonista 編） - Qiita](https://qiita.com/inasawa/items/3e730c338bcefd522fb8))から face_detector.py を勉強させていただきました。
> ここでは、ビデオカメラのフレームに対してリアルタイムに検出器を適用しています。

> 問題は 80-90 フレームで発生します。スクリプトは単に停止しますが、アプリケーションはクラッシュしません。

> なぜ止まるのか、どうすれば防げるのかがわかりません。

> 何かアイデアはありますか？


```.py
# coding: utf-8

from objc_util import *
from ctypes import c_void_p
import ui
import time

# 全フレームを処理しようとすると動かなくなるのでこの程度で
FRAME_INTERVAL = 6  # 30fps / 6 = 5fps

frame_counter = 0
last_fps_time = time.time()
fps_counter = 0

AVCaptureSession = ObjCClass('AVCaptureSession')
AVCaptureDevice = ObjCClass('AVCaptureDevice')
AVCaptureDeviceInput = ObjCClass('AVCaptureDeviceInput')
AVCaptureVideoDataOutput = ObjCClass('AVCaptureVideoDataOutput')
AVCaptureVideoPreviewLayer = ObjCClass('AVCaptureVideoPreviewLayer')

CIImage    = ObjCClass('CIImage')
CIDetector = ObjCClass('CIDetector')

dispatch_get_current_queue = c.dispatch_get_current_queue
dispatch_get_current_queue.restype = c_void_p

CMSampleBufferGetImageBuffer = c.CMSampleBufferGetImageBuffer
CMSampleBufferGetImageBuffer.argtypes = [c_void_p]
CMSampleBufferGetImageBuffer.restype = c_void_p

CVPixelBufferLockBaseAddress = c.CVPixelBufferLockBaseAddress
CVPixelBufferLockBaseAddress.argtypes = [c_void_p, c_int]
CVPixelBufferLockBaseAddress.restype = None

CVPixelBufferGetWidth = c.CVPixelBufferGetWidth
CVPixelBufferGetWidth.argtypes = [c_void_p]
CVPixelBufferGetWidth.restype = c_int

CVPixelBufferGetHeight = c.CVPixelBufferGetHeight
CVPixelBufferGetHeight.argtypes = [c_void_p]
CVPixelBufferGetHeight.restype = c_int

CVPixelBufferUnlockBaseAddress = c.CVPixelBufferUnlockBaseAddress
CVPixelBufferUnlockBaseAddress.argtypes = [c_void_p, c_int]
CVPixelBufferUnlockBaseAddress.restype = None


def captureOutput_didOutputSampleBuffer_fromConnection_(_self, _cmd, _output, _sample_buffer, _conn):
    global frame_counter, fps_counter, last_fps_time
    global image_width, image_height, faces

    # 性能確認のためビデオデータの実 FPS 表示
    fps_counter += 1
    now = time.time()
    if int(now) > int(last_fps_time):
        label_fps.text = '{:5.2f} fps'.format((fps_counter) / (now - last_fps_time))
        last_fps_time = now
        fps_counter = 0

    # 画像処理は FRAME_INTERVAL 間隔で処理
    if frame_counter == 0:
        # ビデオ画像のフレームデータを取得
        imagebuffer =  CMSampleBufferGetImageBuffer(_sample_buffer)
        # バッファをロック
        CVPixelBufferLockBaseAddress(imagebuffer, 0)

        image_width  = CVPixelBufferGetWidth(imagebuffer)
        image_height = CVPixelBufferGetHeight(imagebuffer)
        ciimage = CIImage.imageWithCVPixelBuffer_(ObjCInstance(imagebuffer))

        # CIDetector により顔検出
        options = {'CIDetectorAccuracy': 'CIDetectorAccuracyHigh'}
        detector = CIDetector.detectorOfType_context_options_('CIDetectorTypeFace', None, options)
        faces = detector.featuresInImage_(ciimage)

        # バッファのロックを解放
        CVPixelBufferUnlockBaseAddress(imagebuffer, 0)

        # 検出した顔の情報を使って表示を更新
        path_view.set_needs_display()

    frame_counter = (frame_counter + 1) % FRAME_INTERVAL

class PathView(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        # 検出した顔の輪郭に合わせて、表示を加工
        if faces is not None and faces.count() != 0:
            # 顔の部分を白く覆う
            ui.set_color((1, 1, 1, 0.9))
            for face in faces:
                face_bounds = face.bounds()
                # カメラの画像は X軸=1920 Y軸=1080
                # View は X軸=375 Y軸=667
                # 画像のX軸Y軸をViewのY軸X軸に対応させ、サイズを調整
                x = face_bounds.origin.y    * self.height / image_width
                y = face_bounds.origin.x    * self.width  / image_height
                w = face_bounds.size.height * self.height / image_width
                h = face_bounds.size.width  * self.width  / image_height
                path = ui.Path.oval(x, y, w * 1.3, h)
                path.fill()

@on_main_thread
def main():
    global path_view, label_fps, faces

    # 画面の回転には対応しておらず
    # iPhoneの画面縦向きでロックした状態で、横長画面で使う想定
    # View のサイズは手持ちの iPhone6 に合わせたもの
    faces = None
    main_view = ui.View(frame=(0, 0, 375, 667))
    path_view = PathView(frame=main_view.frame)
    main_view.name = 'Face Detector'

    sampleBufferDelegate = create_objc_class(
                                'sampleBufferDelegate',
                                methods=[captureOutput_didOutputSampleBuffer_fromConnection_],
                                protocols=['AVCaptureVideoDataOutputSampleBufferDelegate'])
    delegate = sampleBufferDelegate.new()

    session = AVCaptureSession.alloc().init()
    device = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
    _input = AVCaptureDeviceInput.deviceInputWithDevice_error_(device, None)
    if _input:
        session.addInput_(_input)
    else:
        print('Failed to create input')
        return

    output = AVCaptureVideoDataOutput.alloc().init()
    queue = ObjCInstance(dispatch_get_current_queue())
    output.setSampleBufferDelegate_queue_(delegate, queue)
    output.alwaysDiscardsLateVideoFrames = True

    session.addOutput_(output)
    session.sessionPreset = 'AVCaptureSessionPresetHigh' # 1920 x 1080

    prev_layer = AVCaptureVideoPreviewLayer.layerWithSession_(session)
    prev_layer.frame = ObjCInstance(main_view).bounds()
    prev_layer.setVideoGravity_('AVLayerVideoGravityResizeAspectFill')

    ObjCInstance(main_view).layer().addSublayer_(prev_layer)

    # 性能確認のためビデオデータの実 FPS 表示
    label_fps = ui.Label(frame=(0, 0, main_view.width, 30), flex='W', name='fps')
    label_fps.background_color = (0, 0, 0, 0.5)
    label_fps.text_color = 'white'
    label_fps.text = ''
    label_fps.alignment = ui.ALIGN_CENTER

    main_view.add_subview(label_fps)
    main_view.add_subview(path_view)

    session.startRunning()

    main_view.present('sheet')
    main_view.wait_modal()

    session.stopRunning()
    delegate.release()
    session.release()
    output.release()

if __name__ == '__main__':
    main()
```

### JonB

> もし、frame_xounter が大きくなったら、frame_counter と last frame time を定期的に 0 にリセットする方法を追加することを検討してもよいでしょう。

> または、フレーム時間、frame_counter、および現在時間で更新されるラベルを持つ - これらはコールバック内のロジックで使用されるからです。


### pavlinb

> 自動ロック後、携帯電話が起動すると、スクリプトがさらに 80 ～ 90 パスして、再びハングする。

### JonB

> わかりました、いくつか問題があるようです。

> まず、didDropSampleBuffer デリゲートメソッドを実装し、フレームが遅れた理由を表示する必要があります。

> 2 つ目は、minFrameDuration を設定して、デリゲートが必要以上に呼び出されないようにする必要があります。古いバージョンでは、これは output.minFrameDuration にあったと思います。新しい iOS バージョンでは、接続で設定すると思います、 output.connections[0].videoMinFrameDuration

> 第三に、どのディスパッチキューで呼び出されるかという問題があります。あるいは、デリゲートは常にできるだけ速く戻る必要があり、別のスレッドで重い仕事を呼び出し、そうでなければデータを落とします。

> 後で改良した gist を投稿します。

### pavlinb

> もう一つの良い例をここ([Image capture system with AVCaptureStillImageOutput.](https://gist.github.com/Cethric/83a4b2ccf25798d5e074))でテストしてみました。

> このスクリプトでは

> `self.captureOutput.setMinFrameDuration_(CMTimeMake(1, 2), argtypes=[CMTime], restype=None)` を実装しています。

> `CMTimeMake(.,.)`を使っています。

> 残念ながら、このスクリプトもハングアップしてしまいます。

### JonB

> Cethric のものをベースにしたバージョンを持っています。後日、きれいにして投稿します。ドロップフレームのコールバックを実装したので、何が問題かわかると思います。

> 私が見つけた 1 つの問題は、minFrameDuration を設定する様々な方法が機能しないことです。つまり、コールバックが高い確率で呼び出されるのです。

### pavlinb

> `setMinFrameDuration` は、`camera.captureOutput` オブジェクト（`AVCaptureVideoDataOutput`）にあるようです。

しかし、`camera.captureDevice` (`AVCaptureDevice`)にも`setActiveVideoMinFrameDuration` が存在します。


> どちらも動作させることができませんでした。

### JonB

> これを試してみてください。 [detector.py](https://gist.github.com/jsbain/424d4fe1a3c0b1ae3fd705d72f665c1e)

> FRAME_PROC_INTERVAL を、FrameLate が常に表示されなくなるまで増やすか、または 1 に設定してできるだけ速くします。

> 実際の最小フレーム間隔を設定するためには、多くの輪をくぐり抜ける必要があります。DESIRED_FPS を変更することで、30fps 未満にできるかどうかを確認することができます。

> これはハングアップしますか？ もしそうなら、最初のフレームが戻ってきたときにどんなメッセージが出ますか？

# 📝 2022/10/31

[iOS 14 Vision Body Pose Detection: Count Squat Reps in a SwiftUI Workout App | by Philipp Gehrke | Better Programming](https://betterprogramming.pub/ios-14-vision-body-pose-detection-count-squat-reps-in-a-workout-c88991f7cad4)

[Vision で身体や手のポーズを検出する – WWDC2020│](https://plum-plus.jp/2020/11/06/vision%e3%81%a7%e8%ba%ab%e4%bd%93%e3%82%84%e6%89%8b%e3%81%ae%e3%83%9d%e3%83%bc%e3%82%ba%e3%82%92%e6%a4%9c%e5%87%ba%e3%81%99%e3%82%8b-wwdc2020/)

### `VNSequenceRequestHandler`

> 概要

> このハンドラをインスタンス化すると、一連の画像に対して Vision リクエストを実行することができる。VNImageRequestHandler とは異なり、作成時に画像を指定することはない。その代わり、perform メソッドの 1 つを呼び続けるときに、各画像フレームを 1 つずつ供給する。

```.log
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

```.log
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
> このハンドラをインスタンス化すると、1 つの画像に対して Vision リクエストを実行できる。作成時に画像と、オプションで完了ハンドラを指定し、リクエストの実行を開始するために performRequests:error: を呼び出す。

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

- Pythonista の draw 以外で描けるか確認
  - `CAShapeLayer`
  - `UIBezierPath`
- キャプチャ
  - `CameraViewController`
  - `AVCaptureSession` 関係
    - ただ画面上に出すことは成功

## `self.objc_instance.layer()`

実装の仕方ちがう

[Swift, Objective-C を Xamarin.iOS に移植する際のポイント（2）　 UIView.Layer の差し替え - 個人的なメモ](https://hiro128.hatenablog.jp/entry/2017/09/30/234916)

余裕があったら調べる

## カメラをキャプチャする

色々なことろ参考にしながら、delegate まで実装

## `dispatch_get_main_queue`

`main` は、気軽に呼べない

[how can i access dispatch_get_main_queue | omz:forum](https://forum.omz-software.com/topic/6204/how-can-i-access-dispatch_get_main_queue/2)

## delegate を Class 内に配置？

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
