#import 'pythonista'
import _photos
from _photos import is_authorized

try:
	from _photos2 import *
except ImportError:
	pass

import sys
PY3 = sys.version_info[0] >= 3

if not PY3:
	bytes = str

try:
	from cStringIO import StringIO
except ImportError:
	from io import BytesIO as StringIO

def pick_image(show_albums=False, include_metadata=False, original=True, raw_data=False, multi=False):
	# TODO: Support show_albums, include_metadata parameters
	if raw_data and not original:
		raise ValueError('`raw_data` can only used in combination with `original`')
	assets = pick_asset(multi=multi)
	if not assets:
		return None
	if multi:
		if raw_data:
			return [a.get_image_data(original=original) for a in assets]
		else:
			return [a.get_image(original=original) for a in assets]
	else:
		if raw_data:
			return assets.get_image_data(original=original)
		else:
			return assets.get_image(original=original)

def __pick_image(show_albums=False, include_metadata=False, original=True, raw_data=False, multi=False):
	if raw_data and not original:
		raise ValueError('`raw_data` can only used in combination with `original`')
	picked_items = _photos.pick_image(show_albums, include_metadata, multi, original)
	if picked_items is None or picked_items == (None, None):
		return picked_items
	return_list = []
	for item in picked_items:
		image_data = None
		metadata = None
		if include_metadata:
			image_data, metadata_json = item
			import json
			metadata = json.loads(metadata_json)
		else:
			image_data = item
		if original:
			if raw_data:
				img = image_data
			else:
				from PIL import Image
				data_buffer = StringIO(image_data)
				img = Image.open(data_buffer)
		else:
			data, w, h = image_data
			from PIL import Image
			img = Image.frombytes('RGBA', (w, h), data)
		if include_metadata:
			return_list.append((img, metadata))
		else:
			return_list.append(img)
	if multi:
		return return_list
	return return_list[0]

def capture_image(*args, **kwargs):
	image_info = _photos.capture_image(*args, **kwargs)
	if image_info is None:
		return None
	image_data, w, h = image_info
	from PIL import Image
	img = Image.frombytes('RGBA', (w, h), image_data).convert('RGB')
	return img

def get_count():
	return _photos.get_image_count()

def get_thumbnail(image_index=-1):
	if get_count() == 0:
		return None
	image_info = _photos.get_thumbnail_image(image_index)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		from PIL import Image
		img = Image.frombytes('RGBA', (w, h), image_data)
		return img

def get_image(image_index=-1, original=True, raw_data=False):
	if get_count() == 0:
		return None
	if raw_data and not original:
		raise ValueError('`raw_data` can only used in combination with `original`')
	if not original:
		return get_fullscreen_image(image_index)
	image_data = _photos.get_image_data(image_index)
	if raw_data:
		return image_data
	if isinstance(image_data, bytes):
		from PIL import Image
		jpegdata = StringIO(image_data)
		img = Image.open(jpegdata)
		return img
	return None

def get_fullscreen_image(image_index=-1):
	if get_count() == 0:
		return None
	image_info = _photos.get_fullscreen_image(image_index)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		from PIL import Image
		img = Image.frombytes('RGBA', (w, h), image_data)
		return img

def get_metadata(image_index=-1):
	if get_count() == 0:
		return None
	metadata_json = _photos.get_metadata(image_index)
	if metadata_json is None:
		return None
	else:
		import json
		return json.loads(metadata_json)

def save_image(image):
	import ui
	if isinstance(image, ui.Image):
		return _photos.save_ui_image(image)
	else:
		import io
		b = io.BytesIO()
		if image.mode == 'RGBA':
			image.save(b, 'PNG')
		else:
			image.save(b, 'JPEG', 0.9)
		img_data = b.getvalue()
		ui_img = ui.Image.from_data(img_data)
		return _photos.save_ui_image(ui_img)
