from user import User
from random import randint
import json

def goNorth(User):
        ylocation = User.yCoordinates
        print(ylocation)
        ylocation = ylocation + 1
        print(ylocation)
        User.yCoordinates(ylocation)

def noMovement():
    try:
        stationaryAction = open('./data_files/stationary_action.json', 'r')
        actionExtractor = json.load(stationaryAction)
        if len(actionExtractor) > 0:
            randomNumber = randint(0,len(actionExtractor))
            action = actionExtractor[randomNumber]["action"]
        else:
            print("Random Action catalogue file (stationary_action.json is not formated correctly")
    except IOError:
        print("Plot file cannot be found")
        exit
    except ValueError:
        print("Json plot file could not be read properly")
        exit

    print("You continue to stand still")
    print(action)


def travelling(direction, User):
    switch = {
        "north": goNorth(User),
        "south": goSouth(User),
        "east": goEast(User),
        "west": goWest(User) 
    }

    switch.get(direction, noMovement)(User)  