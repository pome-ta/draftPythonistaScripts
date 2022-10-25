# 📝 2022/10/25

## `photoFaceDetection.py` 静止画で取得

### log

[[iOS 11] 画像解析フレームワークVisionで顔認識を試した結果 | DevelopersIO](https://dev.classmethod.jp/articles/ios-11-vision/) 大体同じかな？

```
boundingBox=[0.558769, 0.620258, 0.0669028, 0.0892037]
boundingBox=[0.722235, 0.402091, 0.074335, 0.0991133]
boundingBox=[0.285486, 0.640302, 0.0764578, 0.101944]
```

```
<VNFaceObservation: 0x604000182700> 68149739-D1B0-4E89-8FB2-44F33969FAED 1 [0.557461 0.616566 0.069802 0.0930694] ID=0
<VNFaceObservation: 0x6040001828a0> D113842C-B9CA-4D70-88CE-74814860D383 1 [0.722581 0.400897 0.0740046 0.0986728] ID=0
<VNFaceObservation: 0x600000182e50> 69A72E48-0270-4687-B0B4-4F57A8E5DEA3 1 [0.28446 0.639232 0.0771421 0.102856] ID=0
```


# 📝 2022/10/24


## `completionHandler`

`VNDetectFaceRectanglesRequest(completionHandler:` この呼び出し方法が不明だった。クロージャでは？と、勘付いた自分を褒めたい



``` .swift
let faceDetectionRequest = VNDetectFaceRectanglesRequest(completionHandler: { (request, error) in
    
    if error != nil {
        print("FaceDetection error: \(String(describing: error)).")
    }
    
    guard let faceDetectionRequest = request as? VNDetectFaceRectanglesRequest,
        let results = faceDetectionRequest.results as? [VNFaceObservation] else {
            return
    }
    DispatchQueue.main.async {
        // Add the observations to the tracking list
        for observation in results {
            let faceTrackingRequest = VNTrackObjectRequest(detectedObjectObservation: observation)
            requests.append(faceTrackingRequest)
        }
        self.trackingRequests = requests
    }
})
```


[Swift クロージャーについて　サルだとわからん - IT人材育成コネクト](https://connect-solution.net/jp/2019/11/23/swift-%e3%82%af%e3%83%ad%e3%83%bc%e3%82%b8%e3%83%a3%e3%83%bc%e3%81%ab%e3%81%a4%e3%81%84%e3%81%a6%e3%80%80%e3%82%b5%e3%83%ab%e3%81%a0%e3%81%a8%e3%82%8f%e3%81%8b%e3%82%89%e3%82%93/)

[Swift completionHandlerについて - IT人材育成コネクト](https://connect-solution.net/jp/2021/07/11/swift-completionhandler-2/)


## Photo からはじめるか、、、

画像借り場所

[ios-vision/multi-face.png at master · googlesamples/ios-vision](https://github.com/googlesamples/ios-vision/blob/master/FaceDetectorDemo/FaceDetector/multi-face.png)


# 📝 2022/10/23

## `create_objc_class`

`methods` の命名は、`_` で引数の数を確認してる？


# 📝 2022/10/22


## `AVCaptureVideoDataOutput`

### `connectionWithMediaType`

`vide`


`AVMediaTypeVideo` では、ないみたい

# 📝 2022/10/21

[Tracking the User’s Face in Real Time | Apple Developer Documentation](https://developer.apple.com/documentation/vision/tracking_the_user_s_face_in_real_time?language=objc)



## `AVCaptureDeviceDiscoverySession`

落ちるから、通常のdevices で取る

## `highestResolution420Format` の処理


`ObjCInstance` で読めるか？



kCVPixelFormatType_420YpCbCr8BiPlanarFullRange

[CVPixelFormatType Enum (CoreVideo) | Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/api/corevideo.cvpixelformattype?view=xamarin-mac-sdk-14)

[Apple - Lists.apple.com](https://lists.apple.com/archives/cocoa-dev/2017/Jun/msg00144.html)

kCVPixelFormatType_420YpCbCr8BiPlanarFullRange    875704422



``` .log
----
875704438
c_void_p(10799546064)
----
875704422
c_void_p(10799545872)
----
875704438
c_void_p(10799543136)
----
875704422
c_void_p(10799531088)
----
875704438
c_void_p(10799333168)
----
875704422
c_void_p(10799300800)
----
875704438
c_void_p(10799301184)
----
875704422
c_void_p(10799302048)
----
875704438
c_void_p(10799302336)
----
875704422
c_void_p(10799303056)
----
875704438
c_void_p(10799305312)
----
875704422
c_void_p(10799305744)
----
875704438
c_void_p(10799306272)
----
875704422
c_void_p(10799306992)
----
875704438
c_void_p(10799303200)
----
875704422
c_void_p(10799304016)
----
875704438
c_void_p(10799303440)
----
875704422
c_void_p(10799397360)
----
875704438
c_void_p(10799392128)
----
875704422
c_void_p(10799395488)
----
875704438
c_void_p(10799392800)
----
875704422
c_void_p(10799392512)
----
875704438
c_void_p(10799350480)
----
875704422
c_void_p(10799350000)
----
875704438
c_void_p(10799682144)
----
875704422
c_void_p(10799679504)
----
875704438
c_void_p(10799680464)
----
875704422
c_void_p(10799681424)
----
875704438
c_void_p(10799680608)
----
875704422
c_void_p(10799681280)
----
875704438
c_void_p(10799679264)
----
875704422
c_void_p(10799682864)
----
875704438
c_void_p(10799677584)
----
875704422
c_void_p(10799697040)
----
875704438
c_void_p(10799699920)
----
875704422
c_void_p(10799701888)
----
875704438
c_void_p(10799703904)
----
875704422
c_void_p(10799708752)
----
875704438
c_void_p(10799696176)
----
875704422
c_void_p(10799670560)
----
875704438
c_void_p(10799673728)
----
875704422
c_void_p(10799672672)
----
875704438
c_void_p(10799672768)
----
875704422
c_void_p(10799668688)


```
