# coding: utf-8

def _debug_execfile(file_path):
	with open(file_path, encoding='utf-8') as f:
		exec(compile(f.read(), file_path, 'exec'), globals())

def _debug_main():
	import sys, os
	from bdb import BdbQuit
	from debugger import debugger as d
	sys.settrace(None)
	
	d.clear_all_breaks()
	d.reset()
	script_path = sys.argv[1]
	breakpoints = sys.argv[2:]
	for bp in breakpoints:
		bp_path, lineno = bp.split(':')
		d.set_break(d.canonic(bp_path), int(lineno))
	script_dir = os.path.split(script_path)[0]
	os.chdir(script_dir)
	sys.path = [script_dir] + sys.path
	globals()['__file__'] = script_path
	try:
		if sys.version_info[0] >= 3:
			d.run('_debug_execfile("%s")' % (script_path,))
		else:
			d.run('execfile("%s")' % (script_path,))
	except BdbQuit:
		pass
	
if __name__ == '__main__':
	_debug_main()
