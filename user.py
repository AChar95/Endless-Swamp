class User:
    
    def __init__(self, name, xCoordinates = 0, yCoordinates = 0):
        self._username = name
        self._xCoordinates = xCoordinates
        self._yCoordinates = yCoordinates
    
    @property
    def xCoordinates(self):
        return self._xCoordinates
    
    @property
    def yCoordinates(self):
        return self._yCoordinates
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        self._username = value
    
    @xCoordinates.setter
    def xCoordinates(self, value):
        self._xCoordinates = value
    
    @yCoordinates.setter
    def yCoordinates(self, value):
        self._yCoordinates = value