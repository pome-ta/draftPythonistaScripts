#import 'pythonista'
import _twitter
import json

def get_all_accounts():
	return _twitter.get_all_accounts()

def get_account(username):
	if username.startswith('@'):
		username = username[1:]
	accounts = _twitter.get_all_accounts()
	for a in accounts:
		if a.get('username', None) == username:
			return a
	return None

def request(account, url, method='GET', parameters=None):
	if parameters is None:
		parameters = {}
	account_id = account.get('id')
	param_data = json.dumps(parameters)
	return _twitter.request(method, url, account_id, param_data)

def get_request_headers(account, url, method='GET', parameters=None):
	if parameters is None:
		parameters = {}
	account_id = account.get('id')
	param_data = json.dumps(parameters)
	headers_json = _twitter.get_request_headers_json(method, url, account_id, param_data)
	return json.loads(headers_json)

def get_mentions_timeline(account, count=20, parameters=None):
	all_parameters = {'count': str(count)}
	if parameters is not None:
		all_parameters.update(parameters)
	status, data = request(account, 'https://api.twitter.com/1.1/statuses/mentions_timeline.json', 'GET', {'count': str(count)})
	if status == 200:
		mentions = json.loads(data.decode('utf-8'))
		return mentions
	return None

def get_home_timeline(account, count=20, parameters=None):
	all_parameters = {'count': str(count)}
	if parameters is not None:
		all_parameters.update(parameters)
	status, data = request(account, 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'GET', all_parameters)
	if status == 200:
		tweets = json.loads(data.decode('utf-8'))
		return tweets
	return None

def get_favorites(account, username=None, count=20, parameters=None):
	if username is None:
		username = account.get('username')
	all_parameters = {'count': str(count), 'screen_name': username}
	if parameters is not None:
		all_parameters.update(parameters)
	status, data = request(account, 'https://api.twitter.com/1.1/favorites/list.json', 'GET', all_parameters)
	if status == 200:
		tweets = json.loads(data.decode('utf-8'))
		return tweets
	return None

def search(account, query, count=20, parameters=None):
	all_parameters = {'q': query, 'count': str(count)}
	if parameters is not None:
		all_parameters.update(parameters)
	status, data = request(account, 'https://api.twitter.com/1.1/search/tweets.json', 'GET', all_parameters)
	if status == 200:
		tweets = json.loads(data.decode('utf-8'))
		return tweets
	return None

def post_tweet(account, text, parameters=None):
	all_parameters = {'status': text}
	if parameters is not None:
		all_parameters.update(parameters)
	status, data = request(account, 'https://api.twitter.com/1.1/statuses/update.json', 'POST', all_parameters)
	if status == 200:
		tweet = json.loads(data.decode('utf-8'))
		return tweet
	return None