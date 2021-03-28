def isCaught(length, time):
    return time % ((length-1)*2) == 0

if __name__ == "__main__":
    dataFile = open("data13.txt", "r")
    line = dataFile.readline()
    data = {}
    while line != "": # put in each layer and its range
        lineData = line.split()
        data[int(lineData[0][:-1])] = int(lineData[1])
        line = dataFile.readline()

    delay = 10
    while True:
        for layer in data.keys():
            if isCaught(data[layer], delay+layer):
                delay+=1
                break
        else: # break if never caught
            break

    print(delay)
