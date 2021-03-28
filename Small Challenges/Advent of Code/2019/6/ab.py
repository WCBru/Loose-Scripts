if __name__ == "__main__":
    parentMap = {}
    file = open("input.txt")
    line = file.readline()

    while line != "":
        lineParts = line.strip().split(")")
        parentMap[lineParts[1]] = [lineParts[0]]
        line = file.readline()

    file.close()

    for child in parentMap.keys():
        nextParent = parentMap.get(parentMap.get(child)[0])
        while nextParent != None:
            parentMap[child].append(nextParent[0])
            nextParent = parentMap.get(nextParent[0])

    print(sum([len(parentMap[child]) for child in parentMap.keys()]))

    for san in range(len(parentMap["SAN"])):
        for you in range(len(parentMap["YOU"])):
            if parentMap["SAN"][san] == parentMap["YOU"][you]:
                print(san + you)
                raise Exception("Done")
