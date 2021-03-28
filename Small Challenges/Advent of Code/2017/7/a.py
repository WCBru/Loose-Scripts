if __name__ == "__main__":
    indata = open("data7.txt", "r")
    parentList = {}
    data = indata.readline()
    while data != "":
        rawdata = data.split()
        name = rawdata[0]
        if len(rawdata) > 2:
            children = rawdata[3:]
            for child in children:
                if child[-1] == ",":
                    child = child[:-1]
                parentList[child] = name
        
        data = indata.readline()
    #print(parentList)
    children = parentList.keys()
    for child in children:
        if parentList[child] not in children:
            print(parentList[child])
            break
