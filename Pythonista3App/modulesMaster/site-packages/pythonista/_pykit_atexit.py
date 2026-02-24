#import 'pythonista'

registered_functions = {}

def register(key, func):
	registered_functions[key] = func

def unregister(key):
	try:
		del registered_functions[key]
	except KeyError:
		pass

def exit():
	for func in registered_functions.values():
		try:
			func()
		except:
			pass