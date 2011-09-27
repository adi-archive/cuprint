import zmq
import sys
import settings
import json

ctx = zmq.Context()
sender = ctx.socket(zmq.PUSH)

def test():
	data = {'printer':'watt100a', 'uni':'zm2169', 
		'filename':'conversion-test.docx', 
		'tmp_file':'/tmp/cuprint/conversion-test.docx', 
		'options': {'copies':'1'}}
	sender.connect(settings.ZMQ_ADDR)
	sender.send('print '+json.dumps(data))
