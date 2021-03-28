def isCaught(length, time):
    return time % ((length-1)*2) == 0

if __name__ == "__main__":
    dataFile = open("data13.txt", "r")
    line = dataFile.readline()
    totalSev = 0
    while line != "":
        lineData = line.split()
        layer = int(lineData[0][:-1])
        length = int(lineData[1])
        totalSev += layer*length if isCaught(length, layer) else 0
        line = dataFile.readline()

    print(totalSev)
