#import 'pythonista'
import _clipboard

import sys
if sys.version_info[0] >= 3:
	basestring = str
	PY3 = True
else:
	PY3 = False

def get():
	"""get() -- Get the clipboard's text content as a unicode string"""
	s = _clipboard.get()
	if s is None:
		return None
	if PY3:
		return s
	return unicode(s, 'utf-8')

def set(s):
	"""set(string) -- Set the clipboard's content to a string"""
	if not isinstance(s, basestring):
		raise TypeError('Expected a string')
	if PY3:
		_clipboard.set(s)
	elif isinstance(s, unicode):
		_clipboard.set(s.encode('utf-8'))
	else:
		_clipboard.set(s)

def get_image(idx=0, format='pil'):
	"""Get the image at the given index in the clipboard as a PIL.Image. Returns None if the index is >= the number of images in the clipboard."""
	if format == 'ui':
		return _clipboard.get_ui_image(idx)
	else:
		image_info = _clipboard.get_image_data(idx)
		if image_info is None:
			return None
		image_data, w, h = image_info
		import PIL, io
		image_fp = io.BytesIO(image_data)
		return PIL.Image.open(image_fp)

def set_image(image, format='png', jpeg_quality=0.75):
	"""Set the clipboard to a given PIL.Image or ui.Image."""
	format = format.lower()
	is_jpeg = (format == 'jpeg' or format == 'jpg')
	import ui
	if isinstance(image, ui.Image):
		_clipboard.set_ui_image(image, is_jpeg, jpeg_quality)
	else:
		rgba_image = image
		if image.mode != 'RGBA':
			rgba_image = image.convert('RGBA')
		image_data = rgba_image.tostring()
		_clipboard.set_image_data(image_data, image.size[0], image.size[1], is_jpeg, jpeg_quality)
