from flask import Flask, session, request, render_template, redirect
import settings
from filters import filters
from helpers import *
import os
import cups
import sys

app = Flask(__name__)
app.config.from_object(settings)
app.jinja_env.filters.update(filters)

@app.route('/')
def index():
	return render_template('buildings.html', buildings=app.config['BUILDINGS'])

@app.route('/<building>/print')
def print_form(building):
	printers = app.config['PRINTERS'][building]
	return render_template('printers.html', building=building, printers=printers)
	
@app.route('/print', methods=['POST'])
def handle_print():
	f = request.files['document']
	if print_file(f, request.form):
		return render_template('success.html', 
			printer=request.form['printer'])
	else: redirect('failure.html')

@app.route('/help')
def show_help():
	return render_template('help.html')

@app.route('/contact')
def show_contact():
	return render_template('contact.html')

@app.route('/terms')
def show_terms():
	return render_template('terms.html')
	
application=app
