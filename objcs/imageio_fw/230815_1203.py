import ctypes
from objc_util import ObjCClass,ObjCInstance, c,uiimage_to_png

import ui
import pdbg

#CGImageSourceCopyProperties = c.CGImageSourceCopyProperties

PHAsset = ObjCClass('PHAsset')
PHAssetCollection = ObjCClass('PHAssetCollection')
PHFetchOptions = ObjCClass('PHFetchOptions')

UIImage = ObjCClass('UIImage')
NSData = ObjCClass('NSData')

# PHAssetCollectionTypeSmartAlbum = 2
# PHAssetCollectionSubtypeSmartAlbumUserLibrary = 209

# PHAssetCollectionSubtypeSmartAlbumRecentlyAdded = 206

fetch_assetCollections = PHAssetCollection.fetchAssetCollectionsWithType_subtype_options_(
  2, 209, None)

assetCollection = fetch_assetCollections.firstObject()

fetch_asset = PHAsset.fetchAssetsInAssetCollection_options_(
  assetCollection, None)

last_object = fetch_asset.lastObject()
#assetsLibraryURL_url = last_object.assetsLibraryURL()
mainFileURL_url = last_object.mainFileURL()

url_data = NSData.dataWithContentsOfURL_(mainFileURL_url)

ui_image = UIImage.imageWithData_(url_data)
#pdbg.state(ui_image)

#CGImageSourceCreateWithURL

CGImageSourceCreateWithURL = c.CGImageSourceCreateWithURL
CGImageSourceCreateWithURL.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
CGImageSourceCreateWithURL.restype = ctypes.c_void_p


CGImageSource = ObjCInstance(CGImageSourceCreateWithURL(mainFileURL_url, None))


pdbg.state(CGImageSource)
