from objc_util import load_framework

load_framework('ImageIO')

import photos

all_assets = photos.get_assets()
last_asset = all_assets[-1]

