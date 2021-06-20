from random import randint
from win_mechanic import winMechanic
from user import User
from plot import plot
from movement import travelling
from chest import Chest
from compass import compassDirection, compassDistance

def main():
    chest = Chest()
    chest.chestX = randint(-50,50)
    chest.chestY = randint(-50,50)
    userName = input("Please enter your character's name: ")
    user = User(userName)
    while True:
        direction = input("Which direction would you like to go: ")
        direction = direction.lower()
        if direction == "west" or direction == "east":
            user.xCoordinates = travelling(direction, user)
        elif direction == "north" or direction == "south":
            user.yCoordinates = travelling(direction, user)
        else:
            print("%s is not supported direction" %(direction))
            travelling(direction, user)
        print(str(user.xCoordinates) + " " + str(user.yCoordinates))
        print(str(compassDistance(user, chest)) + " " + str(compassDirection(user, chest)))
        winMechanic(compassDistance(user, chest))
    # print(''' 
    #       Welcome to the endless swamp, a place of infantismal sludge as far as the eye can see.
    #       The jolly wagon driver waved goodbye before whipping the mule. 'Good luck on your hunt %s' he shouts as he drives away
    #       ''' %(userName))
    # print(plot()["chapter-1"][0]["point"] %(userName))
if __name__ == "__main__":
    main()
