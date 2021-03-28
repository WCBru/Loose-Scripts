TIME_CONSTANT = 60

# Reads in the input doc and creates a dict of prerequisite steps
def read_in_input(name):
    doc = open(name)
    line = doc.readline()
    out_dict = {}

    # Read in line-by-line
    while line != "":
        # Get the two letters in each statement
        before, after = line.split()[1::6] # 1st to end, w/ step size 6

        # Add letters if not present in dict
        if before not in out_dict.keys():
            out_dict[before] = []

        if after not in out_dict.keys():
            out_dict[after] = []

        # Add pre-req to list
        out_dict[after].append(before)
        
        line = doc.readline() # Read next line
    # End while loop
    
    return out_dict

# Calculate the time for a given step
# Assumes capital letter given
def time_for_step(cap_letter):
    return TIME_CONSTANT + (ord(cap_letter) - 64)

# Returns if all the pre-requisites have been completed for a given target
def step_available(prereqs, completed, target):
    return all([let in completed for let in prereqs[target]])

if __name__ == "__main__":
    prereq_dict = read_in_input("input.txt")
    alpha_list = sorted(prereq_dict.keys()) # Assumes same case

    # Variables relevant to order completion
    order = [] # Final order
    pending = {} # In-progress steps
    limit = 5 # No. of workers
    time = 0 # Current time

    # Until all steps completed
    while len(order) < len(alpha_list):
        # If worker(s) available
        while len(pending) < limit:
            # Start any available steps
            for letter in alpha_list:
                # If all pre-reqs satisfied
                # and letter isn't already done
                # and isn't pending
                if (step_available(prereq_dict, order, letter)
                    and letter not in order
                    and letter not in pending.keys()):
                        # Add to pending list, with completion time
                        pending[letter] = time + time_for_step(letter)
            else: # No available steps
                break

        # Determine next step to be completed
        # Finds the next time to be completed, and any steps which
        # will be completed at that time
        next_letters = [] # letters which match min time
        next_time = 60*(len(alpha_list)+1) # Min. time pending. Starts large
        
        for pend in pending.keys():
            if pending[pend] == next_time: # Match min. time
                next_letters.append(pend)
            elif pending[pend] < next_time: # New min. time
                next_time = pending[pend]
                next_letters = [pend]

        # Check next letter found. If no step chosen, raise error
        if len(next_letters) == 0:
            print(pending)
            raise ValueError("No pending step chosen")

        # Advance time to next step
        time = next_time # Set time
        for letter in next_letters: # Remove pending and add to completed
            order.append(letter)
            pending.pop(letter)

    print(time)
