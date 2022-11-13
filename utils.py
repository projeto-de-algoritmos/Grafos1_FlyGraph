import json
from graphs import *

def jsonalize(object):
	parsed = json.dumps(object, indent=2, default=Aresta.ComplexHandler)
	return parsed

def pprint(object):
	print(jsonalize(object))
