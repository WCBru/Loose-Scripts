CYCLES = 6
DELTAS = [(1,0,0),(0,1,0),(0,0,1),
          (1,-1,0),(1,1,0),(1,0,-1),(1,0,1),(0,1,1),(0,1,-1),
          (1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)]
DELTAS += [tuple([-x for x in tup]) for tup in DELTAS]    

def getadj(pt):
    output = [None for x in range(len(DELTAS))]
    for d in range(len(DELTAS)):
        output[d] = (tuple([pt[i] + DELTAS[d][i] for i in range(len(pt))]))

    return output

def finddeltas(field):
    removal = set()
    emptyadd = set()
    emptyblank = set()
    for pt in field:
        adjcount = 0
        for adj in getadj(pt):
            if adj in field:
                adjcount += 1
            elif adj not in emptyadd and adj not in emptyblank:
                if sum([adj2 in field for adj2 in getadj(adj)]) == 3:
                    emptyadd.add(adj)
                else:
                    emptyblank.add(adj)

        if adjcount != 2 and adjcount != 3:
            removal.add(pt)

    return (removal, emptyadd)

if __name__ == "__main__":
    toadd = []
    for d in DELTAS:
        toadd.append((d[0], d[1], d[2], 0))
        toadd.append((d[0], d[1], d[2], -1))
        toadd.append((d[0], d[1], d[2], 1))

    toadd.append((0, 0, 0, 1))
    toadd.append((0, 0, 0, -1))

    DELTAS = toadd
    print(len(DELTAS))
    
    active = set()
    row = 0
    for line in open("input.txt").read().split("\n"):
        for char in range(len(line)):
            if line[char] == "#":
                active.add((row, char, 0, 0))
        row += 1

    for c in range(CYCLES):
        remove, add = finddeltas(active)
        for r in remove:
            active.remove(r)
        for a in add:
            active.add(a)
        print(c)

    print(len(active))
