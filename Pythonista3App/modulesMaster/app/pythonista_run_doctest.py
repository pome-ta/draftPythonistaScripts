import sys
import doctest
import console
import os
import imp
import time
import editor

PY3 = sys.version_info[0] >= 3

class PythonistaDocTestRunner (doctest.DocTestRunner):
	def report_start(self, out, test, example):
		pass
	
	def report_success(self, out, test, example, got):
		test_lineno = test.lineno or 0
		editor.annotate_line(lineno=test_lineno + example.lineno + 1, text='OK', style='success', expanded=False, filename=test.filename)
	
	def report_failure(self, out, test, example, got):
		test_lineno = test.lineno or 0
		editor.annotate_line(lineno=test_lineno + example.lineno + 1, text='Got: ' + got, style='error', filename=test.filename)
	
	def report_unexpected_exception(self, out, test, example, exc_info):
		annotation_text = exc_info[0].__name__ + ': ' + str(exc_info[1])
		test_lineno = test.lineno or 0
		editor.annotate_line(lineno=test_lineno + example.lineno + 1, text=annotation_text, style='error', filename=test.filename)

def _testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, optionflags=0, extraglobs=None, parser=doctest.DocTestParser(), encoding=None, runner_class=None):
	'''Modified version of doctest.testfile that allows to pass in a custom DocTestRunner class'''
	if PY3:
		text, filename = doctest._load_testfile(filename, package, module_relative, encoding=encoding or 'utf-8')
	else:
		text, filename = doctest._load_testfile(filename, package, module_relative)
	if name is None:
		name = os.path.basename(filename)
	if globs is None:
		globs = {}
	else:
		globs = globs.copy()
	if extraglobs is not None:
		globs.update(extraglobs)
	if '__name__' not in globs:
		globs['__name__'] = '__main__'
	if runner_class is None:
		runner_class = doctest.DocTestRunner
	runner = runner_class(verbose=verbose, optionflags=optionflags)
	test = parser.get_doctest(text, globs, name, filename, 0)
	runner.run(test)
	return doctest.TestResults(runner.failures, runner.tries)

def _testmod(m=None, name=None, globs=None, verbose=None, optionflags=0, extraglobs=None, exclude_empty=False, runner_class=None):
	'''Modified version of doctest.testmod that allows to pass in a custom DocTestRunner class'''
	if name is None:
		name = m.__name__
	finder = doctest.DocTestFinder(exclude_empty=exclude_empty)
	runner = runner_class(verbose=verbose, optionflags=optionflags)
	for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
		runner.run(test)
	return doctest.TestResults(runner.failures, runner.tries)

def report_result(test_count, fail_count):
	if fail_count > 0:
		console.hud_alert('%i of %i Test%s Failed' % (fail_count, test_count, 's' if test_count > 1 else ''), 'error')
	else:
		if test_count == 0:
			console.hud_alert('No Tests Found', 'error')
		elif test_count == 1:
			console.hud_alert('Test Passed', 'success')
		else:
			console.hud_alert('All %i Tests Passed' % (test_count,), 'success')

def main():
	if len(sys.argv) < 2:
		return
	test_path = sys.argv[1]
	os.chdir(os.path.split(test_path)[0])
	if os.path.splitext(test_path)[1].lower() == '.py':
		mod_name = os.path.splitext(os.path.split(test_path)[1])[0]
		mod = imp.load_source(mod_name, test_path)
		fail_count, test_count = _testmod(mod, runner_class=PythonistaDocTestRunner)
		report_result(test_count, fail_count)
	else:
		fail_count, test_count = _testfile(test_path, module_relative=False, runner_class=PythonistaDocTestRunner)
		report_result(test_count, fail_count)

if __name__ == '__main__':
	main()
