from math import atan2, hypot, pi

def compassDirection (userX, userY, chestX, chestY):
    deltaY = chestY - userY
    deltaX = chestX - userX
    
    degreesTemp = atan2(deltaY, deltaX)/pi*180
    
    if degreesTemp < 0:
        degreesFinal = 360 + degreesTemp
    else:
        degreesFinal = degreesTemp
    
    compassBrackets =  ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    compassLookup = round(degreesFinal/45)
    return compassBrackets[compassLookup]

def compassDistance (userX, userY, chestX, chestY):
    deltaY = abs(chestY - userY)
    deltaX = abs(chestX - userX)

    return hypot(deltaX, deltaY)

if __name__ == "__main__":
    print("This file should only be imported and not called directly, please run endless_swamp.py")
    exit