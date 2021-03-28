def read_in_input(name):
    doc = open(name)
    line = doc.readline()
    out_dict = {}

    while line != "":
        before, after = line.split()[1::6] # 1st to end, w/ step size 6

        # Add letters if not present in dict
        if before not in out_dict.keys():
            out_dict[before] = []

        if after not in out_dict.keys():
            out_dict[after] = []

        # Add pre-req to list
        out_dict[after].append(before)
        
        line = doc.readline()

    return out_dict

if __name__ == "__main__":
    prereq_dict = read_in_input("input.txt")

    alpha_list = sorted(prereq_dict.keys()) # Assumes same case
    order = []

    # Continue until step list completed
    while len(order) < len(prereq_dict):
        for letter in alpha_list: # Iterate through each letter

            # If all pre-reqs satisfied, and letter isn't already done
            if (all([let in order for let in prereq_dict[letter]])
                and letter not in order):

                # Add letter, move on
                order.append(letter)
                break
        else: # If all steps are either done or unreachable
            raise IndexError("Could not find next step")

    print("".join(order)) # Turn into single string
