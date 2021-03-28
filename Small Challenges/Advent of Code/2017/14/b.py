import knotCode as kHash

def oneAtPosn(posn, src):
    if posn[0] < 0 or posn[1] < 0:
        return False
    try:
        return src[posn[0]][posn[1]] == '1'
    except IndexError:
        return False

def wipeRegion(posn, grid):
    outGrid = grid[:]
    stack = [posn]
    while len(stack) != 0:
        #print(stack)
        current = stack.pop()
        
        if oneAtPosn(current, outGrid):
            outGrid[current[0]][current[1]] = '0'
            for row, col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newPosn = (current[0]+row, current[1]+col)
                    if oneAtPosn(newPosn, outGrid):
                        stack.append(newPosn)
            
    return outGrid

if __name__ == "__main__":
    keyStr = input("Enter key: ").strip()
    fragGrid = []
    regionKeys = []
    numReg = 0

    #Grid Constructor
    for row in range(128):
        roundSeq = kHash.createSeq(keyStr + "-" + str(row))
        hexChars = kHash.fullKnot(roundSeq)
        row = []
        for char in hexChars:
            bite = []
            for digit in str(bin(int(char, 16)))[2:]:
                
                bite.append(digit)
            while len(bite) < 4:
                bite.insert(0, '0')
            row+= bite
        fragGrid.append(row)
    print("Grid generated")
    
    #Region Finder
    for row in range(128):
        for col in range(128):
            if oneAtPosn((row,col), fragGrid):
                fragGrid = wipeRegion((row,col), fragGrid)
                numReg+= 1

    print("Number of Regions: {}".format(numReg))
