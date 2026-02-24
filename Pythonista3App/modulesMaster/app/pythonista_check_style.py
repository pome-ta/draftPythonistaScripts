import editor
import os
import pycodestyle as pep8
import sys
import console
from objc_util import ObjCClass

if sys.version_info[0] >= 3:
	from io import StringIO
else:
	from StringIO import StringIO

def main():
	file_path = editor.get_path()
	if not file_path:
		return
	defaults = ObjCClass('NSUserDefaults').standardUserDefaults()
	ignored_str = defaults.stringForKey_('StyleCheckerIgnoredErrorCodes')
	if ignored_str:
		ignored = [e for e in str(ignored_str).split(',') if len(e) > 0]
	else:
		ignored = []
	editor.clear_annotations(file_path)
	prev_default_ignore = pep8.DEFAULT_IGNORE
	pep8.DEFAULT_IGNORE = ''
	pep8style = pep8.StyleGuide(**({'ignore': ignored} if ignored else {}))
	stdout = sys.stdout
	output_buffer = StringIO()
	sys.stdout = output_buffer
	try:
		pep8style.check_files([file_path])
	finally:
		sys.stdout = stdout
		pep8.DEFAULT_IGNORE = prev_default_ignore
	output_lines = output_buffer.getvalue().splitlines()
	for line in output_lines:
		comps = line.split(':', 3)
		filename, lineno, col, msg = comps
		editor.annotate_line(int(lineno), msg, 'warning', filename)
	if not output_lines:
		console.hud_alert('No Issues Found')
	
if __name__ == '__main__':
	main()
