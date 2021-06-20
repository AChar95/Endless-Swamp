from math import atan2, ceil, hypot, pi

def compassDirection (User, chest):
    
    deltaY = chest.chestY - User.yCoordinates
    deltaX = chest.chestX - User.xCoordinates
    
    degreesTemp = atan2(deltaY, deltaX)/pi*180
    if deltaX == 0 or deltaY == 0:
        if deltaX == 0 and deltaY == 0:
            return ""
        elif deltaX == 0:
            if checkDirection(deltaY):
                return "N"
            else:
                return "S"
        elif deltaY == 0:
            if checkDirection(deltaX):
                return "E"
            else:
                return "W"
        else:
            print("This outcome is not supported, critical error in program, exiting now")
            exit
    else:
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
    return ceil(hypot(deltaX, deltaY))

def checkDirection(coordinateValue):
    if coordinateValue > 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print("This file should only be imported and not called directly, please run endless_swamp.py")
    exit