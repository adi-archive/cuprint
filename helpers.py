import settings
from werkzeug import secure_filename
import os
import zmq
import json

context = zmq.Context()

def connect_to_worker():
	sender = context.socket(zmq.PUSH)
	sender.connect(settings.ZMQ_ADDR)
	
	return sender

def print_file(f, form):
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
	sender.send('print '+data)
