from definitions import *

if __name__ == "__main__":
    name_map = {unord[key]:key for key in unord.keys()} # Reverse dict

    # List of IP assignments. Assigned before corrosponding instruction
    # Since instr incrementing will pass over the IP assignment
    ip_list = {}
    instr_list = {} # List of instructions (numbered from 0)

    # Parse input
    doc = open("input.txt")
    counter = 0 # Instr number counter
    line = doc.readline()
    while line != "":
        parts = line.split()

        # IP Assignment line. No counting used
        if parts[0] == "#ip":
            ip_list[counter] = int(parts[1])
        else: # Instruction: add to instr_list and increment counter
            instr_list[counter] = tuple([parts[0]] + [int(val)
                                                    for val in parts[1:]])
            counter += 1
            
        line = doc.readline()
    # END WHILE

    # Main loop
    ipreg = 0 # Register of current IP value
    reg = [0 for i in range(6)] # registers
    limit = len(instr_list) # Limit of instructions, since list is constant

    # While still inside list
    while reg[ipreg] < limit:
        ptrval = reg[ipreg] # Instruction number to do

        # Check if IP Ptr needs to move
        if ptrval in ip_list.keys():
            ipreg = ip_list[ptrval]

        # Otherwise, get instruction, get result, place in result reg, inc IP
        instr = instr_list[ptrval]
        result = get_theo(name_map[instr[0]], reg, instr)
        reg[instr[-1]] = result
        reg[ipreg] += 1

    print(reg[0])
