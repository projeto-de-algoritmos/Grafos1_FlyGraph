class Airport:
    def __init__(self,
                 oaci,
                 state,
                 operation,
                 latitude,
                 longitude,
                 altitude,
                 name,
                 town,
                 flights=[]):
        self.__oaci = oaci
        self.__state = state
        self.__operation = operation
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altitude = altitude
        self.__name = name
        self.__town = town
        self.__flights = flights

    def jsonable(self):
        return self.__dict__

    def ComplexHandler(Obj):
        if hasattr(Obj, 'jsonable'):
            return Obj.jsonable()

    def appendEdge(self, node):
        self.__flights.append(node)

    @property
    def oaci(self):
        return self.__oaci

    @property
    def state(self):
        return self.__state
    
    @property
    def operation(self):
        return self.__operation
    
    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude
    
    @property
    def altitude(self):
        return self.__altitude

    @property
    def name(self):
        return self.__name

    @property
    def town(self):
        return self.__town

    @property
    def flights(self):
        return list(self.__flights)

    @property
    def name(self):
        return self.__name

    @oaci.setter
    def oaci(self, oaci):
        self.__oaci = oaci

    @state.setter
    def state(self, state):
        self.__state = state

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude

    @altitude.setter
    def altitude(self, altitude):
        self.__altitude = altitude

    @name.setter
    def name(self, name):
        self.__name = name

    @town.setter
    def town(self, town):
        self.__town = town

    @flights.setter
    def flights(self, flights):
        self.__flights = flights
