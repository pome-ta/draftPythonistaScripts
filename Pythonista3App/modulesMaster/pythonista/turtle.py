#import 'pythonista'
# coding: utf-8

# ui-based iOS port of the turtle module (not 100% compatible with standard library
# turtle module, but most things beginners would use should work)

import ui
from math import *
import math
import time
import sys
import numbers
import threading
import appex

PY3 = sys.version_info[0] >= 3
if PY3:
	basestring = str

_default_size = min(ui.get_screen_size()) - 100
_main_view = None
_default_pen = None
_default_color_mode = 1.0
_canvas_size = max(ui.get_screen_size())
_canvas_image = None
_all_pens = []

if appex.is_shortcut():
	_default_size = 320
	_canvas_size = 320

# When the pen is set to 'fastest', this is how many drawing commands are batched:
batch_size = 100

class Vec2D(tuple):
	"""A 2 dimensional vector class, used as a helper class
	for implementing turtle graphics.
	May be useful for turtle graphics programs also.
	Derived from tuple, so a vector is a tuple!

	Provides (for a, b vectors, k number):
	   a+b vector addition
	   a-b vector subtraction
	   a*b inner product
	   k*a and a*k multiplication with scalar
	   |a| absolute value of a
	   a.rotate(angle) rotation
	"""
	def __new__(cls, x, y):
		return tuple.__new__(cls, (x, y))
	def __add__(self, other):
		return Vec2D(self[0]+other[0], self[1]+other[1])
	def __mul__(self, other):
		if isinstance(other, Vec2D):
			return self[0]*other[0]+self[1]*other[1]
		return Vec2D(self[0]*other, self[1]*other)
	def __rmul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Vec2D(self[0]*other, self[1]*other)
	def __sub__(self, other):
		return Vec2D(self[0]-other[0], self[1]-other[1])
	def __neg__(self):
		return Vec2D(-self[0], -self[1])
	def __abs__(self):
		return (self[0]**2 + self[1]**2)**0.5
	def rotate(self, angle):
		"""rotate self counterclockwise by angle
		"""
		perp = Vec2D(-self[1], self[0])
		angle = angle * math.pi / 180.0
		c, s = math.cos(angle), math.sin(angle)
		return Vec2D(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)
	def __getnewargs__(self):
		return (self[0], self[1])
	def __repr__(self):
		return "(%.2f,%.2f)" % self


class PenView (ui.View):
	def draw(self):
		if _canvas_image:
			_canvas_image.draw()
		for pen in _all_pens:
			if not pen._turtle_visible:
				continue
			with ui.GState():
				ui.concat_ctm(ui.Transform.translation(self.superview.width/2, self.superview.height/2))
				pen_tip = ui.Path()
				pen_tip.move_to(-10, -5)
				pen_tip.line_to(0, 0)
				pen_tip.line_to(-10, 5)
				pen_tip.close()
				ui.concat_ctm(ui.Transform.translation(*pen._pos))
				ui.concat_ctm(ui.Transform.rotation(pen._angle))
				ui.set_color(pen._current_color)
				pen_tip.fill()
	
	def set_needs_display(self, make_visible=True):
		ui.View.set_needs_display(self)
		if make_visible and not appex.is_shortcut():
			_main_view.present()

_pen_view = PenView()

class TurtleView (ui.View):
	def __init__(self, *args, **kwargs):
		ui.View.__init__(self, *args, **kwargs)
		self.name = 'Turtle Graphics'
		self.canvas_view = ui.View(frame=(0, 0, _default_size, _default_size), bg_color='white')
		self.bg_color = (0.9, 0.9, 0.9, 1.0)
		self.tint_color = (0.2, 0.2, 0.2, 1.0)
		self.add_subview(self.canvas_view)
		clear_btn_item = ui.ButtonItem('Clear', action=self.clear_action)
		save_btn_item = ui.ButtonItem('Save', action=self.save_action)
		self.right_button_items = [save_btn_item, clear_btn_item]
		_pen_view.frame = self.canvas_view.bounds
		_pen_view.flex = 'WH'
		self.canvas_view.add_subview(_pen_view)
		self.title_label = ui.Label(frame=(0, 0, self.width, 40), flex='W')
		self.title_label.alignment = ui.ALIGN_CENTER
		self.title_label.text = 'Turtle Graphics'
		self.title_label.text_color = (0.4, 0.4, 0.4, 1.0)
		self.title_label.font = ('<System>', 14)
		self.add_subview(self.title_label)
		save_button = ui.Button(image=ui.Image('iow:ios7_download_outline_24'), flex='LB')
		save_button.frame = (self.width - 40, 0, 40, 40)
		save_button.action = self.save_action
		self.add_subview(save_button)
	
	def layout(self):
		# NOTE: When this is called, the previous imports might already have gone out of scope.
		import ui
		center = ui.Point(self.width/2, self.height/2)
		self.canvas_view.frame = (center.x - self.canvas_view.width/2, center.y - self.canvas_view.height/2, self.canvas_view.width, self.canvas_view.height)
	
	def present(self):
		import objc_util
		objc_view = objc_util.ObjCInstance(self)
		user_info = {'view': objc_view}
		objc_util.ObjCClass('NSNotificationCenter').defaultCenter().postNotificationName_object_userInfo_('ConsoleShowGraphicsViewNotification', None, user_info)
	
	def reset(self):
		self.setup(_default_size, _default_size)
		global _canvas_image
		_canvas_image = None
		_default_pen.reset()
		_all_pens[:] = [_default_pen]
		self.canvas_view.bg_color = 'white'
		self.title('Turtle Graphics')
	
	def clear_action(self, sender):
		# NOTE: Used by clearscreen, could also be attached to a UI element (but isn't currently)
		global _canvas_image
		_canvas_image = None
		_pen_view.set_needs_display()
	
	def save_action(self, sender):
		# NOTE: When this is called, the previous imports might already have gone out of scope.
		import photos, dialogs, ui
		with ui.ImageContext(self.canvas_view.width, self.canvas_view.height) as ctx:
			self.canvas_view.draw_snapshot()
			img = ctx.get_image()
		photos.save_image(img)
		if not photos.is_authorized():
			dialogs.hud_alert('Cannot Save', 'error')
		else:
			dialogs.hud_alert('Saved to Photos')
	
	def title(self, title_str):
		self.name = str(title_str)
		self.title_label.text = title_str
	
	def tracer(self, n=None, delay=None):
		if delay is not None:
			for pen in self.turtles():
				pen.delay_sec = delay / 100.0
	
	def delay(self, delay=None):
		if delay is not None:
			for pen in self.turtles():
				pen.delay_sec = delay / 100.0

	def setup(self, width=None, height=None, **kwargs):
		if width is None:
			width = _default_size
		if height is None:
			height = _default_size
		self.canvas_view.bounds = (0, 0, width, height)
	
	def bgcolor(self, *args):
		if len(args) == 1 and isinstance(args[0], basestring):
			self.canvas_view.bg_color = ui.parse_color(args[0])
		elif len(args) == 1:
			r, g, b = args[0]
			if _default_pen._colormode == 255:
				r, g, b = (r/255.0, g/255.0, b/255.0)
			self.canvas_view.bg_color = (r, g, b)
		elif len(args) == 3:
			r, g, b = args
			if _default_pen._colormode == 255:
				r, g, b = (r/255.0, g/255.0, b/255.0)
			self.canvas_view.bg_color = (r, g, b)
	
	def turtles(self):
		return _all_pens

	def clearscreen(self):
		self.clear_action(None)

	def update(self):
		pass


class Pen (object):
	def __init__(self, *args, **kwargs):
		self._use_rad = False
		self._current_color = (0, 0, 0, 1)
		self._current_fill_color = (0, 0, 0, 1)
		self._colormode = _default_color_mode
		self._line_width = 1.0
		self._angle = 0.0
		self._pos = ui.Point(0, 0)
		self._turtle_visible = True
		self.is_down = True
		self.fill_path = None
		if appex.is_shortcut():
			self.delay_sec = 0.0
			self.anim_steps = 1
		else:
			self.delay_sec = 0.01
			self.anim_steps = 4
		self.canvas_size = ui.Size(512, 512)
		self.batched_drawings = []
		_all_pens.append(self)
	
	def _sleep(self):
		time.sleep(self.delay_sec)
	
	def degrees(self):
		""" Set angle measurement units to degrees."""
		self._use_rad = False

	def radians(self):
		""" Set angle measurement units to radians."""
		self._use_rad = True
	
	def _color_args_to_rgba(self, args):
		"""Helper method to convert various color formats to r,g,b,a (with 0.0-1.0 ranges)"""
		r, g, b, a = 0, 0, 0, 1
		if len(args) >= 3:
			r, g, b = args[:3]
			if self._colormode == 255:
				r, g, b = (r/255.0, g/255.0, b/255.0)
			a = args[3] if len(args) > 3 else 1.0
		elif len(args) == 1 and isinstance(args[0], basestring):
			r, g, b, a = ui.parse_color(args[0])
		elif len(args) == 1:
			r, g, b = args[0][:3]
			if self._colormode == 255:
				r, g, b = (r/255.0, g/255.0, b/255.0)
			a = args[0][3] if len(args[0]) > 3 else 1.0
		return (r, g, b, a)
	
	def _angle_to_rad(self, angle):
		if self._use_rad:
			return angle
		return math.radians(angle)
	
	def _add_drawing(self, draw_func, force_flush=False):
		if self.delay_sec == 0:
			self.batched_drawings.append(draw_func)
			if len(self.batched_drawings) < batch_size and not force_flush:
				return
		
		with ui.ImageContext(_canvas_size, _canvas_size) as ctx:
			with ui.autoreleasepool():
				global _canvas_image
				if _canvas_image:
					_canvas_image.draw(0, 0)
				ui.concat_ctm(ui.Transform.translation(_pen_view.superview.width/2, _pen_view.superview.height/2))
				if self.batched_drawings:
					for batched_draw_func in self.batched_drawings:
						batched_draw_func()
					self.batched_drawings = []
					_canvas_image = ctx.get_image()
					self.update_view()
				else:
					draw_func()
					_canvas_image = ctx.get_image()
	
	def _force_flush(self):
		if self.batched_drawings:
			self._add_drawing(lambda: None, force_flush=True)

	def reset(self):
		"""Delete the turtle's drawings and restore its default values.

		No argument.

		Delete the turtle's drawings from the screen, re-center the turtle
		and set variables to the default values.

		Example (for a Turtle instance named turtle):
		>>> turtle.position()
		(0.00,-22.00)
		>>> turtle.heading()
		100.0
		>>> turtle.reset()
		>>> turtle.position()
		(0.00,0.00)
		>>> turtle.heading()
		0.0
		"""
		self._pos = ui.Point(0, 0)
		self._current_color = (0, 0, 0, 1)
		self._current_fill_color = (0, 0, 0, 1)
		self._line_width = 1.0
		self._angle = 0.0
		self._turtle_visible = True
		self.is_down = True
		self.fill_path = None
		self.batched_drawings = []
		self.colormode(255)
		self.update_view(make_visible=False)
	
	def clone(self):
		"""Create and return a clone of the turtle.

		No argument.

		Create and return a clone of the turtle with same position, heading
		and turtle properties.

		Example (for a Turtle instance named mick):
		mick = Turtle()
		joe = mick.clone()
		"""
		p = Pen()
		p._pos = self._pos
		p._angle = self._angle
		p._current_color = self._current_color
		p._current_fill_color = self._current_fill_color
		p._turtle_visible = self._turtle_visible
		p._line_width = self._line_width
		return p
	
	def speed(self, speed_value=None):
		""" Return or set the turtle's speed.

		Optional argument:
		speed -- an integer in the range 0..10 or a speedstring (see below)

		Set the turtle's speed to an integer value in the range 0 .. 10.
		If no argument is given: return current speed.

		If input is a number greater than 10 or smaller than 0.5,
		speed is set to 0.
		Speedstrings  are mapped to speedvalues in the following way:
		    'fastest' :  0
		    'fast'    :  10
		    'normal'  :  6
		    'slow'    :  3
		    'slowest' :  1
		speeds from 1 to 10 enforce increasingly faster animation of
		line drawing and turtle turning.

		Attention:
		speed = 0 : *no* animation takes place. forward/back makes turtle jump
		and likewise left/right make the turtle turn instantly.

		Example (for a Turtle instance named turtle):
		>>> turtle.speed(3)
		"""
		# TODO: The mapping is incorrect, fastest is 10 here, but should be 0.
		if speed_value is not None:
			speed_delays = {'fastest': 0.0 , 'fast': 0.01, 'normal': 0.03, 'slow': 0.05, 'slowest': 0.1}
			if isinstance(speed_value, basestring):	
				self.delay_sec = speed_delays.get(speed_value, 0.03)
			elif isinstance(speed_value, int):
				self.delay_sec = 0.0 if (speed_value >= 10 or speed_value <= 0) else (10 - speed_value) / 100.0   
		return 10 if self.delay_sec == 0 else min(10, max(0, (1.0/self.delay_sec)/10 - 1))
	
	def delay(self, ms):
		""" Return or set the drawing delay in milliseconds.

		Optional argument:
		delay -- positive integer

		Example (for a TurtleScreen instance named screen):
		>>> screen.delay(15)
		>>> screen.delay()
		15
		"""
		self.delay_sec = min(1.0, ms / 100.0)
		return self.delay_sec * 100.0
		
	def _draw_line(self, from_pos, to_pos, color, line_width):
		line_path = ui.Path()
		line_path.move_to(*from_pos)
		line_path.line_to(*to_pos)
		line_path.line_width = line_width
		line_path.line_cap_style = ui.LINE_CAP_ROUND
		line_path.line_join_style = ui.LINE_JOIN_ROUND
		ui.set_color(color)
		line_path.stroke()
	
	def _forward(self, d):
		self._sleep()
		new_pos = self._pos + (cos(self._angle) * d, sin(self._angle) * d)
		if self.fill_path:
			self.fill_path.line_to(*new_pos)
		if self.is_down:
			from_pos = self._pos
			line_width = self._line_width
			color = self._current_color
			def _draw():
				self._draw_line(from_pos, new_pos, color, line_width)
			self._add_drawing(_draw)
		self._pos = new_pos
		self.update_view()
	
	def forward(self, d):
		"""Move the turtle forward by the specified distance.

		Aliases: forward | fd

		Argument:
		distance -- a number (integer or float)

		Move the turtle forward by the specified distance, in the direction
		the turtle is headed.

		Example (for a Turtle instance named turtle):
		>>> turtle.position()
		(0.00, 0.00)
		>>> turtle.forward(25)
		>>> turtle.position()
		(25.00,0.00)
		>>> turtle.forward(-75)
		>>> turtle.position()
		(-50.00,0.00)
		"""
		for i in range(self.anim_steps):
			self._forward(float(d)/self.anim_steps)
	
	fd = forward
		
	def backward(self, d):
		"""Move the turtle backward by distance.

		Aliases: back | backward | bk

		Argument:
		distance -- a number

		Move the turtle backward by distance ,opposite to the direction the
		turtle is headed. Do not change the turtle's heading.

		Example (for a Turtle instance named turtle):
		>>> turtle.position()
		(0.00, 0.00)
		>>> turtle.backward(30)
		>>> turtle.position()
		(-30.00, 0.00)
		"""
		self.forward(-d)
	
	back = backward
	bk = backward
	
	def _left(self, angle):
		self._sleep()
		self._angle -= self._angle_to_rad(angle)
		self.update_view()
	
	def left(self, angle):
		"""Turn turtle left by angle units.

		Aliases: left | lt

		Argument:
		angle -- a number (integer or float)

		Turn turtle left by angle units. (Units are by default degrees,
		but can be set via the degrees() and radians() functions.)
		Angle orientation depends on mode. (See this.)

		Example (for a Turtle instance named turtle):
		>>> turtle.heading()
		22.0
		>>> turtle.left(45)
		>>> turtle.heading()
		67.0
		"""
		for i in range(self.anim_steps):
			self._left(float(angle)/self.anim_steps)
	
	lt = left
		
	def right(self, angle):
		"""Turn turtle right by angle units.

		Aliases: right | rt

		Argument:
		angle -- a number (integer or float)

		Turn turtle right by angle units. (Units are by default degrees,
		but can be set via the degrees() and radians() functions.)
		Angle orientation depends on mode. (See this.)

		Example (for a Turtle instance named turtle):
		>>> turtle.heading()
		22.0
		>>> turtle.right(45)
		>>> turtle.heading()
		337.0
		"""
		self.left(-angle)
	
	rt = right
	
	def begin_fill(self):
		"""Called just before drawing a shape to be filled.

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.color("black", "red")
		>>> turtle.begin_fill()
		>>> turtle.circle(60)
		>>> turtle.end_fill()
		"""
		if self.fill_path:
			self.end_fill()
		self.fill_path = ui.Path()
		self.fill_path.move_to(*self._pos)
	
	def end_fill(self):
		"""Fill the shape drawn after the call begin_fill().

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.color("black", "red")
		>>> turtle.begin_fill()
		>>> turtle.circle(60)
		>>> turtle.end_fill()
		"""
		if not self.fill_path:
			return
		fill_path = self.fill_path
		fill_color = self._current_fill_color
		def _draw():
			ui.set_color(fill_color)
			fill_path.fill()
		self._add_drawing(_draw)
		self.fill_path = None
		self.update_view()
	
	def fill(self, flag):
		if bool(flag):
			self.begin_fill()
		else:
			self.end_fill()
	
	def filling(self):
		"""Return fillstate (True if filling, False else).

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.begin_fill()
		>>> if turtle.filling():
		...     turtle.pensize(5)
		... else:
		...     turtle.pensize(3)
		"""
		return self.fill_path is not None
	
	def color(self, *args):
		"""Return or set the pencolor and fillcolor.

		Arguments:
		Several input formats are allowed.
		They use 0, 1, 2, or 3 arguments as follows:

		color()
		    Return the current pencolor and the current fillcolor
		    as a pair of color specification strings as are returned
		    by pencolor and fillcolor.
		color(colorstring), color((r,g,b)), color(r,g,b)
		    inputs as in pencolor, set both, fillcolor and pencolor,
		    to the given value.
		color(colorstring1, colorstring2),
		color((r1,g1,b1), (r2,g2,b2))
		    equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
		    and analogously, if the other input format is used.

		If turtleshape is a polygon, outline and interior of that polygon
		is drawn with the newly set colors.
		For mor info see: pencolor, fillcolor

		Example (for a Turtle instance named turtle):
		>>> turtle.color('red', 'green')
		>>> turtle.color()
		('red', 'green')
		>>> colormode(255)
		>>> color((40, 80, 120), (160, 200, 240))
		>>> color()
		('#285078', '#a0c8f0')
		"""
		if len(args) == 1 or len(args) >= 3:
			self.fillcolor(*args)
			self.pencolor(*args)
		elif len(args) == 2:
			self.pencolor(args[0])
			self.fillcolor(args[1])
		return self.pencolor(), self.fillcolor()

	def pencolor(self, *args):
		""" Return or set the pencolor.

		Arguments:
		Four input formats are allowed:
		  - pencolor()
		    Return the current pencolor as color specification string,
		    possibly in hex-number format (see example).
		    May be used as input to another color/pencolor/fillcolor call.
		  - pencolor(colorstring)
		    s is a Tk color specification string, such as "red" or "yellow"
		  - pencolor((r, g, b))
		    *a tuple* of r, g, and b, which represent, an RGB color,
		    and each of r, g, and b are in the range 0..colormode,
		    where colormode is either 1.0 or 255
		  - pencolor(r, g, b)
		    r, g, and b represent an RGB color, and each of r, g, and b
		    are in the range 0..colormode

		If turtleshape is a polygon, the outline of that polygon is drawn
		with the newly set pencolor.

		Example (for a Turtle instance named turtle):
		>>> turtle.pencolor('brown')
		>>> tup = (0.2, 0.8, 0.55)
		>>> turtle.pencolor(tup)
		>>> turtle.pencolor()
		'#33cc8c'
		"""
		if args:
			r, g, b, a = self._color_args_to_rgba(args)
			self._current_color = (r, g, b, a)
		return self._current_color
	
	def fillcolor(self, *args):
		""" Return or set the fillcolor.

		Arguments:
		Four input formats are allowed:
		  - fillcolor()
		    Return the current fillcolor as color specification string,
		    possibly in hex-number format (see example).
		    May be used as input to another color/pencolor/fillcolor call.
		  - fillcolor(colorstring)
		    s is a Tk color specification string, such as "red" or "yellow"
		  - fillcolor((r, g, b))
		    *a tuple* of r, g, and b, which represent, an RGB color,
		    and each of r, g, and b are in the range 0..colormode,
		    where colormode is either 1.0 or 255
		  - fillcolor(r, g, b)
		    r, g, and b represent an RGB color, and each of r, g, and b
		    are in the range 0..colormode

		If turtleshape is a polygon, the interior of that polygon is drawn
		with the newly set fillcolor.

		Example (for a Turtle instance named turtle):
		>>> turtle.fillcolor('violet')
		>>> col = turtle.pencolor()
		>>> turtle.fillcolor(col)
		>>> turtle.fillcolor(0, .5, 0)
		"""
		if args:
			r, g, b, a = self._color_args_to_rgba(args)
			self._current_fill_color = (r, g, b, a)
		return self._current_fill_color
	
	
	def width(self, w=None):
		"""Set or return the line thickness.

		Aliases:  pensize | width

		Argument:
		width -- positive number

		Set the line thickness to width or return it. If resizemode is set
		to "auto" and turtleshape is a polygon, that polygon is drawn with
		the same line thickness. If no argument is given, current pensize
		is returned.

		Example (for a Turtle instance named turtle):
		>>> turtle.pensize()
		1
		>>> turtle.pensize(10)   # from here on lines of width 10 are drawn
		"""
		if w is not None:
			self._line_width = w
		return self._line_width
	
	pensize = width
	
	def down(self):
		"""Pull the pen down -- drawing when moving.

		Aliases: pendown | pd | down

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.pendown()
		"""
		self.is_down = True
	
	pendown = down
	pd = down

	def up(self):
		"""Pull the pen up -- no drawing when moving.

		Aliases: penup | pu | up

		No argument

		Example (for a Turtle instance named turtle):
		>>> turtle.penup()
		"""
		self.is_down = False
		
	penup = up
	pu = up

	def isdown(self):
		"""Return True if pen is down, False if it's up.

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.penup()
		>>> turtle.isdown()
		False
		>>> turtle.pendown()
		>>> turtle.isdown()
		True
		"""
		return self.is_down
	
	def clear(self):
		"""Delete the turtle's drawings from the screen. Do not move turtle.

		No arguments.

		Delete the turtle's drawings from the screen. Do not move turtle.
		State and position of the turtle as well as drawings of other
		turtles are not affected.

		Examples (for a Turtle instance named turtle):
		>>> turtle.clear()
		"""
		self.fill_path = None
		global _canvas_image
		_canvas_image = None
		self.update_view()
	
	def write(self, text, move=False, align=None, font=None):
		"""Write text at the current turtle position.

		Arguments:
		arg -- info, which is to be written to the TurtleScreen
		move (optional) -- True/False
		align (optional) -- one of the strings "left", "center" or right"
		font (optional) -- a triple (fontname, fontsize, fonttype)

		Write text - the string representation of arg - at the current
		turtle position according to align ("left", "center" or right")
		and with the given font.
		If move is True, the pen is moved to the bottom-right corner
		of the text. By default, move is False.

		Example (for a Turtle instance named turtle):
		>>> turtle.write('Home = ', True, align="center")
		>>> turtle.write((0,0), True)
		"""
		# TODO: Implement `align` and `font` parameters
		text = str(text)
		w, h = ui.measure_string(text)
		color = self._current_color
		pos = self._pos
		def _draw():
			ui.set_color(color)
			ui.draw_string(text, (pos.x, pos.y - h, 0, 0))
		self._add_drawing(_draw)
		if move:
			self._pos += (w, 0)
		self.update_view()
	
	def circle(self, radius, extent=None, steps=None):
		""" Draw a circle with given radius.

		Arguments:
		radius -- a number
		extent (optional) -- a number
		steps (optional) -- an integer

		Draw a circle with given radius. The center is radius units left
		of the turtle; extent - an angle - determines which part of the
		circle is drawn. If extent is not given, draw the entire circle.
		If extent is not a full circle, one endpoint of the arc is the
		current pen position. Draw the arc in counterclockwise direction
		if radius is positive, otherwise in clockwise direction. Finally
		the direction of the turtle is changed by the amount of extent.

		As the circle is approximated by an inscribed regular polygon,
		steps determines the number of steps to use. If not given,
		it will be calculated automatically. Maybe used to draw regular
		polygons.

		call: circle(radius)                  # full circle
		--or: circle(radius, extent)          # arc
		--or: circle(radius, extent, steps)
		--or: circle(radius, steps=6)         # 6-sided polygon

		Example (for a Turtle instance named turtle):
		>>> turtle.circle(50)
		>>> turtle.circle(120, 180)  # semicircle
		"""
		if extent is None:
			extent = math.radians(360)
		else:
			extent = math.radians(extent) if not self._use_rad else extent
		frac = abs(extent) / math.radians(360)
		if steps is None or steps == 0:
			steps = 1 + int(min(11 + abs(radius)/6.0, 59.0) * frac)
		elif not isinstance(steps, int):
			raise TypeError('steps must be an integer')
		w = 1.0 * extent / steps
		w2 = 0.5 * w
		l = 2.0 * radius * sin(w2)
		if radius < 0:
			l, w, w2 = -l, -w, -w2
		if not self._use_rad:
			w, w2 = math.degrees(w), math.degrees(w2)
		self._left(w2)
		for i in range(steps):
			self._forward(l)
			self._left(w)
		self._left(-w2)
	
	def dot(self, size=None, *color):
		"""Draw a dot with diameter size, using color.

		Optional arguments:
		size -- an integer >= 1 (if given)
		color -- a colorstring or a numeric color tuple

		Draw a circular dot with diameter size, using color.
		If size is not given, the maximum of pensize+4 and 2*pensize is used.

		Example (for a Turtle instance named turtle):
		>>> turtle.dot()
		>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
		"""
		if size is None:
			size = max(self._line_width + 4, self._line_width * 2)
		if not isinstance(size, numbers.Number):
			raise TypeError('size must be a number or None')
		pos = self.pos()
		current_color = self._current_color
		def draw_dot():
			dot_path = ui.Path.oval(pos[0] - size*0.5, -pos[1] - size*0.5, size, size)
			if color:
				rgba = self._color_args_to_rgba(color)
				ui.set_color(rgba)
			else:
				ui.set_color(current_color)
			dot_path.fill()
		self._add_drawing(draw_dot)
	
	def stamp():
		# Not implemented
		return 0
	
	def clearstamp(self, stampid):
		# Not implemented
		pass
	
	def clearstamps(self, n=None):
		# Not implemented
		pass
	
	def undo(self):
		#---todo: keep buffer of n previous images for undoing?
		pass
	
	def goto(self, x, y=None):
		"""Move turtle to an absolute position.

		Aliases: setpos | setposition | goto:

		Arguments:
		x -- a number      or     a pair/vector of numbers
		y -- a number             None

		call: goto(x, y)         # two coordinates
		--or: goto((x, y))       # a pair (tuple) of coordinates
		--or: goto(vec)          # e.g. as returned by pos()

		Move turtle to an absolute position. If the pen is down,
		a line will be drawn. The turtle's orientation does not change.

		Example (for a Turtle instance named turtle):
		>>> tp = turtle.pos()
		>>> tp
		(0.00, 0.00)
		>>> turtle.setpos(60,30)
		>>> turtle.pos()
		(60.00,30.00)
		>>> turtle.setpos((20,80))
		>>> turtle.pos()
		(20.00,80.00)
		>>> turtle.setpos(tp)
		>>> turtle.pos()
		(0.00,0.00)
		"""
		if y is None:
			return self.goto(*x)
		self._sleep()
		if self.fill_path:
			self.fill_path.line_to(x, -y)
		if self.is_down:
			pos = self._pos
			color = self._current_color
			line_width = self._line_width
			def _draw():
				self._draw_line(pos, (x, -y), color, line_width)
			self._add_drawing(_draw)
		self._pos = ui.Point(x, -y)
		self.update_view()
	
	setpos = goto
	setposition = goto
	
	def home(self):
		"""Move turtle to the origin - coordinates (0,0).

		No arguments.

		Move turtle to the origin - coordinates (0,0) and set its
		heading to its start-orientation (which depends on mode).

		Example (for a Turtle instance named turtle):
		>>> turtle.home()
		"""
		self.goto(0, 0)
	
	def towards(self, *args):
		"""Return the angle of the line from the turtle's position to (x, y).

		Arguments:
		x -- a number   or  a pair/vector of numbers   or   a turtle instance
		y -- a number       None                            None

		call: distance(x, y)         # two coordinates
		--or: distance((x, y))       # a pair (tuple) of coordinates
		--or: distance(vec)          # e.g. as returned by pos()
		--or: distance(mypen)        # where mypen is another turtle

		Return the angle, between the line from turtle-position to position
		specified by x, y and the turtle's start orientation. (Depends on
		modes - "standard" or "logo")

		Example (for a Turtle instance named turtle):
		>>> turtle.pos()
		(10.00, 10.00)
		>>> turtle.towards(0,0)
		225.0
		"""
		if len(args) == 1:
			args = args[0]
		if isinstance(args, Pen):
			x, y = args._pos
		elif len(args) == 2:
			x, y = args
		else:
			raise TypeError('Expected x, y or Pen object')
		dx, dy = x - self._pos.x, y - self._pos.y
		a = math.atan2(dy, dx)
		if not self._use_rad:
			a = math.degrees(a)
		return a
	
	def heading(self):
		""" Return the turtle's current heading.

		No arguments.

		Example (for a Turtle instance named turtle):
		>>> turtle.left(67)
		>>> turtle.heading()
		67.0
		"""
		if self._use_rad:
			return self._angle
		return math.degrees(self._angle)
	
	def setheading(self, angle):
		"""Set the orientation of the turtle to to_angle.

		Aliases:  setheading | seth

		Argument:
		to_angle -- a number (integer or float)

		Set the orientation of the turtle to to_angle.
		Here are some common directions in degrees:

		 standard - mode:          logo-mode:
		-------------------|--------------------
		   0 - east                0 - north
		  90 - north              90 - east
		 180 - west              180 - south
		 270 - south             270 - west

		Example (for a Turtle instance named turtle):
		>>> turtle.setheading(90)
		>>> turtle.heading()
		90
		"""
		self._sleep()
		a = self._angle_to_rad(angle)
		if self.mode() == 'standard': # note: other modes are not implemented atm
			a += math.pi
		self._angle = a
		self.update_view()
	
	seth = setheading
	
	def position(self):
		"""Return the turtle's current location (x,y), as a Vec2D-vector.

		Aliases: pos | position

		No arguments.

		Example (for a Turtle instance named turtle):
		>>> turtle.pos()
		(0.00, 240.00)
		"""
		return Vec2D(self._pos[0], -self._pos[1])
	
	pos = position
	
	def xcor(self):
		""" Return the turtle's x coordinate.

		No arguments.

		Example (for a Turtle instance named turtle):
		>>> reset()
		>>> turtle.left(60)
		>>> turtle.forward(100)
		>>> print turtle.xcor()
		50.0
		"""
		return self._pos.x
	
	def ycor(self):
		""" Return the turtle's y coordinate
		---
		No arguments.

		Example (for a Turtle instance named turtle):
		>>> reset()
		>>> turtle.left(60)
		>>> turtle.forward(100)
		>>> print turtle.ycor()
		86.6025403784
		"""
		return -self._pos.y
	
	def distance(self, x, y=None):
		"""Return the distance from the turtle to (x,y) in turtle step units.

		Arguments:
		x -- a number   or  a pair/vector of numbers   or   a turtle instance
		y -- a number       None                            None

		call: distance(x, y)         # two coordinates
		--or: distance((x, y))       # a pair (tuple) of coordinates
		--or: distance(vec)          # e.g. as returned by pos()
		--or: distance(mypen)        # where mypen is another turtle

		Example (for a Turtle instance named turtle):
		>>> turtle.pos()
		(0.00, 0.00)
		>>> turtle.distance(30,40)
		50.0
		>>> pen = Turtle()
		>>> pen.forward(77)
		>>> turtle.distance(pen)
		77.0
		"""
		if y is None:
			x, y = x
		return abs(self._pos - (x, y))
	
	def setx(self, x):
		"""Set the turtle's first coordinate to x

		Argument:
		x -- a number (integer or float)

		Set the turtle's first coordinate to x, leave second coordinate
		unchanged.

		Example (for a Turtle instance named turtle):
		>>> turtle.position()
		(0.00, 240.00)
		>>> turtle.setx(10)
		>>> turtle.position()
		(10.00, 240.00)
		"""
		self._sleep()
		self._pos = ui.Point(x, self._pos.y)
		self.update_view()
	
	def sety(self, y):
		"""Set the turtle's second coordinate to y

		Argument:
		y -- a number (integer or float)

		Set the turtle's first coordinate to x, second coordinate remains
		unchanged.

		Example (for a Turtle instance named turtle):
		>>> turtle.position()
		(0.00, 40.00)
		>>> turtle.sety(-10)
		>>> turtle.position()
		(0.00, -10.00)
		"""
		self._sleep()
		self._pos = ui.Point(self._pos.x, -y)
		self.update_view()
	
	def pen(self, pen=None, **pendict):
		"""Return or set the pen's attributes.
		
		NOTE: resizemode, stretchfactor, outline, tilt are not supported in Pythonista
		
		Arguments:
		    pen -- a dictionary with some or all of the below listed keys.
		    **pendict -- one or more keyword-arguments with the below
		                 listed keys as keywords.

		Return or set the pen's attributes in a 'pen-dictionary'
		with the following key/value pairs:
		   "shown"      :   True/False
		   "pendown"    :   True/False
		   "pencolor"   :   color-string or color-tuple
		   "fillcolor"  :   color-string or color-tuple
		   "pensize"    :   positive number
		   "speed"      :   number in range 0..10
		   "resizemode" :   "auto" or "user" or "noresize"
		   "stretchfactor": (positive number, positive number)
		   "shearfactor":   number
		   "outline"    :   positive number
		   "tilt"       :   number

		This dictionary can be used as argument for a subsequent
		pen()-call to restore the former pen-state. Moreover one
		or more of these attributes can be provided as keyword-arguments.
		This can be used to set several pen attributes in one statement.


		Examples (for a Turtle instance named turtle):
		>>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
		>>> turtle.pen()
		{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
		'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
		'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
		>>> penstate=turtle.pen()
		>>> turtle.color("yellow","")
		>>> turtle.penup()
		>>> turtle.pen()
		{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
		'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
		'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
		>>> p.pen(penstate, fillcolor="green")
		>>> p.pen()
		{'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
		'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
		'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
		"""
		current_pen_info = {'shown': self.isvisible(),
							'pendown': self.isdown(),
							'pencolor': self._current_color,
							'fillcolor': self._current_fill_color,
							'pensize': self._line_width,
							'speed': 10 if self.delay_sec == 0 else min(10, max(0, (1.0/self.delay_sec)/10 - 1))
		}
		if pen is None:
			pen = {}
		pen.update(pendict)
		if 'shown' in pen:
			self.showturtle() if pen['shown'] else self.hideturtle()
		if 'pendown' in pen:
			self.pendown() if pen['pendown'] else self.penup()
		if 'pencolor' in pen:
			self.pencolor(pen['pencolor'])
		if fillcolor in pen:
			self.fillcolor(pen['fillcolor'])
		if 'pensize' in pen:
			self.width(pen['pensize'])
		if 'speed' in pen:
			self.speed(pen['speed'])
		return current_pen_info

	def showturtle(self):
		"""Makes the turtle visible.

		Aliases: showturtle | st

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.hideturtle()
		>>> turtle.showturtle()
		"""
		self._turtle_visible = True
		self.update_view()
	
	st = showturtle
	
	def hideturtle(self):
		"""Makes the turtle invisible.

		Aliases: hideturtle | ht

		No argument.

		It's a good idea to do this while you're in the
		middle of a complicated drawing, because hiding
		the turtle speeds up the drawing observably.

		Example (for a Turtle instance named turtle):
		>>> turtle.hideturtle()
		"""
		self._turtle_visible = False
		self.update_view()
	
	ht = hideturtle
	
	def isvisible(self):
		"""Return True if the Turtle is shown, False if it's hidden.

		No argument.

		Example (for a Turtle instance named turtle):
		>>> turtle.hideturtle()
		>>> print turtle.isvisible():
		False
		"""
		return self._turtle_visible
	
	def getscreen(self):
		return _main_view
	
	def getturtle(self):
		return self
	
	def getpen(self):
		return self
	
	def setundobuffer(self, buffer_size):
		# Not implemented
		pass
	
	def undobufferentries(self):
		# Not implemented
		return 0
	
	def mode(self, mode=None):
		#--- todo?
		return 'standard'
	
	def colormode(self, cmode=None):
		if cmode == 1.0 or cmode == 255:
			self._colormode = cmode
			global _default_color_mode
			_default_color_mode = cmode
		return self._colormode
	
	def update_view(self, make_visible=True):
		if len(self.batched_drawings) > 0:
			return
		_pen_view.set_needs_display(make_visible=make_visible)


class Turtle (Pen):
	pass


def done():
	pass

mainloop = done

def Screen():
	return _main_view

def textinput(title, prompt):
	import dialogs
	try:
		return dialogs.input_alert(title, prompt, '', 'OK')
	except KeyboardInterrupt:
		return None

def numinput(title, prompt, default=None, minval=None, maxval=None):
	import dialogs
	default_text = str(default) if default is not None else ''
	result = None
	while result is None:
		entered_text = dialogs.input_alert(title, prompt, default_text, 'OK')
		try:
			result = float(entered_text)
			if minval is not None and result < minval:
				prompt = 'The number you entered is too small.'
				result = None
			elif maxval is not None and result > maxval:
				prompt = 'The number you entered is too big.'
				result = None
		except ValueError:
			prompt = 'Please enter a number!'
	return result


_main_view = TurtleView()
_default_pen = Pen()

# Move and draw
forward = _default_pen.forward
fd = forward
backward = _default_pen.backward
back = backward
bk = backward
left = _default_pen.left
lt = left
right = _default_pen.right
rt = right
goto = _default_pen.goto
setpos = goto
setposition = goto
setx = _default_pen.setx
sety = _default_pen.sety
setheading = _default_pen.setheading
seth = setheading
home = _default_pen.home
circle = _default_pen.circle
dot = _default_pen.dot
stamp = _default_pen.stamp
clearstamp = _default_pen.clearstamp
clearstamps = _default_pen.clearstamps
undo = _default_pen.undo
speed = _default_pen.speed

# Tell Turtle's state
position = _default_pen.position
pos = position
towards = _default_pen.towards
xcor = _default_pen.xcor
ycor = _default_pen.ycor
heading = _default_pen.heading
distance = _default_pen.distance

# Setting and measurement
degrees = _default_pen.degrees
radians = _default_pen.radians

# Pen control

# Drawing state
down = _default_pen.down
pendown = down
pd = down
up = _default_pen.up
penup = up
pu = up
width = _default_pen.width
pensize = width
isdown = _default_pen.isdown
pen = _default_pen.pen

# Color control
color = _default_pen.color
pencolor = _default_pen.pencolor
fillcolor = _default_pen.fillcolor

# Filling
fill = _default_pen.fill
begin_fill = _default_pen.begin_fill
end_fill = _default_pen.end_fill

# More drawing control
reset = _main_view.reset
clear = _default_pen.clear
write = _default_pen.write

# Turtle state

# Visibility
showturtle = _default_pen.showturtle
st = showturtle
hideturtle = _default_pen.hideturtle
ht = hideturtle
isvisible = _default_pen.isvisible

# Appearance
'''
todo:
shape()
resizemode()
shapesize() | turtlesize()
settiltangle()
tiltangle()
tilt()
'''

# Special Turtle methods
getturtle = _default_pen.getturtle
getpen = getturtle
getscreen = _default_pen.getscreen
setundobuffer = _default_pen.setundobuffer
undobufferentries = _default_pen.undobufferentries
'''
todo:
begin_poly()
end_poly()
get_poly()
window_width()
window_height()
'''

clone = _default_pen.clone

filling = _default_pen.filling

tracer = _main_view.tracer

delay = _default_pen.delay

title = _main_view.title
setup = _main_view.setup

mode = _default_pen.mode
colormode = _default_pen.colormode

bgcolor = _main_view.bgcolor
clearscreen = _main_view.clearscreen


def _flush_all_pens():
	for p in _all_pens:
		p._force_flush()
	if appex.is_shortcut() and _canvas_image:
		import shortcuts
		shortcuts.set_output_image(_canvas_image)
		_canvas_image.show()

import _pykit_atexit
_pykit_atexit.register('turtle', _flush_all_pens)
