# Flask builtins
DEBUG=True
# Generate this with ./manage.py genkey

PRINTERS={
	"dodge": ["dodgeart701a", "dodgeart701b", "dodgeart412a"], 
	"residence-halls": ["broadway304a", "carman103a", "carman103b", 
		"claremontb01a", "ec10a", "ec18a", "furnald102a", "harmony100a", 
		"hartley112a", "hartley112b", "mcbain100a", "riverb01a", "schapiro108a", 
		"watt100a", "wien211a", "wien211b", "woodbridge100a"], 
	"lerner": ["lerner200a", "lerner200b", "lerner300a", "lerner300b"], 
	"statistics": ["statistics902a"], 
	"schermerhorn": ["schermerhorn558a", "schermerhorn601a"], 
	"kent": ["kent300a", "kent300b"], 
	"avery": ["avery200a", "avery200b"], 
	"philosophy": ["philo301a"], 
	"barnard": ["bclibrary100a", "bclibrary200a", "brooks100a", "brooks100b", 
		"dcc413a", "diana307a", "diana307b", "diana307c", "plimpton100a", 
		"plimpton100b", "sixsixteen100a", "sixsixteen100b", "sulzberger100a"], 
	"medical-center": ["ph17107a", "ph17107b", "hammerb100a", "hammer100a", 
		"hammer100b", "hammer100c", "hammer100d", "hammer100e", "hammer100f", 
		"hammer200a", "hammer200b", "hammer200c", "hammer200d", "hammer200e", 
		"hammer200f", "hammer200g", "bard100a", "bdh100b", "tw2100a"], 
	"intl-affairs": ["iab323color", "iab323a", "iab323b", "iab215a", 
		"iab309a", "iab310a", "iab329a"], "career-services": ["ccsa"], 
	"watson": ["watson8", "watson811a"], 
	"social-work": ["socialwork202a", "socialwork207a", "socialwork105a", 
	"socialwork105b", "socialwork105c", "socialwork105d", "socialwork105e", 
	"socialwork214a", "socialwork309a", "socialwork401a", "socialwork403a", 
	"socialwork721a", "socialwork821a", "socialwork900a"], 
	"mudd": ["et251color", "mudd251a", "mudd251b", "mudd251c", "mudd422a"], 
	"butler": ["butler209a", "butler209b", "butler213a", "butler213b", 
		"butler213c", "butler300a", "butler300b", "butler403a", "butler403b", 
		"butler301a", "butler305a", "butler401a", "butler501a", "butler600a", 
		"butler606a"], 
	"uris": ["uris130a", "uris130b", "uris130c", "uris130d"], 
	"lewisohn": ["lewisohn300a", "lewisohn300b"], 
	"math": ["math407a", "math303a"], 
	"burke": ["burke100a", "burke300a"]
}

BUILDINGS=['Avery', 'Barnard', 'Burke', 'Butler', 'Career Services', 'Dodge', 
	'Int\'l Affairs', 'Kent', 'Lerner', 'Lewisohn', 'Math', 
	'Medical Center', 'Mudd', 'Philosophy', 'Residence Halls', 'Schermerhorn', 
	'Social Work', 'Statistics', 'Uris', 'Watson']

import os

UPLOAD_DIR='/tmp/cuprint'

if not os.path.isdir(UPLOAD_DIR):
	os.mkdir(UPLOAD_DIR)
	
ZMQ_ADDR='tcp://127.0.0.1:5555'

DIRECT_PRINT_FORMATS = {'pdf', 'ps'}
