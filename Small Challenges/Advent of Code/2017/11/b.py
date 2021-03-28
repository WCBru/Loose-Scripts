oppositeMoves = [('ne', 'sw'), ('nw', 'se'), ('n', 's')]
tBear = ['n','ne','se','s','sw','nw']

def cancelOpposites(rawDict):
    outDict = rawDict
    for pair in oppositeMoves:
        vals = (rawDict.get(pair[0]), rawDict.get(pair[1]))
        for step in range(2):
            outDict[pair[step]] -= min(vals)
    return outDict

def condenseTriangles(rawDict):
    outDict = rawDict
    valueChange = True
    while valueChange:
        valueChange = False

        for direc in range(len(tBear)):
            if outDict.get(tBear[direc]) != 0 and outDict.get(tBear[direc-2]) != 0:
                valueChange = True
                vals = (outDict.get(tBear[direc]), outDict.get(tBear[direc-2]))
                
                for step in range(3):
                    outDict[tBear[direc-step]] -= ((-1)**step)*min(vals)
                
    return outDict

if __name__ == "__main__":
    rawInstr = open("data11.txt", "r").read().split(",")
    instrc = [] # Gradually records the whole path
    stepNos = []
    for instruction in rawInstr:
        instrc.append(instruction)
        instrDict = {direction:0 for direction in tBear}
        for instr in instrc:
            instrDict[instr] += 1
        instrDict = cancelOpposites(instrDict)
        instrDict = condenseTriangles(instrDict)

        total = 0
        for direc in instrDict.keys():
            total += instrDict[direc]
        stepNos.append(total)
    print(max(stepNos))
