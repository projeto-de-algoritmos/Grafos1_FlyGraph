import json
from graphs import *

def jsonalize(object):
	parsed = json.dumps(object, indent=2, default=Flight.ComplexHandler)
	return parsed

def pprint(object):
	print(jsonalize(object))
