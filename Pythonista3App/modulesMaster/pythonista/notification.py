#import 'pythonista'

from objc_util import ObjCClass, ObjCInstance, ObjCBlock, NSSet, load_framework, nsurl, c_void_p

try:
	load_framework('UserNotifications')
	UNUserNotificationCenter = ObjCClass('UNUserNotificationCenter')
except:
	raise NotImplementedError('The notification module requires iOS 10 or later.')

import _notification
import sys
import uuid
import os
import json
import hashlib
from numbers import Number
import shutil
import tempfile
from _pythonista import make_url as pythonista_url

UNNotificationRequest = ObjCClass('UNNotificationRequest')
UNMutableNotificationContent = ObjCClass('UNMutableNotificationContent')
UNTimeIntervalNotificationTrigger = ObjCClass('UNTimeIntervalNotificationTrigger')
UNCalendarNotificationTrigger = ObjCClass('UNCalendarNotificationTrigger')
UNLocationNotificationTrigger = ObjCClass('UNLocationNotificationTrigger')
CLCircularRegion = ObjCClass('CLCircularRegion')
UNNotificationCategory = ObjCClass('UNNotificationCategory')
UNNotificationAction = ObjCClass('UNNotificationAction')
UNTextInputNotificationAction = ObjCClass('UNTextInputNotificationAction')
UNNotificationSound = ObjCClass('UNNotificationSound')
UNNotificationAttachment = ObjCClass('UNNotificationAttachment')

CENTER = UNUserNotificationCenter.currentNotificationCenter()

if sys.version_info[0] >= 3:
	basestring = str


def _load_notification_categories():
	file_path = os.path.expanduser('~/notification_categories.json')
	try:
		with open(file_path, 'r') as f:
			category_infos = json.load(f)
	except:
		category_infos = {}
	return category_infos


def _save_notification_categories(category_infos):
	file_path = os.path.expanduser('~/notification_categories.json')
	with open(file_path, 'w') as f:
		json.dump(category_infos, f, indent=2)


def _clear_notification_categories():
	file_path = os.path.expanduser('~/notification_categories.json')
	with open(file_path, 'w') as f:
		json.dump({}, f)


def _get_soundlib_path():
	# NOTE: All notification sounds have to be copied here, for the notification process to find them...
	fm = ObjCClass('NSFileManager').defaultManager()
	NSLibraryDirectory = 5
	NSUserDomain = 1
	library_dir_url = fm.URLForDirectory_inDomain_appropriateForURL_create_error_(NSLibraryDirectory, NSUserDomain, None, True, None)
	library_path = str(library_dir_url.path())
	p = os.path.join(library_path, 'Sounds')
	if not os.path.exists(p):
		os.makedirs(p)
	return p


def cancel_all():
	CENTER.removeAllPendingNotificationRequests()
	_clear_notification_categories()


def cancel(identifier):
	if not isinstance(identifier, basestring):
		raise TypeError('identifier must be a string')
	CENTER.removePendingNotificationRequestsWithIdentifiers_([identifier])


def remove_delivered(identifier):
	if not isinstance(identifier, basestring):
		raise TypeError('identifier must be a string')
	CENTER.removeDeliveredNotificationsWithIdentifiers_([identifier])


def remove_all_delivered():
	CENTER.removeAllDeliveredNotifications()


def get_scheduled():
	return _notification.get_scheduled()


def _date_comps_from_trigger(trigger):
	calendar_keys = ['year', 'quarter', 'month', 'day', 'weekday', 'weekday_ordinal', 'week_of_month', 'week_of_year', 'hour', 'minute', 'second']
	if not any(trigger.get(k) for k in calendar_keys):
		# There are no calendar-related keys in the trigger
		return None
	if any(not isinstance(trigger.get(k, 0), Number) for k in calendar_keys):
		raise ValueError('All date components must be numbers')
	date_comps = ObjCClass('NSDateComponents').new().autorelease()
	prop_names = {'weekday_ordinal': 'weekdayOrdinal', 'week_of_month': 'weekOfMonth', 'week_of_year': 'weekOfYear'}
	for key in calendar_keys:
		value = trigger.get(key, None)
		if value is not None:
			objc_prop_name = prop_names.get(key, key)
			setattr(date_comps, objc_prop_name, value)
	return date_comps


def _parse_actions(actions, user_info, actions_id):
	if actions is not None:
		for i, a in enumerate(actions):
			button_id = str(i)
			button_action_url = a.get('action_url', a.get('url', None))
			if button_action_url:
				user_info['buttonActions'][button_id] = button_action_url
		existing_categories = _load_notification_categories()
		if actions_id is not None:
			category_id = actions_id
		else:
			category_id = hashlib.md5(repr(actions).encode('utf-8')).hexdigest()
		if not existing_categories.get(category_id) or actions_id is not None:
			existing_categories[category_id] = actions
			un_categories = []
			for key, cat_actions in existing_categories.items():
				un_actions_for_cat = []
				for i, a in enumerate(cat_actions):
					button_title = a.get('title', ' ')
					button_id = str(i)
					action_url = a.get('action_url', a.get('url', None))
					action_options = 0
					# NOTE: pythonista URLs are normally executed in the background for button actions, but that's not always desirable, so it's possible to override this behavior by setting a 'foreground' option.
					force_foreground = a.get('foreground', False)
					if action_url and not force_foreground:
						if not action_url.startswith('pythonista:') and not action_url.startswith('pythonista3:'):
							force_foreground = True
							# Not a pythonista URL, always require foreground execution
							force_foreground = True
					if force_foreground:
						action_options |= (1 << 2)
						# NOTE: Background execution as the default makes sense for button actions because tapping the notification itself always results in foreground execution, and should typically be used if any further interaction is required.
					destructive = a.get('destructive', False)
					if destructive:
						action_options |= (1 << 1)
					if a.get('text_input'):
						input_button_title = a.get('text_input_button_title', 'OK')
						input_placeholder = a.get('text_input_placeholder')
						un_action = UNTextInputNotificationAction.actionWithIdentifier_title_options_textInputButtonTitle_textInputPlaceholder_(
							button_id, button_title, action_options, input_button_title, input_placeholder)
					else:
						un_action = UNNotificationAction.actionWithIdentifier_title_options_(button_id, button_title, action_options)
					un_actions_for_cat.append(un_action)
				category = UNNotificationCategory.categoryWithIdentifier_actions_intentIdentifiers_options_(key, un_actions_for_cat, [], 0)
				un_categories.append(category)
			CENTER.setNotificationCategories_(NSSet.setWithArray_(un_categories))
			# Update the json cache of registered notification categories:
			_save_notification_categories(existing_categories)
		return category_id


def _process_attachments(attachments):
	if attachments is None:
		return []
	un_attachments = []
	for attachment in attachments:
		if type(attachment).__name__ == 'Image':
			import ui
			if isinstance(attachment, ui.Image):
				jpeg_data = attachment.to_jpeg()
				img_filename = uuid.uuid4().hex + '.jpg'
				img_path = os.path.join(tempfile.gettempdir(), img_filename)
				with open(img_path, 'wb') as f:
					f.write(jpeg_data)
				attachment = img_path
		if not isinstance(attachment, basestring):
			raise TypeError('Attachments must be strings (file paths)')
		try:
			file_ext = os.path.splitext(attachment)[1]
			filename = uuid.uuid4().hex + file_ext
			temp_file_path = os.path.join(tempfile.gettempdir(), filename)
			shutil.copyfile(attachment, temp_file_path)
			attachment_url = nsurl(temp_file_path)
			un_att = UNNotificationAttachment.attachmentWithIdentifier_URL_options_error_('', attachment_url, {}, None)
			if un_att:
				un_attachments.append(un_att)
			else:
				raise ValueError('Could not create attachment from file')
		except Exception as e:
			raise ValueError('Invalid attachment or unreadable file: %s' % (attachment,))
	return un_attachments


def _parse_location_trigger(trigger):
	latitude = trigger.get('latitude', None)
	longitude = trigger.get('longitude', None)
	radius = trigger.get('radius', 100)
	if latitude is None or longitude is None:
		return None
	center = (latitude, longitude)
	region_id = uuid.uuid4().hex
	region = CLCircularRegion.alloc().initWithCenter_radius_identifier_(center, radius, region_id).autorelease()
	region.setNotifyOnEntry_(trigger.get('entry', True))
	region.setNotifyOnExit_(trigger.get('exit', True))
	un_trigger = UNLocationNotificationTrigger.triggerWithRegion_repeats_(region, trigger.get('repeats', False))
	if un_trigger:
		import location
		if not location.is_authorized():
			# We don't really need the location here, but this implicitly requests location access, which is needed for location-based notifications to work.
			location.get_location()
	return un_trigger


def _parse_trigger(trigger, delay):
	un_trigger = None
	if trigger is not None:
		if trigger is not None:
			delay = trigger.get('delay', delay)
			# NOTE: The 'repeats' option is valid for all trigger types.
			repeats = bool(trigger.get('repeats', False))
			if delay > 0:
				if repeats and delay < 60:
					raise ValueError('delay must be >=60s for repeating notifications')
				un_trigger = UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_(delay, repeats)
			date_comps = _date_comps_from_trigger(trigger)
			if date_comps:
				un_trigger = UNCalendarNotificationTrigger.triggerWithDateMatchingComponents_repeats_(date_comps, repeats)
				if not un_trigger or not un_trigger.nextTriggerDate():
					raise ValueError('Invalid date components for calendar trigger (in the past?)')
			if un_trigger is None:
				un_trigger = _parse_location_trigger(trigger)
	elif delay > 0:
		# Create implicit non-repeating trigger for `delay` keyword arg.
		un_trigger = UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_(delay, False)
	return un_trigger


def _process_sound(sound_name, content):
	if sound_name is None:
		return
	sound_file_path = None
	dest_filename = None
	if sound_name.lower() == 'default':
		content.setSound_(UNNotificationSound.defaultSound())
	elif ':' in sound_name:
		# Built-in sound effect name
		import sound
		sound_file_path = sound.get_effect_path(sound_name)
		dest_filename = sound_name.replace(':', '_') + '.caf'
	else:
		sound_file_path = os.path.abspath(sound_name)
	if sound_file_path:
		# Need to copy the sound file to ~/Library/Sounds, so that the notification process can find them...
		soundlib_path = _get_soundlib_path()
		if dest_filename:
			filename = dest_filename
		else:
			filename = os.path.split(sound_file_path)[-1]
		dest_path = os.path.join(soundlib_path, filename)
		try:
			shutil.copyfile(sound_file_path, dest_path)
			un_sound = UNNotificationSound.soundNamed_(filename)
			content.setSound_(un_sound)
		except Exception as e:
			raise ValueError('Invalid sound_name or unreadable file: %s' % (sound_name,))


def schedule(message=None, delay=0, sound_name=None, action_url=None, title=None, subtitle=None, attachments=None, trigger=None, actions=None, identifier=None):
	# Basic argument type validation:
	if not any((message, sound_name, title, subtitle)):
		raise ValueError('Notification must contain text or a sound.')
	if message is not None and not isinstance(message, basestring):
		raise TypeError('message must be a string')
	if not isinstance(delay, Number):
		raise TypeError('delay must be a number')
	if sound_name is not None and not isinstance(sound_name, basestring):
		raise TypeError('sound_name must be a string or None')
	if action_url is not None and not isinstance(action_url, basestring):
		raise TypeError('action_url must be a string or None')
	if title is not None and not isinstance(title, basestring):
		raise TypeError('title must be a string or None')
	if subtitle is not None and not isinstance(subtitle, basestring):
		raise TypeError('subtitle must be a string or None')
	if identifier is not None and not isinstance(identifier, basestring):
		raise TypeError('identifier must be a string or None')
	# Process attachments:
	un_attachments = _process_attachments(attachments)
	
	# Parse trigger:
	un_trigger = _parse_trigger(trigger, delay)
	
	user_info = {'buttonActions': {}}
	# Main action URL (gets invoked when the notification itself is tapped)
	if action_url:
		user_info['actionURL'] = action_url
	
	# Parse button actions, and fill user_info with the buttons' URLs:
	# Note: If a custom identifier is used for the notification, use that for the category as well.
	category_id = _parse_actions(actions, user_info, identifier)
	
	# Configure basic notification content:
	content = UNMutableNotificationContent.new().autorelease()
	content.setUserInfo_(user_info)
	if un_attachments:
		content.setAttachments_(un_attachments)
	if category_id:
		content.setCategoryIdentifier_(category_id)
	if title:
		content.setTitle_(title)
	if subtitle:
		content.setSubtitle_(subtitle)
	content.setBody_(message)
	
	if identifier is None:
		identifier = uuid.uuid4().hex
	
	# Add sound:
	_process_sound(sound_name, content)
	
	# Authorize notification access after all arguments are validated:
	authorized = _notification.authorize()
	if not authorized:
		return None
	
	# Schedule actual notification:
	req = UNNotificationRequest.requestWithIdentifier_content_trigger_(identifier, content, un_trigger)
	CENTER.addNotificationRequest_withCompletionHandler_(req, None)
	return identifier


if __name__ == '__main__':
	import ui
	schedule('Test', title='Title', sound_name='game:Beep', attachments=[ui.Image('test:Mandrill')])
