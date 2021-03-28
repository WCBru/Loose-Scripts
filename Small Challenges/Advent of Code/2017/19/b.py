moves = {'u': (-1,0), 'l': (0, -1), 'd': (1,0), 'r': (0,1)}
compass = ['u', 'l', 'd', 'r']
symbols = ['|', '-', '|', '-']

def move(posn, directn):
    delta = moves[directn]
    return (posn[0] + delta[0], posn[1] + delta[1])
        
def getChar(posn, maze):
    return maze[posn[0]][posn[1]]

def atEnd(posn, origin, maze):
    wayBack = compass.index(origin)-2
    possibleDir = compass[:]
    possibleDir.pop(wayBack)
    for direc in possibleDir:
        try:
            if getChar(move(posn, direc), maze) != " ":
                return False
        except IndexError:
            pass
    else:
        return True
        
def findNewDirec(posn, direc, maze):
    dirIndex = compass.index(direc)
    for newDir in [compass[dirIndex - 2*x + 1] for x in range(1,3)]:
        newSq = move(posn, newDir)
        if getChar(newSq, maze) == symbols[compass.index(newDir)]:
            return newSq, newDir
    else:
        print("Problem finding new direction")
        return posn, direc
    
if __name__ == "__main__":
    maze = open("data19.txt", "r").read().split('\n')
    pos = (0, maze[0].index('|'))
    direc = 'd'
    steps = 1

    while not atEnd(pos, direc, maze):
        newSq = move(pos, direc)
        #print(pos)
        #print(getChar(newSq, maze))
        if getChar(newSq, maze) != " ":
            
            pos = newSq
        else:
            pos, direc = findNewDirec(pos, direc, maze)

        steps += 1

    print(steps)
