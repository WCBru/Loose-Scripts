def doHash(lst, start, length):
    outLst = lst[:]
    for ind in range(length):
        outLst[(start+length-1-ind)%len(lst)] = lst[(start+ind)%len(lst)]
    return outLst

if __name__ == "__main__":
    inList = open("data10.txt", "r").read().split(',')
    for cell in range(len(inList)):
        inList[cell] = int(inList[cell]) # order list
    hashList = [num for num in range(256)] # big list
    currStart = 0
    for order in range(len(inList)):
        hashList = doHash(hashList, currStart, inList[order])
        currStart += (order + inList[order])%len(hashList)

    #stuff here
    print(hashList[0]*hashList[1])
