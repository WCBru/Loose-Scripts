from definitions import *

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

if __name__ == "__main__":
    clues = get_clues("input.txt")

    match_list = []
    '''matches = {}'''
    for clue in clues:
        ''' Code for keeping track of invidual numbers
        opcode = clue[1][0]
        if opcode not in matches.keys():
            matches[opcode] = [num for num in range(16)] # 0 - 15

        
        # Check if the in/out of the operation matches what is given
        new_lst = []
        for operation in matches[opcode]:
            try:                
                if get_theo(operation, clue[0], clue[1]) == clue[2][clue[1][-1]]:     
                    new_lst.append(operation)
            except IndexError:
                pass
        # END FOR
        
        matches[opcode] = new_lst'''

        # Count the number of matches for all 16 opcodes
        matches = 0
        for code in range(16):
            # Check if theoretical outcome is the same as the output given
            if get_theo(code, clue[0], clue[1]) == clue[2][clue[1][-1]]:
                matches += 1
        match_list.append(matches)
    # END FOR

    print(sum([ int(num > 2) for num in match_list ]))
