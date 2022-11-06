#from images2gif import writeGif
from pathlib import Path
import images2gif
from PIL import Image as ImageP

from objc_util import ObjCClass
import photos
from objc_util import ObjCClass, ObjCInstance
import pdbg

PHAsset = ObjCClass('PHAsset')

#img_assets = photos.get_assets('video')
img_assets = photos.get_assets()
pick_img = photos.pick_asset(img_assets)

img_objc = ObjCInstance(pick_img._objc_ptr)
#pdbg.state(objc_img)
#print(img_objc.mainFileURL())
file_url = img_objc.mainFileURL()
file_path = str(file_url).strip('file:')
print(file_path)

gif_path = Path(file_path)

print(gif_path.exists())

#gif_read = images2gif.readGif(f'{img_objc.mainFileURL()}')


#gif_img = pick_img.get_image()
#gif_img.show()

#gif_bytes = pick_img.get_image_data()
#gifimg = ImageP.open(gif_bytes)
#hoge = images2gif.readGif(gifimg)

#gifimg.save('gif.gif')
#writeGif('gif.gif', gifimg)

#bytes = imgs.getvalue()
#print(len(bytes))


