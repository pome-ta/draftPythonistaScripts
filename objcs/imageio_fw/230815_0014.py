from objc_util import ObjCClass, c
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

result = PHAssetCollection.fetchAssetCollectionsWithType_subtype_options_(
  2, 209, None)

assetCollection = result.firstObject()

fetchResult = PHAsset.fetchAssetsInAssetCollection_options_(
  assetCollection, None)

#first_object = fetchResult.firstObject()
#first_object = fetchResult.indexOfObject_(0)

last_object = fetchResult.lastObject()
assetsLibraryURL_url = last_object.assetsLibraryURL()
mainFileURL_url = last_object.mainFileURL()

#pdbg.state(assetCollection)
#pdbg.state(fetchResult)
#pdbg.state(last_object.assetsLibraryURL())
url_data = NSData.dataWithContentsOfURL_(mainFileURL_url)
#absoluteString',
# 'absoluteURL',
#print(photo_url)
#print(photo_url.absoluteString())
#pdbg.state(photo_url.absoluteString())
#pdbg.state(last_object.mainFileURL())

