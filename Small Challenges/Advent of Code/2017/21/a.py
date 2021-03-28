def copyList(inList):
    outList = []
    for lst in inList:
        outList.append(lst[:])
    return outList

def convertToList(string):
    return [[char for char in line] for line in string.split("/")]

def size(patx):
    return len(patx.split("/")[0])

def convertToString(lst):
    outStr = "".join(lst[0])
    for line in lst[1:]:
        outStr += "/" + "".join(line)
    return outStr

def printLst(lst):
    for row in lst:
        print(row)

def getRotated(pattern):
    patsize = size(pattern)
    ori = convertToList(pattern)
    current = copyList(ori)
    outList = [pattern]
    for x in range(3):
        for row in [0, patsize-1]:
            for elm in range(patsize):
                current[row][elm] = ori[patsize-1-elm][row]
        if patsize == 3:
            current[1][2] = ori[0][1]
            current[1][0] = ori[2][1]
        outList.append(convertToString(current))
        ori = copyList(current)

    return outList

def getFlipped(src):
    outList = []
    pList = convertToList(src)
    outList.append(src)
    current = copyList(pList)
    current[0] = pList[size(src)-1]
    current[size(src)-1] = pList[0]
    outList.append(convertToString(current))

    current = copyList(pList)
    cols = [0, size(src)-1]
    for col in range(2):
        for row in range(size(src)):
            current[row][cols[col]] = pList[row][cols[col-1]]
    outList.append(convertToString(current))
    return outList

def checkMatch(pat, rules):
    for rot in getRotated(pat):
        for flip in getFlipped(rot):
            if flip in rules:
                return rules[flip]
                
    raise IndexError

def segpiece(pato, rules, modu):
    length = size(pato)
    offsets = {}
    patList = convertToList(pato)
    numSeg = int(length/modu)
    for row in range(numSeg):
        for col in range(numSeg):
            subList = patList[row*modu:(row+1)*modu]
            for elm in range(len(subList)):
                subList[elm] = subList[elm][col*modu:(col+1)*modu]
            offsets[(row, col)] = checkMatch(convertToString(subList), rules)
    
    outList = [['x' for x in range(length+numSeg)] for y in range(length+numSeg)]
    for orow, ocol in offsets:
        lst = convertToList(offsets[(orow, ocol)])
        for row in range(modu+1):
            for col in range(modu+1):
                outList[row+(modu+1)*orow][col+(modu+1)*ocol] = lst[row][col]
    
    return convertToString(outList)

if __name__ == "__main__":
    rule2 = {}
    rule3 = {}
    rules = open("data21.txt", "r")
    cRule = rules.readline().strip()
    while True:
        seg = cRule.split()
        if len(seg[0]) == 5:
            rule2[seg[0]] = seg[2]
        elif len(seg[0]) == 11:
            rule3[seg[0]] = seg[2]
        else:
            print("Error: Rule Length Mismatch")
        cRule = rules.readline().strip()
        if cRule == "":
            break

    currPat = ".#./..#/###"
    
    for x in range(5):
        pSize = size(currPat)
        if pSize % 2 == 0:
            currPat = segpiece(currPat, rule2, 2)
        elif pSize % 3 == 0:
            currPat = segpiece(currPat, rule3, 3)
        else:
            print("Incompatible Size")
    total = 0
    for char in currPat:
        if char == "#":
            total += 1
    print(total)
