#import 'pythonista'

from _keyboard import *
import _keyboard

current_view = None

def set_view(view=None, mode='current', min_height=0, max_height=0):
	# NOTE: min_height and max_height are currently not implemented.
	_keyboard.set_keyboard_view(view, mode=mode, min_height=min_height, max_height=max_height)
	# Keep a reference, so that the view doesn't get garbage-collected:
	global current_view
	current_view = view

# TODO: Support using this module outside of the custom keyboard for debugging...
