from random import randint
import json, requests


def travelling(direction, User):
    def goNorth(User):
        ylocation = User.yCoordinates
        return ylocation + 1

    def goSouth(User):
        ylocation = User.yCoordinates
        return ylocation - 1

    def goEast(User):
        xlocation = User.xCoordinates
        return xlocation + 1

    def goWest(User):
        xlocation = User.xCoordinates
        return xlocation - 1

    def noMovement():
        try:
            stationaryAction = open('./data_files/stationary_action.json', 'r')
            actionExtractor = json.load(stationaryAction)
            if len(actionExtractor["actions"]) > 0:
                randomNumber = randint(0, len(actionExtractor["actions"])-1)
                print(randomNumber)
                action = actionExtractor["actions"][randomNumber]["supported_actions"]
                print("You continue to stand still")
                print(action)
            else:
                print("Random Action catalogue file (stationary_action.json) is not formated correctly\rAttempting to pull latest version from 'https://github.com/AChar95/Endless-Swamp'")
                url = "https://raw.githubusercontent.com/AChar95/Endless-Swamp/main/data_files/stationary_action.json"
                r = requests.get(url)
                with open('./data_files/stationary_action.json', 'wb') as f:
                    f.write(r.content)
                    f.close()
        except IOError:
            print("Plot file cannot be found")
            exit()
        except ValueError:
            print("Json plot file could not be read properly")
            exit()
    switch = {
        'north': goNorth(User),
        'south': goSouth(User),
        'east': goEast(User),
        'west': goWest(User)
    }

    return switch.get(direction, noMovement())
