from random import expovariate, randrange
from user import User
from plot import plot
from movement import travelling

def main():
    userName = input("Please enter your character's name: ")
    user = User(userName)
    while True:
        direction = input("Which direction would you like to go: ")
        direction = direction.lower()
        if direction == "west" or direction == "east" or direction == "north" or direction == "south":
            travelling(direction, user)
            print(user.xCoordinates + user.yCoordinates)
        else:
            exit
    # print(''' 
    #       Welcome to the endless swamp, a place of infantismal sludge as far as the eye can see.
    #       The jolly wagon driver waved goodbye before whipping the mule. 'Good luck on your hunt %s' he shouts as he drives away
    #       ''' %(userName))
    # print(plot()["chapter-1"][0]["point"] %(userName))
if __name__ == "__main__":
    main()
