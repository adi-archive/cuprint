import settings
import cups
import os
import zmq
import sys
import json
from helpers import deunicode

def convert_document(filename):
	newfilename = filename.rsplit('.',1)[0]+'.ps'
	cmd = 'abiword --to=ps --to-name="%s" "%s"' % (newfilename, filename)
	os.system(cmd)
	if os.path.isfile(newfilename):
		return newfilename
	return None

def convert_spreadsheet(filename):
	newfilename = filename.rsplit('.', 1)[0]+'.pdf'
	cmd = 'ssconvert %s %s' % (filename, newfilename)
	os.system(cmd)
	if os.path.isfile(newfilename):
		return newfilename
	return None

FORMAT_CONVERTERS = (
	(('doc', 'docx', 'odt', 'rtf'), convert_document),
	(('xls', 'xlsx', 'ods', 'csv'), convert_spreadsheet),
	(('pdf', 'ps'), None)
)

def convert_file(filename):
	if '.' in filename:
		ext = filename.rsplit('.', 1)[1]
		for (exts, converter) in FORMAT_CONVERTERS:
			if ext in exts:
				if converter:
					newfilename = converter(filename)
					if newfilename:
						return newfilename
					return None
				return filename
		return None
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

