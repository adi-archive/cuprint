import re

def slugify(s):
	value = re.sub(r'[^\w\s-]', '', s).strip().lower()
	value = re.sub(r'[-\s]+', '-', value)
	return value

filters={'slugify': slugify}
