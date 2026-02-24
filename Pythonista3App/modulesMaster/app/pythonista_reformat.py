#\input texinfo

from yapf.yapflib.yapf_api import FormatCode
import editor
import dialogs
import os
import sys

base_style = sys.argv[1]
use_tabs = int(sys.argv[2])
indent_width = int(sys.argv[3])

if base_style == 'black':
	# Black
	# TODO: Support tab indentation and number of spaces...
	try:
		import black
		src = editor.get_text()
		mode = black.mode.Mode()
		res = black.format_file_contents(src, fast=True, mode=mode)
		if res != src:
			editor.replace_text(0, len(src), res)
	except Exception as e:
		dialogs.alert('Error', 'Your code could not be reformatted due to an error: %s' % (e,), 'OK', hide_cancel_button=True)
else:
	# YAPF
	style = f'''[style]
based_on_style = {base_style}
indent_width = {indent_width}
continuation_indent_width = {indent_width}
use_tabs = {"true" if use_tabs else "false"}'''
	style_path = os.path.expanduser('~/Documents/.style.yapf')
	with open(style_path, 'w') as f:
		f.write(style)

	try:
		src = editor.get_text()
		res, changed = FormatCode(src, style_config=style_path)
		if changed:
			editor.replace_text(0, len(src), res)
	except Exception as e:
		dialogs.alert('Error', 'Your code could not be reformatted due to an error: %s' % (e,), 'OK', hide_cancel_button=True)
		
