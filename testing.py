import unittest
from user import User
from chest import Chest

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
        
        
if __name__ == '__main__':
    unittest.main()