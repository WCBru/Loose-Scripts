if __name__ == "__main__":
    programs = [char for char in input().strip()]
    original = programs[:]
    instructions = input().strip().split(',')
    for instr in instructions:
        if instr[0] == 's':
            amount = int(instr[1:])
            programs = programs[-1*amount:] + programs[:len(programs)-amount]
        elif instr[0] == 'x':
            target = [int(num) for num in instr[1:].split('/')]
            programs[target[0]], programs[target[1]] = (programs[target[1]],
                                                        programs[target[0]])
        elif instr[0] == 'p':
            originalIndex = [int(num) for num in instr[1:].split('/')]
            target = [original.index(programs[num])
                      for num in originalIndex]
            programs[target[0]], programs[target[1]] = (programs[target[1]],
                                                       programs[target[0]])
        else:
            print("Instruction not recognised: " + instr)

    print("".join(programs))
