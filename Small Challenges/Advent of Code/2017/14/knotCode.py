def createSeq(inStr):
    outLst = []
    for cell in range(len(inStr)):
        outLst.append(ord(inStr[cell]))
    outLst += [17,31,73,47,23]
    return outLst

def doHash(lst, start, length):
    outLst = lst[:]
    for ind in range(length):
        outLst[(start+length-1-ind)%len(lst)] = lst[(start+ind)%len(lst)]
    return outLst

def roundRobin(inList, seq):
    outList = inList[:]
    currStart = 0
    skip = 0
    for x in range(64): #Run the round robin 64 times
        for order in seq:
            outList = doHash(outList, currStart, order)
            currStart += (skip + order)%len(outList)
            skip+= 1
    return outList
	
def xorBlocks(robinLst):
    outLst = []
    for block in range(16):
        currentBlock = robinLst[block*16:(block+1)*16]
        resultant = 0
        for num in currentBlock:
            resultant ^= num
        outLst.append(resultant)
    return outLst

def blockToHex(inList):
    outstr = ""
    for conden in inList:
        charHex = hex(conden)
        if len(charHex) == 3: # make small numbers into 2 hex digits
            charHex = "0x0" + charHex[2]
        outstr += charHex[-2:]
    return outstr
	
def fullKnot(seq):
    return blockToHex(xorBlocks(roundRobin([x for x in range(256)], seq)))
	
if __name__ == "__main__":
    inList = open("data10.txt", "r").read()
    roundSeq = createSeq(inList)

    outStr = fullKnot(roundSeq)
    print(outStr)
    # check that 16 hex chars are outputted
    print("32 Chars printed" if len(outStr) == 32 else
          "Wrong Number of Chars produced: " + str(len(outstr)))
