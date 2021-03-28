import sys
def processInstr(line, reg, note):
    if len(line) > 2 and not line[2].isdigit() and line[2][0] != '-':
        line[2] = reg[line[2]]
    
    if line[0] == "snd":
        return reg[line[1]]
    elif line[0] == "set":
        reg[line[1]] = int(line[2])
    elif line[0] == "add":
        reg[line[1]] += int(line[2])
    elif line[0] == "mul":
        reg[line[1]] *= int(line[2])
    elif line[0] == "mod":
        reg[line[1]] %= int(line[2])
    else:
        print("instr not recognised: " + str(line))
    
    return note

if __name__ == "__main__":
    regMem = {}
    instrSet = open("data18.txt", "r").read().split("\n")
    lastNote = 0
    instr = 0
    while instr < len(instrSet):
        line = instrSet[instr].split()

        if line[1] not in regMem.keys():
            regMem[line[1]] = 0

        if line[0] == "jgz":
            if regMem[line[1]] >0:
                instr += int(line[2]) - 1               
        elif line[0] == "rcv":
             if regMem[line[1]] != 0:
                print("recovered: " + str(lastNote))
                sys.exit()
        else:
            lastNote = processInstr(line, regMem, lastNote)
        instr+= 1
    print(regMem)
