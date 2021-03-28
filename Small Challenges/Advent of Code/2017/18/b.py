import sys

class Program:

    def __init__(self, progNum):
        self.id = progNum
        self.reg = {'p': progNum}
        self.instr = 0
        self.toRcv = []
        self.sendCount = 0

    def __repr__(self):
        return str(self.reg)

    def __int__(self):
        return self.instr

    def getID(self):
        return self.id

    def addRcv(self, num):
        self.toRcv.append(num)

    def addReg(self, key, val):
        self.reg[key] = val

    def keepRcv(self, target):
        self.reg[target] = self.toRcv.pop(0)

    def getSendCount(self):
        return self.sendCount

    def getInstr(self):
        return self.instr

    def getRcv(self):
        return self.toRcv

    def incInstr(self):
        self.instr += 1

    def incCount(self):
        self.sendCount += 1

    def getReg(self):
        return self.reg

    def processInstr(self, line):
        try:
            line[2] = int(line[2])
        except ValueError:
            line[2] = self.reg[line[2]]
        
        if line[0] == "set":
            self.reg[line[1]] = line[2]
        elif line[0] == "add":
            self.reg[line[1]] += line[2]
        elif line[0] == "mul":
            self.reg[line[1]] *= line[2]
        elif line[0] == "mod":
            self.reg[line[1]] %= line[2]

    def jmp(self, dist):
        try:
            self.instr += int(dist)
        except ValueError:
            self.instr += self.reg[dist]

    def isActive(self, limit):
        return self.instr >= 0 and self.instr < limit


def activeProgram(lst,target):
    for prog in lst:
        if prog.isActive(target):
            return True
    else:
        return False

if __name__ == "__main__":
    progMem = [Program(x) for x in range(2)]
    instrSet = open("data18.txt", "r").read().split("\n")
    switch = False


    while activeProgram(progMem, len(instrSet)):
        for prog in progMem:
            if prog.isActive(len(instrSet)):
                line = instrSet[prog.getInstr()].split()

                if line[0] == "rcv":
                    if len(prog.getRcv()) == 0:
                        if switch:
                            print(progMem[1].getSendCount())
                            sys.exit()
                        else:
                            switch = True
                            continue
                    else:
                        switch = False
                        prog.keepRcv(line[1])

                else:
                    switch = False
                    if line[1] not in prog.getReg():
                        prog.addReg(line[1], 0)

                    if line[0] == "snd":
                        try:
                            pushVal = int(line[1])
                        except ValueError:
                            pushVal = prog.getReg()[line[1]]

                        progMem[prog.getID()^1].addRcv(pushVal)
                        prog.incCount()
                    elif line[0] == "jgz":
                        try:
                            overVal = int(line[1])
                        except ValueError:
                            overVal = prog.getReg()[line[1]]
                            
                        if overVal > 0:
                            prog.jmp(line[2])
                            continue
                    else:
                        prog.processInstr(line)
                    
                prog.incInstr()
            elif prog.getID() == 1:
                print(progMem[1].getSendCount())
                sys.exit()
                
    print(progMem[1].getSendCount())
    
    '''rcvFlag = False
    while True:
        for prog in range(len(progMrk)):
            line = instrSet[progMrk[prog]].split()
            
            # Add a new register with value 0
            if line[1] not in progMem[prog].keys():
                progMem[prog][line[1]] = 0

            # Replace reference to register with its value (predicate only)
            if len(line) > 2 and not line[2].isdigit() and line[2][0] != '-':
                line[2] = progMem[prog][line[2]]

            # Check instruction
            if line[0] == "jgz":
                if True:
                    #print("Jumped ({})".format(progMem[currProg][line[1]]))
                    progMrk[prog] += int(line[2]) - 1
            elif line[0] == "snd":
                send1Count += 1 if prog == 1 else 0
                try:
                    toRcv[prog^1].append(int(line[1]))
                except ValueError:
                    toRcv[prog^1].append(progMem[prog][line[1]])
            elif line[0] == "rcv":
                if len(toRcv[prog]) == 0:
                    if rcvFlag:
                        print(send1Count)
                        sys.exit()
                    else:
                        rcvFlag = True
                        continue
                else:
                    progMem[prog][line[1]] = toRcv[prog].pop(0)
            else:
                processInstr(line, progMem[prog])

            rcvFlag = False
            progMrk[prog] += 1
            if progMrk[prog] < 0 or progMrk[prog] >= len(instrSet):
                if prog == 1:
                    print(send1Count)
                    sys.exit()
                else:
                    progMrk.pop(0)
'''
