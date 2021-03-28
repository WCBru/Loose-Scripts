class Particle:
    
    def __init__(self, instr, ID):
        self.ID = ID
        line = instr.split(", ")
        prop = []
        for segNum in range(3):
            prop.append(line[segNum][3:-1])
        self.pos = processCoords(prop[0])
        self.vel = processCoords(prop[1])
        self.acc = processCoords(prop[2])

    def advTime(self):
        self.vel = elmAdd(self.vel, self.acc)
        self.pos = elmAdd(self.pos, self.vel)
        return self.pos

    def getDist(self):
        return sum([abs(coord) for coord in self.pos])

    def getAcc(self):
        return sum([abs(coord) for coord in self.acc])

    def getVel(self):
        return sum([abs(x) for x in self.vel])


def processCoords(line):
    return [int(coord) for coord in line.split(',')]

def elmAdd(lst1, lst2):
    if len(lst1) != len (lst2):
        print("List lengths don't match!")
        return lst1
    else:
        return [lst1[x] + lst2[x] for x in range(len(lst1))]

if __name__ == "__main__":
    inList = open("data20.txt")
    inStr = inList.readline().strip()
    partList = []
    idNo = 0
    while inStr != "":
        partList.append(Particle(inStr, idNo))
        inStr = inList.readline().strip()
        idNo += 1

    for x in range(10000):
        toRemove = []
        visited = {}
        for part in partList:
            partLoc = tuple(part.pos)
            if partLoc in visited.keys():
                toRemove.append(part.ID)
                toRemove.append(visited[partLoc])
            else:
                visited[partLoc] = part.ID

        newList = []
        for part in partList:
            if part.ID not in toRemove:
                newList.append(part)
        
        partList = newList
        for part in partList:
            part.advTime()

    print(len(partList))
