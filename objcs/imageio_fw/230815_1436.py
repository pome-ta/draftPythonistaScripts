import ctypes
from objc_util import ObjCClass, ObjCInstance, c

PHAssetCollection = ObjCClass('PHAssetCollection')
PHAsset = ObjCClass('PHAsset')
NSData = ObjCClass('NSData')

# todo: Function `CGImageSourceCreateWithURL` の定義
# [CGImageSourceCreateWithURL | Apple Developer Documentation](https://developer.apple.com/documentation/imageio/1465262-cgimagesourcecreatewithurl?language=objc)

CGImageSourceCreateWithURL = c.CGImageSourceCreateWithURL
CGImageSourceCreateWithURL.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
CGImageSourceCreateWithURL.restype = ctypes.c_void_p

# todo: アルバムから「最近の項目」を取得
# PHAssetCollectionTypeSmartAlbum = 2
# PHAssetCollectionSubtypeSmartAlbumUserLibrary = 209
fetch_assetCollections = PHAssetCollection.fetchAssetCollectionsWithType_subtype_options_(
  2, 209, None)

assetCollection = fetch_assetCollections.firstObject()

fetch_asset = PHAsset.fetchAssetsInAssetCollection_options_(
  assetCollection, None)

# todo: 「最近の項目」の最新の写真を取得
last_object = fetch_asset.lastObject()

# xxx: `NSURL: assets-library://` では、面倒だったので（`last_object.assetsLibraryURL()`）
# `NSURL: file://` で取れるように`mainFileURL`
main_file_url = last_object.mainFileURL()

_image_source = CGImageSourceCreateWithURL(main_file_url, None)
CGImageSource = ObjCInstance(_image_source)

