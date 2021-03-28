# could use eval() but that seems to be an unasfe habit
import sys

def evalCond(pred, regVal):
    if pred[0] == "==":
        return regVal == int(pred[1])
    elif pred[0] == ">=":
        return regVal >= int(pred[1])
    elif pred[0] == "<=":
        return regVal <= int(pred[1])
    elif pred[0] == "!=":
        return regVal != int(pred[1])
    elif pred[0] == ">":
        return regVal > int(pred[1])
    elif pred[0] == "<":
        return regVal < int(pred[1])
    else:
        return None
    

def evalInc(instr):
    if instr == "dec":
        return -1
    else:
        return 1

if __name__ == "__main__":
    registers = {}
    data = open("data8.txt", "r")
    line = data.readline()
    while line.strip() != "":
        chunks = line.split()

        # check for new registers
        for reg in [chunks[0], chunks[4]]:
            if registers.get(reg) == None:
                registers[reg] = 0
        if evalCond(chunks[5:], registers[chunks[4]]):
            registers[chunks[0]] += evalInc(chunks[1]) * int(chunks[2])
        
        line = data.readline()
    regList = registers.keys()
    maxVal = -1000000 # a really low number
    for reg in regList:
        if registers[reg] > maxVal:
            maxVal = registers[reg]
    print(maxVal)
