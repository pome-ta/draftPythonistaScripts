#import 'pythonista'
# coding: utf-8

import appex
if appex.is_running_extension():
	raise NotImplementedError('Not available in app extension')

from objc_util import *
import json
import ui
import os

from _pythonista import make_url

theme_cache = {}
theme_filenames = {'Default': 'Default', 'Dawn': 'Theme01_Dawn', 'Tomorrow': 'Theme02_Tomorrow', 'Solarized Light': 'Theme03_SolarizedLight', 'Solarized Dark': 'Theme04_SolarizedDark 2', 'Cool Glow': 'Theme05_CoolGlow', 'Gold': 'Theme06_Gold', 'Tomorrow Night': 'Theme07_TomorrowNight', 'Oceanic': 'Theme08_Oceanic', 'Editorial': 'Theme09_Editorial'}

PASlidingContainerViewController = ObjCClass('PASlidingContainerViewController')
PA2UniversalTextEditorViewController = ObjCClass('PA2UniversalTextEditorViewController')
OMTextRange = ObjCClass('OMTextRange')
PA3LibraryManager = ObjCClass('PA3LibraryManager')

@on_main_thread
def _get_editor_tab(only_text=True):
	win = UIApplication.sharedApplication().keyWindow()
	root_vc = win.rootViewController()
	if root_vc.isKindOfClass_(PASlidingContainerViewController):
		tabs_vc = root_vc.detailViewController()
		tab = tabs_vc.selectedTabViewController()
		if not only_text or tab.isKindOfClass_(PA2UniversalTextEditorViewController):
			return tab
	return None

def _validate_range(start, end, strict=False):
	if end is None:
		end = start
	if start > end:
		raise ValueError('Start of range must be <= end')
	if start < 0:
		raise ValueError('Start of range must be >= 0')
	text = get_text()
	if end >= len(text):
		if strict:
			raise ValueError('Range out of bounds')
		else:
			end = max(0, len(text) - 1)
	if start >= len(text):
		if strict:
			raise ValueError('Range out of bounds')
		else:
			start = max(0, len(text) - 1)
	return (start, end)

@on_main_thread
def get_path():
	tab = _get_editor_tab(only_text=False)
	if not tab:
		return None
	if tab.respondsToSelector_(sel('filePath')):
		return str(tab.filePath())

@on_main_thread
def get_text():
	tab = _get_editor_tab()
	if not tab:
		return None
	return str(tab.editorView().textView().text())

@on_main_thread
def get_selection():
	tab = _get_editor_tab()
	if not tab:
		return None
	r = tab.editorView().textView().selectedRange()
	if r.location != NSNotFound:
		return (r.location, r.location + r.length)

def get_line_selection():
	start, end = get_selection()
	text = get_text()
	while start > 0:
		if text[start-1] == '\n':
			break
		start -= 1
	while text[end] != '\n' and end < len(text) - 1:
		if text[end] == '\n':
			break
		end += 1
	return start, end

@on_main_thread
def set_selection(start, end=None, scroll=False):
	start, end = _validate_range(start, end, strict=False)
	tab = _get_editor_tab()
	if not tab:
		return
	text_view = tab.editorView().textView()
	text_view.setSelectedRange_(NSRange(start, end-start))
	if scroll:
		text_view.scrollToCaretAnimated_withMinimumBottomOffset_(False, 40)

@on_main_thread
def replace_text(start, end, replacement):
	start, end = _validate_range(start, end)
	tab = _get_editor_tab()
	if not tab:
		return
	text_view = tab.editorView().textView()
	r = OMTextRange.rangeWithNSRange_(NSRange(start, end-start))
	text_view.replaceRange_withText_(r, replacement)

@on_main_thread
def make_new_file(name=None, content=None, new_tab=False):
	doc_path = os.path.expanduser('~/Documents')
	if content is None:
		content = ''
	if name is None:
		name = 'Untitled'
	if name.startswith('/'):
		full_path = name
	else:
		full_path = os.path.join(doc_path, name)
	suffix = 1
	while os.path.exists(full_path):
		base_name, ext = os.path.splitext(name)
		new_name = base_name + '_' + str(suffix) + ext
		full_path = os.path.join(doc_path, new_name)
		suffix += 1
	with open(full_path, 'w', encoding='utf-8') as f:
		f.write(content)
	open_file(full_path, new_tab=new_tab)

@on_main_thread
def open_file(name, new_tab=False):
	if not name.startswith('/'):
		doc_path = os.path.expanduser('~/Documents')
		name = os.path.join(doc_path, name)
	if not os.path.exists(name) or not os.path.isfile(name):
		raise FileNotFoundError('"%s" not found' % (name,))
	PA3LibraryManager.sharedManager().openFilePathInEditor_preferNewTab_(name, new_tab)

def reload_files():
	# No longer needed, just a stub for backwards-compatibility
	pass

def get_theme_dict(name=None):
	if name is None:
		defaults = ObjCClass('NSUserDefaults').standardUserDefaults()
		name = str(defaults.stringForKey_('ThemeName'))
	if not name:
		name = 'Default'
	if name.startswith('User:'):
		home_dir = os.environ.get('CFFIXED_USER_HOME')
		user_themes_path = os.path.join(home_dir, 'Library/Application Support/Themes')
		theme_path = os.path.join(user_themes_path, name[5:] + '.json')
	else:
		cached_theme = theme_cache.get(name)
		if cached_theme:
			return cached_theme
		filename = theme_filenames[name] if name in theme_filenames else name
		res_path = str(ObjCClass('NSBundle').mainBundle().resourcePath())
		theme_path = os.path.join(res_path, 'Themes2/%s.json' % filename)
	with open(theme_path, 'r') as f:
		theme_dict = json.load(f)
		if not name.startswith('User:'):
			theme_cache[name] = theme_dict
		return theme_dict

def _use_dark_keyboard(v, dark=True):
	if isinstance(v,ui.TextView):
		ObjCInstance(v).setKeyboardAppearance_(dark)
	elif isinstance(v,ui.TextField):
		ObjCInstance(v).subviews()[0].setKeyboardAppearance_(dark)

def apply_ui_theme(v, theme_name=None):
	t = get_theme_dict(theme_name)
	bg = ui.parse_color(t['background'])
	dark_theme = sum(bg[:3])/3.0 < 0.5
	v.tint_color = t['tint']
	if isinstance(v, (ui.Label, ui.TextView, ui.TextField)):
		v.text_color = t['default_text']
	if isinstance(v, ui.TextField) and dark_theme:
		v.bordered = False
		v.background_color = t['bar_background']
		v.text_color = t['default_text']
		v.corner_radius = 4
	if isinstance(v, (ui.TextField, ui.TextView)):
		_use_dark_keyboard(v, True)
	if isinstance(v, ui.DatePicker):
		r, g, b, _ = ui.parse_color(t['default_text'])
		text_ui_color = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(r, g, b, 1)
		ObjCInstance(v).setValue_forKey_(text_ui_color, 'textColor')
	for sv in v.subviews:
		apply_ui_theme(sv, theme_name)

def present_themed(v, theme_name=None, **kwargs):
	apply_ui_theme(v, theme_name)
	t = get_theme_dict(theme_name)
	bg_color = t.get('background')
	bar_bg = t.get('bar_background', 'white')
	text_color = t.get('default_text', 'black')
	v.background_color = bg_color
	v.present(title_bar_color=bar_bg, title_color=text_color, **kwargs)

# Line annotations:

@on_main_thread
def _get_editors(filename):
	found_tabs = []
	win = UIApplication.sharedApplication().keyWindow()
	root_vc = win.rootViewController()
	if root_vc.isKindOfClass_(ObjCClass('PASlidingContainerViewController')):
		tabs_vc = root_vc.detailViewController()
		for tab in tabs_vc.tabViewControllers():
			if tab.isKindOfClass_(ObjCClass('PA2UniversalTextEditorViewController')):
				if not tab.isViewLoaded():
					continue
				tab_path = str(tab.filePath())
				if tab_path == filename:
					found_tabs.append(tab)
	return found_tabs

@on_main_thread
def annotate_line(lineno, text='', style='warning', expanded=True, filename=None, scroll=False):
	if filename is None:
		filename = get_path()
	filename = os.path.abspath(filename)
	editors = _get_editors(filename)
	if not editors:
		return
	for editor_vc in editors:
		editor_view = editor_vc.editorView()
		styles = {'success': 0, 'warning': 1, 'error': 2, 'mark': 3}
		annotation = {'style': styles.get(style, 1), 'text': text, 'expanded': bool(expanded)}
		editor_view.setLineAnnotation_forParagraphAtIndex_(annotation, lineno - 1)
		if scroll:
			editor_view.scrollToLineAtIndex_(lineno - 1)

@on_main_thread
def clear_annotations(filename=None):
	if filename is None:
		filename = get_path()
	filename = os.path.abspath(filename)
	editors = _get_editors(filename)
	for editor_vc in editors:
		editor_view = editor_vc.editorView()
		editor_view.removeAllLineAnnotations()
