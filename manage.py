#!/usr/bin/env python

import sys, os
import signal
from importlib import import_module

def runtest(testname):
	test = import_module('tests.'+testname)
	test.test()

def runworker(nodaemon=False):
	from worker import make_socket, work_loop
	
	print('Running worker')
	receiver = make_socket()
	work_loop(receiver)

def runapp():
	from application import app
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
	
