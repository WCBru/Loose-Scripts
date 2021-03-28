if __name__ == "__main__":
    prog = open("input.txt").read().strip().split("\n")
    flags = [False for line in prog]

    accum = 0
    line = 0

    while not flags[line]:
        flags[line] = True
        instr, val = prog[line].split()
        if instr == "acc":
            accum += int(val)
            line += 1
        elif instr == "jmp":
            line += int(val)
        elif instr == "nop":
            line += 1
        else:
            raise Exception(instr + " not recognised")

    print(accum)
