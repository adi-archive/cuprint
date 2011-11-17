import settings
import cups
import os
import zmq
import sys
import json
from helpers import deunicode

def convert_file(filename):
	if '.' in filename:
		basename, ext = os.path.splitext(filename)
		ext = ext[1:]
		if ext in settings.DIRECT_PRINT_FORMATS:
			return filename
		if ext in settings.CONVERTABLE_FORMATS:
			newname = basename + '.pdf'
			cmd = 'unoconv -f pdf %s' % filename
			os.system(cmd)
			if os.path.isfile(newname):
				return newname
	return None

def print_file(filename, tmp_file, printer, uni, options):
	cups.setUser(uni)
	conn = cups.Connection()
	try:
		conv_file = convert_file(tmp_file)
		if conv_file:
			conn.printFile(printer, conv_file, filename, options)
			sys.stderr.write('File '+conv_file+' printed successfully\n')
			sys.stderr.flush()
		else:
			sys.stderr.write("Could not convert "+tmp_file+" successfully\n")
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

