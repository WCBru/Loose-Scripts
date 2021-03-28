from definitions import *

# Upon analysing the code, the code will skip the loop at instruction 18
# if it will enter the loop
# The answer is the last number in reg[3] at instr 28 before a repeat

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

    encountered = []
    counter= 0
    loop_capture = True
    loop_list = []
    # While still in limits of instr set
    limit = len(instr_set)
    while reg[ipreg] < limit:
        ptrval = reg[ipreg] # Instruction number to do

        # Loop at instruction 18
        if ptrval == 18:
            if reg[4] < reg[1] // 256:
                reg[2] = 1
                reg[4] = reg[1]//256
                reg[2] = 2
            else:
                reg[2] = reg[4]*256

            reg[5] = 22 # Skip to instr 23

        # Instr number to check answer
        # Answer is the last answer printed
        if ptrval == 28:
            if reg[3] not in encountered:
                print(reg[3])
                encountered.append(reg[3])
            else:
                print(encountered[-1])
                break

        # Otherwise, get instruction, get result, place in result reg, inc IP
        instr = instr_set[ptrval]
        result = get_theo(name_map[instr[0]], reg, instr)
        reg[instr[-1]] = result
        reg[ipreg] += 1
