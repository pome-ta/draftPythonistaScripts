#import 'pythonista'
# coding: utf-8

import _debugger_ui, bdb, sys, editor, ui, threading, os, types, objc_util, ui, scene
if sys.version_info[0] >= 3:
	from io import StringIO
else:
	from StringIO import StringIO

CMD_STEP = 1
CMD_NEXT = 2
CMD_RETURN = 3
CMD_CONTINUE = 4
CMD_QUIT = 5

class PythonistaDebugger (bdb.Bdb):
	def __init__(self, skip=None):
		bdb.Bdb.__init__(self, skip)
		self.dont_stop = True
	
	def reset(self):
		bdb.Bdb.reset(self)
		self.dont_stop = True
		
	def set_trace(self, frame=None):
		if frame is None:
			frame = sys._getframe().f_back
		self.reset()
		while frame:
			frame.f_trace = self.trace_dispatch
			self.botframe = frame
			frame = frame.f_back
		self.set_step()
		self.dont_stop = False
		sys.settrace(self.trace_dispatch)
	
	def run(self, cmd, globals=None, locals=None):
		if globals is None:
			import __main__
			globals = __main__.__dict__
		if locals is None:
			locals = globals
		self.reset()
		sys.settrace(self.trace_dispatch)
		ui.settrace(self.trace_dispatch)
		threading.settrace(self.trace_dispatch)
		objc_util.settrace(self.trace_dispatch)
		scene.settrace(self.trace_dispatch)
		
		if not isinstance(cmd, types.CodeType):
			cmd = cmd+'\n'
		try:
			exec (cmd, globals, locals)
		except bdb.BdbQuit:
			pass
		finally:
			# Set sys trace to None, but don't quit -- this allows to break in UI actions
			# (when the main script isn't running anymore)
			sys.settrace(None)
		
	def stop_here(self, frame):
		if self.dont_stop:
			# Don't stop on the first frame (unlike bdb.Bdb)
			self.dont_stop = False
			self.set_continue()
			return False
		return bdb.Bdb.stop_here(self, frame)
	
	def user_line(self, frame):
		cmd = _debugger_ui.interaction(frame)
		if cmd == CMD_CONTINUE:
			self.set_continue()
		elif cmd == CMD_NEXT:
			self.set_next(frame)
		elif cmd == CMD_RETURN:
			self.set_return(frame)
		elif cmd == CMD_STEP:
			self.set_step()
		elif cmd == CMD_QUIT:
			self.set_quit()


debugger = PythonistaDebugger()

def set_trace():
	debugger.set_trace()
    