def checkReg(instr, data):
    for pred in [1,2]:
        try:
            int(instr[pred])
        except ValueError:
            if instr[pred] not in data:
                data[instr[pred]] = 0

def parseVal(num, data):
    try:
        return int(num)
    except ValueError:
        return data[num]

if __name__ == "__main__":
    instrList = [line.split() for line in
                 open("data23.txt", "r").read().split("\n")]
    reg = {}
    currInstr = 0
    listLen = len(instrList)
    mulCount = 0
    
    while currInstr >=0 and currInstr < listLen:
        line = instrList[currInstr]
        checkReg(line, reg)

        if line[0] == "jnz":
            if parseVal(line[1], reg) != 0:
                currInstr += parseVal(line[2], reg)
                continue
        elif line[0] == "set":
            reg[line[1]] = parseVal(line[2], reg)
        elif line[0] == "sub":
            reg[line[1]] -= parseVal(line[2], reg)
        elif line[0] == "mul":
            reg[line[1]] *= parseVal(line[2], reg)
            mulCount += 1
        currInstr += 1
        
    print(mulCount)
    
