def direction(instr):
    if instr == "left":
        return -1
    elif instr == "right":
        return 1
    else:
        return 0

def processLetter(letter, dct, src):
    for x in range(2):
        src.readline()
        wr = int(src.readline().split()[-1][:-1])
        direc = int(direction(src.readline().split()[-1][:-1]))
        st = src.readline().split()[-1][:-1]
        dct[letter].append((wr, direc, st))

    src.readline()
    

if __name__ == "__main__":
    inStr = open("data25.txt", "r")
    
    states = {chr(x):[] for x in range(65, 71)}
    tape = [0]
    
    currState = inStr.readline().split()[-1][:-1]
    currPos = 0
    steps = int(inStr.readline().split()[-2])
    inStr.readline()
    line = inStr.readline()
    while line != "":
        processLetter(line.split()[-1][:-1], states, inStr)
        line = inStr.readline()

    for x in range(steps):
        action = states[currState][tape[currPos]]
        if currPos == 0 and action[1] == -1:
            currPos += 1
            tape.insert(0, 0)
        elif currPos == len(tape) - 1 and action[1] == 1:
            tape.append(0)

        tape[currPos] = action[0]
        currPos += action[1]
        currState = action[2]

    print(sum(tape))
