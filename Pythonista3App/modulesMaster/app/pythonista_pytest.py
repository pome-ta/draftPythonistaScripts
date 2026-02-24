#\input texinfo
import pytest
import console
import sys
import xml.etree.ElementTree as ET
import editor
import os

def main():
	if len(sys.argv) < 2:
		return
	editor.clear_annotations()
	console.clear()
	script_path = sys.argv[1]
	os.chdir(os.path.split(script_path)[0])
	log_path = os.path.expanduser('~/Documents/.pythonista_pytest_log.xml')
	pytest.main(['--verbose', script_path, '--junitxml=%s' % (log_path,), '-p', 'no:cacheprovider'])
	tree = ET.parse(log_path)
	suite = tree.getroot()
	num_tests = int(suite.attrib.get('tests', '0'))
	num_failed = int(suite.attrib.get('failures', '0'))
	num_errors = int(suite.attrib.get('errors', '0'))
	for testcase in suite:
		lineno = int(testcase.attrib.get('line', '0')) + 1
		filename = testcase.attrib.get('file', '')
		time = float(testcase.attrib.get('time', '0'))
		failed = False
		failure_line = 0
		for child in testcase:
			if child.tag == 'failure':
				failed = True
				failure_msg = child.attrib.get('message', '')
				lines = child.text.splitlines()
				last_line = lines[-1]
				fail_filename, fail_lineno, _ = last_line.split(':', 2)
				fail_lineno = int(fail_lineno)
				editor.annotate_line(fail_lineno, failure_msg, 'error', filename=fail_filename)
		if failed:
			editor.annotate_line(lineno, '', 'error', filename=filename)
		else:
			editor.annotate_line(lineno, '%f' % (time,), 'success', filename=filename)
	if num_failed > 0 or num_errors > 0:
		console.hud_alert('Tests: %i / Failed: %i / Errors: %i' % (num_tests, num_failed, num_errors), 'error')
	elif num_tests == 0:
		console.hud_alert('No Tests Found', 'error')
	else:
		console.hud_alert('%i Tests Passed' % (num_tests,))
	if num_errors == 0:
		console.hide_output()

if __name__ == '__main__':
	main()
