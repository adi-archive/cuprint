from flask import Flask, session, request, render_template, redirect
import settings
from filters import filters
import cPickle as pickle
import os
from werkzeug import secure_filename
import cups

app = Flask(__name__)
app.config.from_object(settings)
app.jinja_env.filters.update(filters)

def file_allowed(filename):
	if '.' in filename:
		ext = filename.split('.')[-1]
		return ext in app.config['ALLOWED_EXTENSIONS']
	return False
	
def print_file(f):
	filename = secure_filename(f.filename)
	tmp_file = os.path.join(app.config['UPLOAD_DIR'], filename)
	f.save(tmp_file)
	options={'copies':str(request.form['copies'])}
	if request.form['page-ranges'] != 'all':
		options['page-ranges'] = str(request.form['page-ranges'])
	cups.setUser(request.form['uni'])
	conn = cups.Connection()
	try:
		return conn.printFile(request.form['printer'], tmp_file, filename, options)
	except cups.IPPError:
		return False

# Example route, delete this and add your own
@app.route('/')
def index():
	return render_template('buildings.html', buildings=app.config['BUILDINGS'])

@app.route('/<building>/print')
def print_form(building):
	printers = app.config['PRINTERS'][building]
	return render_template('printers.html', printers=printers)
	
@app.route('/print', methods=['POST'])
def handle_print():
	f = request.files['document']
	if file_allowed(f.filename):
		if print_file(f):
			return render_template('success.html')
		else: redirect('failure.html')
	return render_template("notallowed.html")
	
		
	

application=app
