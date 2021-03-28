def findHighestIndex(lst):
    highest = 0
    for cell in range(len(lst)):
        if lst[cell] > lst[highest]:
            highest = cell
    return highest

def repeatParameters(data):
    cycleNum = 0
    pastConfigs = []
    currentConfig = data
    while currentConfig not in pastConfigs:
        pastConfigs.append(currentConfig[:])
        highIndex = findHighestIndex(currentConfig)
        toDistrib = currentConfig[highIndex]
        currentConfig[highIndex] = 0
        currentIndex = highIndex
        while toDistrib > 0:
            if currentIndex >= len(data)-1:
                currentIndex = 0
            else:
                currentIndex+=1
            currentConfig[currentIndex] += 1
            toDistrib -= 1
        cycleNum+= 1

    return (cycleNum, currentConfig)

def findRepeatConfig(data):
    return repeatParameters(data)[1]

def findNumCyclesForRepeat(data):
    return repeatParameters(data)[0]

if __name__ == "__main__":
    data = open("data6.txt", "r").read().strip().split()
    for cell in range(len(data)):
        data[cell] = int(data[cell])

    print(findNumCyclesForRepeat(findRepeatConfig(data)))
