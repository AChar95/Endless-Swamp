from math import atan2, hypot, pi

def compassDirection (User, chest):
    
    deltaY = chest.chestY - User.yCoordinates
    deltaX = chest.chestX - User.xCoordinates
    
    degreesTemp = atan2(deltaY, deltaX)/pi*180
    
    if degreesTemp < 0:
        degreesFinal = 360 + degreesTemp
    else:
        degreesFinal = degreesTemp
    
    compassBrackets =  ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    compassLookup = round(degreesFinal/45)
    return compassBrackets[compassLookup]

def compassDistance (User, chest):
    deltaY = abs(chest.chestY - User.yCoordinates)
    deltaX = abs(chest.chestX - User.xCoordinates)

    return hypot(deltaX, deltaY)

if __name__ == "__main__":
    print("This file should only be imported and not called directly, please run endless_swamp.py")
    exit