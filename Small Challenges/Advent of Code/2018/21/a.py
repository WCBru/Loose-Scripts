from definitions import *

# Upon analysing the code, the code will exit at instr 28, 3 == 0
# reg[0] is, otherwise, never altered

if __name__ == "__main__":
    name_map = {unord[key]:key for key in unord.keys()} # Reverse dict
    instr_input = open("input.txt").read().strip().split("\n")
    ipreg = int(instr_input[0].split()[1]) # IP register

    # Init registers and set of instructions
    reg = [0 for i in range(6)]
    instr_set = {}

    # Create instruction list
    counter = 0
    for instr in instr_input[1:]:
        # Split into a tuple of parts
        parts = instr.strip().split()
        instr_set[counter] = tuple([parts[0]] + 
                              [int(part) for part in parts[1:]])
        counter += 1
    # End for

    # While still in limits of instr set
    limit = len(instr_set)
    while reg[ipreg] < limit:
        ptrval = reg[ipreg] # Instruction number to do

        # If it every hits this point, dump the number needed and break
        if ptrval == 28:
            print(reg[3])
            break

        # Otherwise, get instruction, get result, place in result reg, inc IP
        instr = instr_set[ptrval]
        result = get_theo(name_map[instr[0]], reg, instr)
        reg[instr[-1]] = result
        reg[ipreg] += 1
