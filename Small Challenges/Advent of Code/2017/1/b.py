if __name__ == "__main__":
    instr = ""
    while not instr.isdigit():
        instr = input().strip()
    total = 0
    wrap = int(len(instr)/2)
    for digit in range(len(instr)):
        if instr[digit] == instr[digit-wrap]:
            total += int(instr[digit])

    print(total)
