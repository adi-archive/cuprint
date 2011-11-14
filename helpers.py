import settings
from werkzeug import secure_filename
import os
import zmq
import json

def get_preview_url(filename):
	base, ext = os.path.splitext(filename)
	if ext in settings.DIRECT_PRINT_FORMATS:
		return '/tmp/'+filename
	return '/tmp/'+base+'.pdf'

def deunicode(obj):
	if isinstance(obj, dict):
		retval = {}
		for key, val in obj.items():
			if(isinstance(key, unicode)):
				key = str(key)
			if(isinstance(val, unicode)):
				val = str(val)
			elif(isinstance(val, (list,dict))):
				val = deunicode(val)
			retval[key] = val
		return retval
	elif isinstance(obj, list):
		retval = []
		for item in obj:
			if(isinstance(item, unicode)):
				retval.append(str(item))
			elif(isinstance(item, (list,dict))):
				retval.append(deunicode(item))
			else: retval.append(item)
		return retval
	else:
		return obj

def connect_to_worker():
	context = zmq.Context()
	sender = context.socket(zmq.PUSH)
	sender.connect(settings.ZMQ_ADDR)
	
	return sender

def send_job(f, form):
	filename = secure_filename(f.filename)
	tmp_file = os.path.join(settings.UPLOAD_DIR, filename)
	f.save(tmp_file)
	options={'copies':str(form['copies']), 'sides':str(form['sides'])}
	if 'Collate' in form and form['Collate']=='collate':
		options['Collate'] = 'True'
	if form['page-ranges']:
		options['page-ranges'] = str(form['page-ranges'])
	
	sender = connect_to_worker()
	data = json.dumps({'filename': filename, 'tmp_file':tmp_file, 
		'options':options, 'printer':form['printer'], 'uni':form['uni']})
	print('sending job')
	sender.send('print '+data)
	return get_preview_url(filename)
