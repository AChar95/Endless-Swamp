class User:
    
    def __init__(self, xCoordinates, yCoordinates):
        self._xCoordinates = xCoordinates
        self._yCoordinates = yCoordinates
    
    @property
    def xCoordinate(self):
        return self._xCoordinates
    
    @property
    def yCoordinate(self):
        return self._yCoordinates
    
    @xCoordinate.setter
    def xCoordinate(self, value):
        self._xCoordinates = value
    
    @yCoordinate.setter
    def yCoordinate(self, value):
        self._yCoordinates = value