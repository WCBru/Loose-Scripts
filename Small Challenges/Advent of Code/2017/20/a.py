# Answer is in the list: 344
# To change script once I stop  using Vim

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

    def __repr__(self):
        return str(self.ID)

    def advTime(self):
        self.vel = elmAdd(self.vel, self.acc)
        self.pos = elmAdd(self.pos, self.vel)

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

def findLowestIndex(nums):
    minNum = lst(nums.keys())[0]
    for num in nums.keys():
        if num < minNum:
            minNum = num

    return minNum

def findLowestList(nums):
    out = {}
    minimum = min([nums[key] for key in nums.keys()])
    for num in nums.keys():
        if nums[num] == minimum:
            out[num] = nums[num]
        
    return out

if __name__ == "__main__":
    inList = open("data20.txt")
    inStr = inList.readline().strip()
    partList = []
    idNo = 0
    while inStr != "":
        partList.append(Particle(inStr, idNo))
        inStr = inList.readline().strip()
        idNo += 1

    accs = findLowestList({part.ID: part.getAcc() for part in partList})
    if len(accs) > 1:
        accs = findLowestList({partList[ind].ID: partList[ind].getVel() for ind in accs.keys()})
    if len(accs) > 1:
        accs = findLowestList({partList[ind].ID: partList[ind].getDist() for ind in accs.keys()})
    

    minIndex = list(accs.keys())[0]
    print(accs) 
    print(minIndex)
