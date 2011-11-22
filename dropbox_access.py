from flask import session, redirect, url_for
from dropbox import rest, session, client
from keys import DROPBOX_APP_KEY, DROPBOX_APP_SECRET

ACCESS_TYPE = 'dropbox'

def get_dropbox_session():
	return session.DropboxSession(DROPBOX_APP_KEY, 
			DROPBOX_APP_SECRET, ACCESS_TYPE)

def authenticate():
	sess = get_dropbox_session()
	request_token = sess.obtain_request_token()
	url = sess.build_authorize_url(request_token,
			# url_for('show_dropbox'))
			# For development.
			'127.0.0.1:5000/dropbox'
	return redirect(url)

def get_access_token():
	sess = get_dropbox_session()
	try:
		access_token = sess.obtain_access_token(request_token)
	except rest.ErrorResponse:
		pass # Handle this error.
	# Save sess.
	return client.DropboxClient(sess)

def get_dir(client, directory):
	global cache #load cache
	global cache_data

	try:
		output = client.metadata(directory, Hash = cache.get(directory))
		cache[directory] = output['hash']
	except rest.ErrorResponse as e:
		if e.status == 304:
			output = cache_data.get(directory)
		elif e.status == 401:
			authenticate()
		elif e.user_error_msg:
			pass # Show error. 
	#save cache
	return output['contentscont']