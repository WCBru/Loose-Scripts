if __name__ == "__main__":
    instr = ""
    while not instr.isdigit():
        instr = input().strip()
    total = 0
    for digit in range(len(instr)):
        if instr[digit] == instr[digit-1]:
            total += int(instr[digit])

    print(total)
