from definitions import *

D_SKIP_INSTRS = ["addr", "addi", "mulr", "muli"]

if __name__ == "__main__":
    name_map = {unord[key]:key for key in unord.keys()} # Reverse dict

    # Skip Vals
    skip_lst = []
    skip_override = [5,6,7]
    # Since instr incrementing will pass over the IP assignment
    instr_list = {} # List of instructions (numbered from 0)

    # Parse input
    doc = open("input.txt")
    counter = 0 # Instr number counter
    line = doc.readline()
    ipreg = int(line.split()[1])
    line = doc.readline()
    while line != "":
        parts = line.split()

        # Instruction: add to instr_list and increment counter
        instr_list[counter] = tuple([parts[0]] + [int(val)
                                                for val in parts[1:]])
                    
        line = doc.readline()
        if line != "":
            if line.split()[0] not in D_SKIP_INSTRS and line.split()[-1] == parts[-1]:
                skip_lst.append(counter)

        counter += 1
    # END WHILE

    # Main loop
    reg = [0 for i in range(6)] # registers
    reg[0] = 1 # Set reg 0 to 1
    limit = len(instr_list) # Limit of instructions, since list is constant

    # Analysis section. After analysis, it was found that the output would be
    # the sum of factors for whatever is in register 4 once register 2 was hit
    '''
    while reg[ipreg] < limit:
        ptrval = reg[ipreg] # Instruction number to do
        instr = instr_list[ptrval]
        print(ptrval)
        print(reg)
        #if ptrval not in skip_override and (ptrval not in skip_lst and instr[-1] == ipreg):
        if ptrval == 2:
            reg[2] = reg[4]
            reg[5] = reg[4] + 1
            reg[1] = 1
            reg[3] = 15

            # Otherwise, get instruction, get result, place in result reg, inc IP
        else:
            if reg[1] == reg[4]:
                print("hit")
            result = get_theo(name_map[instr[0]], reg, instr)
            reg[instr[-1]] = result
            
        reg[ipreg] += 1
        
    print(reg[0])'''

    # Section for printing answer
    while reg[ipreg] < limit:
        ptrval = reg[ipreg] # Instruction number to do
        instr = instr_list[ptrval]

        # Determine answer from analysis
        if ptrval == 2:
            total = 0
            # Up to square root
            for factor in range(1, int(pow(reg[4], 0.5))):
                if reg[4] % factor == 0:
                    total += factor + reg[4] // factor

            print(total)
            break
        else: # Continue simulation
            result = get_theo(name_map[instr[0]], reg, instr)
            reg[instr[-1]] = result
            reg[ipreg] += 1
