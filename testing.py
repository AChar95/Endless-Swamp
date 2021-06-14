import unittest
from user import User

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
        
if __name__ == '__main__':
    unittest.main()