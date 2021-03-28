def findManLength(target):
    inNum = target
    level = 1
    while level**2 < inNum:
        level+= 2
    upperLimit = level**2
    radialLength = int(level/2)
    currentLower = upperLimit
    lowerIncrements = 1
    while currentLower > inNum:
        currentLower -= radialLength
        lowerIncrements+= 1

    outerLength = inNum - currentLower

    total = ((-1)**lowerIncrements)*(inNum-currentLower)
    if lowerIncrements%2 == 1:
        total += radialLength

    return total+radialLength

if __name__ == "__main__":
    while True:
        instr = ""
        while not instr.isdigit():
            instr = input("Please provide input: ")
        print(findManLength(int(instr)))
