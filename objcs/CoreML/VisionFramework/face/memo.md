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
