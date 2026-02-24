#\input texinfo

import editor
import os
from pyflakes.api import checkPath
from pyflakes.reporter import Reporter
import sys
import console

if sys.version_info[0] >= 3:
	from io import StringIO
else:
	from StringIO import StringIO

class PythonistaReporter (Reporter):
	def __init__(self, stdout, stderr):
		Reporter.__init__(self, stdout, stderr)
		self.err_count = 0
	
	def syntaxError(self, filename, msg, lineno, offset, text):
		editor.annotate_line(lineno, msg, 'error', filename)
		self.err_count += 1
	
	def flake(self, message):
		message_text = message.message % message.message_args
		if message_text.startswith('local variable '):
			message_text = message_text[len('local variable '):]
		lineno = message.lineno
		filename = message.filename
		editor.annotate_line(lineno, message_text, 'warning', filename)
		self.err_count += 1

def main():
	file_path = editor.get_path()
	if not file_path:
		return
	editor.clear_annotations(file_path)
	reporter = PythonistaReporter(sys.stdout, sys.stderr)
	checkPath(file_path, reporter=reporter)
	if reporter.err_count == 0:
		console.hud_alert('No Issues Found', 'success')
	
	
if __name__ == '__main__':
	main()
