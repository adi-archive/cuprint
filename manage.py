#!/usr/bin/env python

import sys, os
from application import app
import json
import cPickle as pickle

def setup_redis():
	r = redis.Redis()
	with open('printers.json') as f:
		printers = json.load(f)
		for key in printers:
			val = pickle.dumps(printers[key])
			r.hset('printers', key, val)

def runapp():
	'''Start the development server'''
	app.run()
	

def genkey():
	'''Generate a SECRET_KEY'''
	key = os.urandom(24)
	line="SECRET_KEY="+repr(key)
	print(line)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage: "+sys.argv[0]+" command [args...]")
	command = locals()[sys.argv[1]]
	command(*sys.argv[2:])
	
