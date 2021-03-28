def run(prog):
    flags = [False for line in prog]
    accum = 0
    line = 0

    while line < len(prog) and not flags[line]:
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

    return (accum, line)

if __name__ == "__main__":
    prog = open("input.txt").read().strip().split("\n")

    for line in range(len(prog)):
        originalLine = prog[line]
        instr, val = prog[line].split()
        if instr == "jmp":
            prog[line] = "nop " + val
        elif instr == "nop":
            prog[line] = "jmp " + val
        accum, lineOut = run(prog)

        if lineOut == len(prog):
            print(accum)
            break
        else:
            prog[line] = originalLine
