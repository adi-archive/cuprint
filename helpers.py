import settings
import cups
from werkzeug import secure_filename
import os

def file_allowed(filename):
	if '.' in filename:
		ext = filename.split('.')[-1]
		return ext in settings.ALLOWED_EXTENSIONS
	return False
	
def print_file(f, form):
	filename = secure_filename(f.filename)
	tmp_file = os.path.join(settings.UPLOAD_DIR, filename)
	f.save(tmp_file)
	options={'copies':str(form['copies']), 'sides':str(form['sides'])}
	if form['page-ranges']:
		options['page-ranges'] = str(form['page-ranges'])
	cups.setUser(form['uni'])
	conn = cups.Connection()
	try:
		return conn.printFile(form['printer'], tmp_file, filename, options)
	except cups.IPPError:
		return False

