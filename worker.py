import settings
import cups
import os
import zmq
import sys
import json
from helpers import deunicode

def print_file(filename, tmp_file, printer, uni, options):
	cups.setUser(uni)
	conn = cups.Connection()
	try:
		conn.printFile(printer, tmp_file, filename, options)
		sys.stderr.write('File '+tmp_file+' printed successfully\n')
		sys.stderr.flush()
	except cups.IPPError:
		sys.stderr.write('Printing '+tmp_file+' unsuccessful\n')
		sys.stderr.flush()

COMMANDS = {'print':print_file}

def make_socket():
	context = zmq.Context()
	receiver = context.socket(zmq.PULL)
	receiver.bind(settings.ZMQ_ADDR)

	return receiver

def work_loop(receiver):
	while True:
		s = receiver.recv()
		
		tup = tuple(s.split(' ',1))

		if(len(tup) != 2): continue

		cmdname, datajson = tup

		cmd = COMMANDS.get(cmdname)

		if not cmd:
			print('Command '+cmdname+' not found')
			continue

		data = deunicode(json.loads(str(datajson)))

		print('got command '+cmdname+' '+datajson)

		if(isinstance(data, dict)):
			cmd(**data)
		elif(isinstance(data, list)):
			cmd(*data)
		else: cmd(data)

