def createSeq(inStr):
    roundSeq = []
    for cell in range(len(inList)):
        roundSeq.append(ord(inList[cell]))
    roundSeq += [17,31,73,47,23]
    return roundSeq

def doHash(lst, start, length):
    outLst = lst[:]
    for ind in range(length):
        outLst[(start+length-1-ind)%len(lst)] = lst[(start+ind)%len(lst)]
    return outLst

def roundRobin(numList):
    outList = numList[:]
    currStart = 0
    skip = 0
    for x in range(64): #Run the round robin 64 times
        for order in roundSeq:
            outList = doHash(outList, currStart, order)
            currStart += (skip + order)%len(outList)
            skip+= 1
    return outList
	
def xorBlocks(robinLst):
    hashList = []
    for block in range(16):
        currentBlock = robinLst[block*16:(block+1)*16]
        resultant = 0
        for num in currentBlock:
            resultant ^= num
        hashList.append(resultant)
    return hashList

def blockToHex(hashList):
    outstr = ""
    for conden in hashList:
        charHex = hex(conden)
        if len(charHex) == 3: # make small numbers into 2 hex digits
            charHex = "0x0" + charHex[2]
        outstr += charHex[-2:]
    return outstr
	
	
if __name__ == "__main__":
    inList = open("data10.txt", "r").read()
    roundSeq = createSeq(inList)
    numList = [x for x in range(256)]

    numList = roundRobin(numList)
    hashList = xorBlocks(numList)
    outstr = blockToHex(hashList)

    print(outstr)
    # check that 16 hex chars are outputted
    print("32 Chars printed" if len(outstr) == 32 else
          "Wrong Number of Chars produced: " + str(len(outstr)))
