from flask import Flask, session, request, render_template, redirect, url_for
import settings
from filters import filters
from helpers import send_job, get_preview_url
import os
import cups
import sys
from keys import FLASK_SECRET_KEY
from dropbox_access import authenticate

app = Flask(__name__)
app.config.from_object(settings)
app.jinja_env.filters.update(filters)

@app.route('/')
def index():
	return render_template('buildings.html', buildings=app.config['BUILDINGS'],
			special_buildings=app.config['SPECIAL_BUILDINGS'])

@app.route('/<building>/print')
def print_form(building):
	printers = app.config['PRINTERS'][building]
	return render_template('printers.html', building=building, printers=printers)
	
@app.route('/print', methods=['POST'])
def handle_print():
	f = request.files['document']
	send_job(f, request.form)
	preview_url = get_preview_url(f.filename)
	return render_template('success.html', 
			printer=request.form['printer'], preview_url=preview_url)

@app.route('/dropbox')
def show_dropbox():
	if 'uid' in session:
		return(redirect(url_for(show_dropbox_dir)))
	elif 'uid' in request.args and 'oauth_token' in request.args:
		session['uid'] = request.args['uid']
		session['oauth_token'] = request.args['oauth_token']
		return(redirect('/dropbox/root/'))
	else:
		return authenticate()

@app.route('/dropbox/<path:dropbox_path>')
def show_dropbox_dir(dropbox_path):
	return dropbox_path

@app.route('/help')
def show_help():
	return render_template('help.html')

@app.route('/contact')
def show_contact():
	return render_template('contact.html')

@app.route('/terms')
def show_terms():
	return render_template('terms.html')

if app.config['DEBUG']:
	from werkzeug import SharedDataMiddleware
	app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
		'/tmp': app.config['UPLOAD_DIR']
	})

application=app
app.secret_key = FLASK_SECRET_KEY
