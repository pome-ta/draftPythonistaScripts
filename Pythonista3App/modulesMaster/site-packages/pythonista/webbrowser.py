#import 'pythonista'

from objc_util import UIApplication, ObjCClass, nsurl, load_framework
import sys
PY3 = sys.version_info[0] >= 3
if PY3:
	from urllib.parse import quote
	basestring = str
else:
	from urllib import quote

try:
	import appex
	is_widget = appex.is_widget()
	is_extension = appex.is_running_extension()
except:
	is_widget = False
	is_extension = False


class Error (Exception):
	pass


def _url_to_nsurl(url):
	if not isinstance(url, basestring):
		raise Error('Invalid URL, not a string')
	# NOTE: This will automatically create file URLs for paths:
	nsurl_obj = nsurl(url)
	if not nsurl_obj:
		raise Error('Invalid URL')
	return nsurl_obj


class DefaultBrowser (object):
	def open(self, url, new=0, autoraise=True, **kwargs):
		modal = kwargs.get('modal', False)
		objc_url = _url_to_nsurl(url)
		# modal parameter is only supported for http(s) and file URLs:
		webview_can_open = url.startswith('http:') or url.startswith('https:') or (':' not in url)
		if modal and webview_can_open:
			# Modal sheet, block until dismissed
			import ui
			webview = ui.WebView()
			webview.name = 'Web'
			webview.load_url(url)
			webview.present('fullscreen')
			webview.wait_modal()
			return True
		if url.startswith('safari-http://') or url.startswith('safari-https://'):
			http_url = url[7:]
			safari = MobileSafari()
			return safari.open(http_url, new=new, autoraise=autoraise, **kwargs)
		if url.startswith('http:') or url.startswith('https:') or url.startswith('file:'):
			if is_extension:
				# in-app browser is not supported in share sheet ext.
				return MobileSafari().open(url, new=new, autoraise=autoraise, **kwargs)
			# Open in-app (host app handles notification)
			info = {'URL': url, 'reveal': autoraise, 'newTab': bool(new)}
			center = ObjCClass('NSNotificationCenter').defaultCenter()
			center.postNotificationName_object_userInfo_('WebBrowserOpenURLNotification', None, info)
			return True
		else:
			# Open in default app...
			safari = MobileSafari()
			return safari.open(url, new=new, autoraise=autoraise, **kwargs)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)

_default_browser = DefaultBrowser()


class MobileSafari (object):
	def open(self, url, new=0, autoraise=True):
		objc_url = _url_to_nsurl(url)
		if is_widget:
			PYKAppContext = ObjCClass('PYK3AppContext' if PY3 else 'PYK2AppContext')
			extension_context = PYKAppContext.sharedContext().extensionContext()
			extension_context.openURL_completionHandler_(objc_url, None)
			return True
		else:
			return UIApplication.sharedApplication().openURL_(objc_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


class Chrome (object):
	def open(self, url, new=0, autoraise=True):
		# NOTE: If `new` is >0, a new tab will *always* be opened, otherwise, a new tab will still be opened
		# for pages that aren't already open in an existing tab.
		if not (url.startswith('http:') or url.startswith('https:')):
			raise Error('This browser only supports http(s) URLs')
		quoted_url = quote(url, '')
		new_url = 'googlechrome-x-callback://x-callback-url/open?url=' + quoted_url
		if new:
			new_url += '&create-new-tab'
		return _default_browser.open(new_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


class iCab (object):
	def open(self, url, new=0, autoraise=True):
		if not (url.startswith('http:') or url.startswith('https:')):
			raise Error('This browser only supports http(s) URLs')
		scheme = 'icabmobiles' if url.startswith('https:') else 'icabmobile'
		new_url = scheme + ':' + url.split(':', 1)[1]
		return _default_browser.open(new_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


class Opera (object):
	def open(self, url, new=0, autoraise=True):
		if not (url.startswith('http:') or url.startswith('https:')):
			raise Error('This browser only supports http(s) URLs')
		scheme = 'opera-https' if url.startswith('https:') else 'opera-http'
		new_url = scheme + ':' + url.split(':', 1)[1]
		return _default_browser.open(new_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


class OperaCoast (object):
	def open(self, url, new=0, autoraise=True):
		if not (url.startswith('http:') or url.startswith('https:')):
			raise Error('This browser only supports http(s) URLs')
		scheme = 'coast-https' if url.startswith('https:') else 'coast-http'
		new_url = scheme + ':' + url.split(':', 1)[1]
		return _default_browser.open(new_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


class Mercury (object):
	def open(self, url, new=0, autoraise=True):
		if not (url.startswith('http:') or url.startswith('https:')):
			raise Error('This browser only supports http(s) URLs')
		quoted_url = quote(url, '')
		new_url = 'merc://' + quoted_url
		return _default_browser.open(new_url)

	def open_new(self, url):
		return self.open(url, new=1)

	def open_new_tab(self, url):
		return self.open(url, new=2)


def open(url, new=0, autoraise=True, **kwargs):
	_default_browser.open(url, new=new, autoraise=autoraise, **kwargs)

def open_new(url):
	_default_browser.open_new(url)

def open_new_tab(url):
	_default_browser.open_new_tab(url)

def get(name=''):
	name = name.lower()
	if name in ('', 'default', 'in-app'):
		return _default_browser
	elif name in ('safari', 'macosx'):
		return MobileSafari()
	elif name in ('google-chrome', 'chrome', 'chromium', 'chromium-browser'):
		return Chrome()
	elif name == 'icab':
		return iCab()
	elif name == 'opera':
		return Opera()
	elif name == 'coast':
		return OperaCoast()
	elif name == 'mercury':
		return Mercury()
	raise Error('could not locate runnable browser')

def register(name, constructor, instance=None):
	raise NotImplementedError('webbrowser.register is not implemented on iOS')

# Pythonista-specific:

def can_open(url):
	# NOTE: This function is deprecated!
	# Validate that this is a well-formed URL:
	nsurl_obj = _url_to_nsurl(url)
	# Always return True (since iOS 9, it cannot be correctly determined
	# anymore whether the URL can actually be opened):
	return True

def add_to_reading_list(url, title=None, preview_text=None):
	objc_url = _url_to_nsurl(url)
	if title is not None and not isinstance(title, basestring):
		raise Error('title must be a string or None')
	if preview_text is not None and not isinstance(preview_text, basestring):
		raise Error('preview_text must be a string or None')
	load_framework('SafariServices')
	reading_list = ObjCClass('SSReadingList').defaultReadingList()
	return reading_list.addReadingListItemWithURL_title_previewText_error_(objc_url, title, preview_text, None)
