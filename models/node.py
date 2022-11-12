class No:
	def __init__(self, id, la = []):
		self.__id = id
		self.__la = list(la)

	def appendEdge(self, node):
		self.__la.append(node)

	@property
	def id(self):
		return self.__id
	
	@property 
	def la(self):
		return list(self.__la)

	@la.setter
	def la(self, la):
		self.__la = la