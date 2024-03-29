#import 'pythonista'
from _cb import *

shared_manager = None
reset = None

class SharedCentralManager (CentralManager):
	def __init__(self):
		self.delegate = None
		self.verbose = False
	
	def verbose_log(self, msg):
		if self.verbose:
			print(msg)
	
	def did_update_state(self):
		self.verbose_log('CB: Did update state: %i' % self.state)
		try:
			self.delegate.did_update_state()
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_discover_peripheral(self, p):
		self.verbose_log('CB: Did discover peripheral: %s (%s)' % (p.name, p.uuid))
		try:
			self.delegate.did_discover_peripheral(p)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_connect_peripheral(self, p):
		self.verbose_log('CB: Did connect peripheral: %s (%s)' % (p.name, p.uuid))
		try:
			self.delegate.did_connect_peripheral(p)
		except AttributeError:
			pass
		except:
			reset()
			raise
		
	
	def did_fail_to_connect_peripheral(self, p, error):
		self.verbose_log('CB: Did fail to connect peripheral: %s (%s) -- Error: %s' % (p.name, p.uuid, error))
		try:
			self.delegate.did_fail_to_connect_peripheral(p, error)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_disconnect_peripheral(self, p, error):
		self.verbose_log('CB: Did disconnect peripheral: %s (%s) -- Error: %s' % (p.name, p.uuid, error))
		try:
			self.delegate.did_disconnect_peripheral(p, error)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_discover_services(self, p, error):
		self.verbose_log('CB: Did discover services for peripheral: %s (%s)' % (p.name, p.uuid))
		try:
			self.delegate.did_discover_services(p, error)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_discover_characteristics(self, s, error):
		self.verbose_log('CB: Did discover characteristics for service: %s' % (s.uuid,))
		try:
			self.delegate.did_discover_characteristics(s, error)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_write_value(self, c, error):
		self.verbose_log('CB: Did write value for characteristic: %s' % c.uuid)
		try:
			self.delegate.did_write_value(c, error)
		except AttributeError:
			pass
		except:
			reset()
			raise
	
	def did_update_value(self, c, error):
		self.verbose_log('CB: Did update value for characteristic: %s' % c.uuid)
		try:
			self.delegate.did_update_value(c, error)
		except AttributeError:
			pass
		except:
			reset()
			raise

shared_manager = SharedCentralManager()

def set_central_delegate(delegate):
	shared_manager.delegate = delegate

def set_verbose(verbose):
	shared_manager.verbose = verbose

def scan_for_peripherals():
	shared_manager.scan_for_peripherals()

def stop_scan():
	shared_manager.stop_scan()

def connect_peripheral(peripheral):
	shared_manager.connect_peripheral(peripheral)

def cancel_peripheral_connection(peripheral):
	shared_manager.cancel_peripheral_connection(peripheral)

def get_state():
	return shared_manager.state

def reset():
	global shared_manager
	shared_manager.delegate = None
	del shared_manager
	shared_manager = SharedCentralManager()
