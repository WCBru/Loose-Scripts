def generateCell(location, src):
    total = 0;
    for x in range(-1,2):
        for y in range(-1,2):
            if src.get((location[0]+x, location[1]+y)):
                total+= src[(location[0]+x, location[1]+y)]

    return total

def findTarget(target):
    data = {(0,0):1}
    currentVal = 1
    currentLocation = (0,0)
    level = 0
    while currentVal <= target:
        if currentLocation[1] == -1*level:
            currentLocation = (currentLocation[0]+1, currentLocation[1])
            if currentLocation[0] > level:
                level+= 1
        elif currentLocation[0] == -1*level:
            currentLocation = (currentLocation[0], currentLocation[1]-1)
        elif currentLocation[1] == level:
            currentLocation = (currentLocation[0]-1, currentLocation[1])
        elif currentLocation[0] == level:
            currentLocation = (currentLocation[0], currentLocation[1]+1)

        currentVal = generateCell(currentLocation, data)
        data[currentLocation] = currentVal

    return currentVal

if __name__ == "__main__":
    instr = ""
    while not instr.isdigit():
        instr = input("Provide target: ")

    print(findTarget(int(instr)))
