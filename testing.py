import unittest
from user import User
from chest import Chest
from compass import compassDirection, compassDistance

class TestingUserMethod(unittest.TestCase):
    
    def testingXCoordinate(self):
        user = User('Keiran', 3, 5)
        self.assertEqual(user.xCoordinates, 3)
    
    def testingYCoordinate(self):
        user = User('Keiran', 3, 5)
        self.assertEqual(user.yCoordinates, 5)
    
    def testingUserName(self):
        user = User('Keiran', 3, 5)
        self.assertEqual(user.username, 'Keiran')
    
    def testingChestXCoordinate(self):
        chest = Chest(3,5)
        self.assertEqual(chest.chestX, 3)
    
    def testChestYCoordinate(self):
        chest = Chest(3,5)
        self.assertEqual(chest.chestY, 5)
        
    def testCompassDirection(self):
        chest = Chest(3,5)
        user = User('Keiran',0,0)
        self.assertEqual(compassDirection(user,chest),'NE')
        
    def testForEast(self):
        chest = Chest(3,5)
        user = User('Keiran',0,5)
        self.assertEqual(compassDirection(user,chest),'E')
    
    def testForSouth(self):
        chest = Chest(3,-5)
        user = User('Keiran',3,0)
        self.assertEqual(compassDirection(user,chest),'S')
    
    def testForDistance(self):
        chest = Chest(3,5)
        user = User('Keiran',0,0)
        self.assertEqual(compassDistance(user,chest),6)
        
if __name__ == '__main__':
    unittest.main()