if __name__ == "__main__":
    fileLines = open("data12.txt", "r").read().split('\n')
    inData = {}
    for line in fileLines:
        data = line.split(' <-> ')
        inData[int(data[0])] = [int(child) for child in data[1].split(', ')]

    explored = []
    stack = []
    grpCount = 0

    for nth in range(len(inData)):
        if nth not in explored:
            grpCount+= 1
            explored.append(nth)
            stack = [num for num in inData[nth]]
            while len(stack) != 0:
                currNode = stack.pop()
                explored.append(currNode)
                for child in inData[currNode]:
                    if child not in explored:
                        stack.append(child)

    print(grpCount)
