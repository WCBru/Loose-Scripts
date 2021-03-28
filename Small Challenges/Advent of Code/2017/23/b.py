# An ad hoc solution: manual analysis of the input used
# to optimize

# 1001 too high - there are occasions where sub h -1 is skipped
# for each d*e, if equal to b, f = 0
# so need to find a way to extract those values
# probably if, at the entrance of the loop, b%d > 1
def parseVal(num, data):
    if num in data:
        return data[num]
    else:
        return int(num)

def isPrime(num):
    for x in range(2,num):
        if num%x == 0:
            return False
    return True

if __name__ == "__main__":
    instrList = [line.split() for line in
                 open("data23op.txt", "r").read().split("\n")]
    reg = {chr(x):0 for x in range(97,105)}
    reg['a'] = 1
    currInstr = 0
    listLen = len(instrList)
    
    while currInstr >=0 and currInstr < listLen:
        
        line = instrList[currInstr]
        if currInstr == 10:
            if not isPrime(reg['b']):
                reg['f'] = 0
        
        if line[0] == "jnz" and parseVal(line[1], reg) != 0:
            currInstr += parseVal(line[2], reg)
            continue
        elif line[0] == "set":
            reg[line[1]] = parseVal(line[2], reg)
        elif line[0] == "sub":
            reg[line[1]] -= parseVal(line[2], reg)
        elif line[0] == "mul":
            reg[line[1]] *= parseVal(line[2], reg)

        currInstr += 1

    print(reg['h'])
    
