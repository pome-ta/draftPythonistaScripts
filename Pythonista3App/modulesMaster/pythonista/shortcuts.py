#import 'pythonista'
import _pythonista
import _webbrowser
import os

from _pythonista import make_url as pythonista_url

def is_running_shortcut():
	import appex
	return appex.is_shortcut()

def open_shortcuts_app(name=None, shortcut_input=''):
	if name is not None:
		from urllib.parse import quote
		_webbrowser.open(f'shortcuts://run-shortcut?name={quote(name)}&input={quote(shortcut_input)}')
	else:
		_webbrowser.open('shortcuts://')

def open_url(url):
	if not isinstance(url, str):
		raise TypeError('url must be a string')
	if is_running_shortcut():
		_pythonista.defer_to_app(url)
	else:
		_webbrowser.open(url)

def set_spoken_output(text):
	if not isinstance(text, str):
		raise TypeError('text must be a string')
	_pythonista.set_shortcut_spoken_result(text)

def set_result_html(html):
	if not isinstance(html, str):
		raise TypeError('html must be a string')
	_pythonista.set_shortcut_html_result(html)

def set_output_files(files):
	# TODO: Validate format (list of dicts with 'path', 'filename', 'data', 'uti' keys
	# TODO: Convert file paths to absolute paths before passing on to _pythonista module (which doesn't do any checks)
	_pythonista.set_shortcut_output_items(files)

def set_output_data(data, filename, uti=None):
	if not isinstance(data, bytes):
		raise TypeError('data must be bytes')
	if not isinstance(filename, str):
		raise TypeError('filename must be a string')
	set_output_files([{'data': data, 'filename': filename}])

def set_output_text(text, filename='output.txt'):
	if not isinstance(text, str):
		raise TypeError('text must be a string')
	if not isinstance(filename, str):
		raise TypeError('filename must be a string')
	set_output_files([{'data': text.encode('utf-8'), 'filename': filename}])

def set_output_image(image):
	if isinstance(image, str):
		if os.path.isfile(image):
			set_output_files([{'path': os.path.abspath(image)}])
			return
		else:
			raise IOError('File not found')
	if image.__class__.__name__ == 'Image' and image.__class__.__module__ == '_ui':
		png = image.to_png()
		set_output_files([{'data': png, 'filename': 'Image.png'}])
		return
	
	if hasattr(image, 'save'):
		import io
		buffer = io.BytesIO()
		image.save(buffer, 'PNG')
		png = buffer.getvalue()
		set_output_files([{'data': png, 'filename': 'Image.png'}])
		return
	# Not a valid image
	raise TypeError('Expected image path or ui.Image/PIL.Image.Image object')

