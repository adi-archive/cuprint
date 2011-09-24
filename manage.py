#!/usr/bin/env python

import sys, os
import signal

def daemonize(func, args, pid_path, log_path):
	pid = os.fork()
	if pid:
		f = open(pid_path, 'w')
		f.write(str(pid))
		f.close()
		exit()
	else:
		f = open(log_path, 'a')
		sys.stdout = log_path
		sys.stderr = log_path
		sys.stdin = open('/dev/null')
		func(*args)

def stopworker():
	if os.path.isfile('worker.pid'):
		f = open('worker.pid')
		pid = int(f.read())
		f.close()
		print('Killing worker process with pid '+str(pid))
		for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGKILL):
			os.kill(pid, sig)
		os.remove('worker.pid')
	else:
		print('Worker not running')

def startworker(nodaemon=False):
	from worker import make_socket, work_loop
	
	if not os.path.isfile('worker.pid'):
		print('Starting worker')
		receiver = make_socket()
		if nodaemon:
			work_loop(receiver)
		else:
			daemonize(work_loop, (receiver,), 'worker.pid', 'error.log')
	else:
		print('Worker already running')

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
	
