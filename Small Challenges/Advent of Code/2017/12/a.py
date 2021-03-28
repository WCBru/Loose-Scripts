if __name__ == "__main__":
    fileLines = open("data12.txt", "r").read().split('\n')
    inData = {}
    for line in fileLines:
        data = line.split(' <-> ')
        inData[int(data[0])] = [int(child) for child in data[1].split(', ')]

    explored = [0]
    stack = [num for num in inData[0]]
    while len(stack) != 0:
        currNode = stack.pop()
        explored.append(currNode)
        for child in inData[currNode]:
            if child not in explored:
                stack.append(child)

    print(len(explored))
