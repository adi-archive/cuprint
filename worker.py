import settings
import cups
import os
import zmq
import sys

def print_file(filename, tmp_file, printer, uni, options):
	cups.setUser(uni)
	conn = cups.Connection()
	try:
		conn.printFile(printer, tmp_file, filename, options)
		sys.stderr.write('File '+tmp_file+' printed successfully\n')
		sys.stderr.flush()
	except cups.IPPError:
		sys.stderr.write('Printing '+tmp_file+' unsuccessful')
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

		cmdname, datajson = tuple(s.split(' ', 1))

		cmd = COMMANDS[cmdname]

		data = json.loads(datajson)

		print('got command '+cmdname+' '+data)
		sys.stdout.flush()

		if(isinstance(data, dict)):
			cmd(**data)
		elif(isinstance(data, list)):
			cmd(*data)
		else: cmd(data)

