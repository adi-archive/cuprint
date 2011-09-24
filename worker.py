import settings
import cups
import os
import zmq
import sys
import json

def deunicode(obj):
	if isinstance(obj, dict):
		retval = {}
		for key, val in obj.items():
			if(isinstance(key, unicode)):
				key = str(key)
			if(isinstance(val, unicode)):
				val = str(val)
			elif(isinstance(val, (list,dict))):
				val = deunicode(val)
			retval[key] = val
		return retval
	elif isinstance(obj, list):
		retval = []
		for item in obj:
			if(isinstance(item, unicode)):
				retval.append(str(item))
			elif(isinstance(item, (list,dict))):
				retval.append(deunicode(item))
			else: retval.append(item)
		return retval
	else:
		return obj


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

