DELTAS = [(1,0),(-1,0),(0,1),(0,-1)]

def getSrc(src):
    if src == "ch1":
        return """7 7
38  33  11  48  19  45  22
47  30  24  15  46  28   3
14  13   2  34   8  21  17
10   9   5  16  27  36  39
18  32  20   1  35  49  12
43  29   4  41  26  31  37
25   6  23  44   7  42  40
35"""
    elif src == "ch2":
        return """7 7
15  16  46   1  38  43  44
25  10   7   6  34  42  14
8  19   9  21  13  23  22
32  11  29  36   3   5  47
31  33  45  24  12  18  28
40  41  20  26  39  48   2
49  35  27   4  37  30  17
26"""
    else:
        return """3 3
1 9 6
2 8 5
3 7 4
4"""

def printBoard(board, tiles):
    # Make a copy of the board
    copy = []
    for row in board:
        copy.append(row[:])

    # Make each contained tile an X
    for tile in tiles:
        copy[tile[0]][tile[1]] = "X"

    # Print each row
    for row in copy:
        print('\t'.join([str(elm) for elm in row]))

def getTile(coord, prob):
    return prob[coord[0]][coord[1]]

def getStart(problem):
    for row in range(len(problem)):
        for col in range(len(problem[row])):
            if problem[row][col] == 1:
                return (row, col)

def getLeaves(dim, contained, prob):
    output = []
    for core in contained:
        for delta in DELTAS:
            newCoord = (core[0]+delta[0], core[1] + delta[1])
            if (all([newCoord[i] < dim[i] and newCoord[i] >= 0 for i in range(2)])
                and newCoord not in contained and newCoord not in output):
                   output.append((newCoord, getTile(newCoord, prob)))
    #print(output)
    return [val[0] for val in sorted(output, key = lambda x : x[1])]
                    
# Recursive function
def timeToTarget(prob, dim, top, goal, start):
    contained = [start]
    additionalTime = 0
    waterLevel = getTile(start, prob)
    while all([getTile(tile, prob) != top for tile in contained]):
        lowLeaf = getLeaves(dim, contained, prob)[0] # Get lowest Leaf
        lowTile = getTile(lowLeaf, prob)
        #printBoard(prob, contained)
        #print("Time " + str(additionalTime))
        #print("Evaluating " + str(lowTile))
        #print(contained)

        if (waterLevel > goal and any([getTile(val, prob) == goal for val in contained])):
            return (additionalTime, contained)
            
        if lowTile < waterLevel: # Should be in ascending order:
            # Get the additional fill tiles and time
            moreTime, moreTiles = timeToTarget(prob,dim,waterLevel,goal,lowLeaf)
            #print(moreTime)
            #print(moreTiles)
            
            # Add the time and tiles
            additionalTime += moreTime
            contained = contained[:-1] + moreTiles + [contained[-1]] # keep last element the same
            #if any([getTile(val, prob) == goal for val in contained])):
            #    return (additionalTime, contained)
            #else: # 2nd last element is duplicate of last element
            if len(moreTiles) > 1: # Don't pop second last if the list is only 1 element long
                contained.pop(-2)
        elif lowTile > goal and any([getTile(val, prob) == goal for val in contained]):
            waterLevel += 1
            additionalTime += len(contained) # Rise 1 level
        else:
            #print(len(contained)*(lowTile - waterLevel))
            additionalTime += len(contained)*(lowTile - waterLevel)# Calculate additional Time
            waterLevel = lowTile
            contained.append(lowLeaf) # Add the next lowest tile
    else:
        return (additionalTime, contained)

if __name__ == "__main__":
    lines = getSrc("ch2").split("\n")
    rows, cols = [int(dim) for dim in lines[0].strip().split(" ",2)]
    target = int(lines[-1].strip())

    grid = [[int(num) for num in line.strip().split()] for line in lines[1:-1]]

    endInfo = timeToTarget(grid, (rows, cols), target + 1, target, getStart(grid))

    print(endInfo[0])
    printBoard(grid, endInfo[1])
