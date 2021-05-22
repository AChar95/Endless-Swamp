class Chest:
    def __init__(self):
        self._chestX
        self._chestY
        
    @property
    def chestX(self):
        return self._chestX
    
    @property
    def chestY(self):
        return self._chestY
    
    @chestX.setter
    def chestX(self, value):
        self._chestX = value
    
    @chestY.setter
    def chestY(self, value):
        self._chestY = value