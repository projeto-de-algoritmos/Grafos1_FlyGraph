class Aresta:
	def __init__(self, i, f, used = False):
		self.__i = i 
		self.__f = f
		self.__used = used
	
	def jsonable(self):
		return self.__dict__

	def ComplexHandler(Obj):
		if hasattr(Obj, 'jsonable'):
			return Obj.jsonable()

	@property
	def used(self):
		return self.__used

	@property
	def i(self):
		return self.__i

	@property
	def f(self):
		return self.__f

	@used.setter
	def used(self, used):
		self.__used = used

	@i.setter
	def i(self, i):
		self.__i = i

	@f.setter
	def f(self, f):
		self.__f = f