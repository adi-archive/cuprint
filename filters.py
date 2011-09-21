import re

def slugify(s):
	value = re.sub(r'[^\w\s-]', '', s).strip().lower()
	value = re.sub(r'[-\s]+', '-', value)
	return value
	
def unslugify(value):
	return ' '.join([s.capitalize() for s in value.split('-')])

filters={'slugify': slugify, 'unslugify':unslugify}
