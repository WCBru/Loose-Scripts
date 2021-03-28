from definitions import *

INPUT_NAME = "input.txt"

# Parse input into a 3-tuple containing 4-tuples
# Before, instruction and resultant registers
def get_clues(doc_name):
    doc = open(doc_name).read().split("\n\n")
    output = []

    # For each segment: double newline
    for seg in doc:
        # Split into individual lines
        parts = seg.split("\n")
        if len(parts) != 3:
            continue

        # Before: Take part after "[" and split by ", "
        before = parts[0].strip().split("[")[1].split(", ")
        before[-1] = before[-1][:-1] # remove final ]
        before = tuple([int(num) for num in before]) # to int tuple

        code = tuple([int(num) for num in parts[1].split()])

        # Take part after "[" and split by ", "
        after = parts[2].strip().split("[")[1].split(", ")
        after[-1] = after[-1][:-1] # remove final ]
        after = tuple([int(num) for num in after]) # to int tuple
        
        output.append((before, code, after))
    
    return output

# Get the number of exact instances of the target list (order independent)
# In the values of the base argument
def get_insts(base, target):
    count = 0
    for key in base.keys():
        # Check for length and all elements of target in the list tested
        if (all([val in base[key] for val in target])
            and len(base[key]) == len(target)):
            
            count += 1
    return count

if __name__ == "__main__":
    clues = get_clues(INPUT_NAME)

    # Process each opcode to determine which number maps to each opcode
    matches = {num: [val for val in range(16)] for num in range(16)}
    for clue in clues:
        opcode = clue[1][0] # OP code to test
        
        # Check if the in/out of the operation matches what is given
        new_lst = []
        for operation in matches[opcode]:
            try: # Catches index errors, if immediate value > 3
                # Test theoretical vs given value
                if get_theo(operation, clue[0], clue[1]) == clue[2][clue[1][-1]]:     
                    new_lst.append(operation)
            except IndexError:
                pass
        # END FOR
        
        matches[opcode] = new_lst
    # END FOR

    deduction_made = False
    # Loop to make deductions
    while any( [len(matches[key]) > 1 for key in matches.keys() ] ):
        # Throw error if anything has no map to value
        if any( [len(matches[key]) == 0 for key in matches.keys()] ):
            raise ValueError("Code {0} has no match".format(code))

        # Deduction loop. Iterate over possible deduction lengths
        max_length = max([len(matches[key]) for key in matches.keys()])

        for length in range(1, max_length):
            # For each length, then iterate through all mappings
            for code in matches.keys():
                # If it matches the current length being tested
                if len(matches[code]) == length:
                    # Check if the number of occurances of that match is equal
                    # to its length. This means that anything than the current
                    # length cannot contain the segment being matched
                    kernel = matches[code]
                    if get_insts(matches, kernel) == length:
                        # Loop for removing the matching elements in arrays
                        # where the kernel is a proper subset
                        for code2 in matches.keys():
                            if (len(matches[code2]) > length
                                and all([val in matches[code2]
                                         for val in kernel])):
                                # Small loop for removing the deduced values
                                [matches[code2].remove(val) for val in kernel]
                                deduction_made = True # Deduction made flag

        # If nothing changed, break
        if not deduction_made:
            break

        deduction_made = False

    # Deductions complete - simulate last part of input
    else:
        # Convert 1 elm list to int
        for key in matches.keys():
            matches[key] = matches[key][0]
        
        registers = [0,0,0,0] # Init registers
        section = open(INPUT_NAME).read().strip().split("\n\n")[-1] # Read inp.

        # Go through each instruction (i.e. each line
        for line in section.split("\n"):
            # Convert each line into a 4-tuple
            instr = tuple([int(val) for val in line.split()])

            # Use the get_theo function to get a value for the current instruc
            result = get_theo(matches[instr[0]], registers, instr)

            # Store the result in the last part of the instruction
            registers[instr[-1]] = result
        # END FOR LOOP FOR SIMULATION

        print(registers[0])
