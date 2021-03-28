# Approach: Scan through once and check for repeat. If not, return the full
# list of tranversals. Then do a check between adjascent elements to determine
# if the difference is a multiple of 442.

# First pass check: returns the end result, if a repeat was found, & val list
def check_by_memory(int_list):
    known = [0]
    current = 0
    
    for num in int_list:
        current += num
        if current in known: # if number seen before
            return (current, True, known)
        else:
            known.append(current)
    else: # If no number was found twice, return full list
        return (current, False, known)

# Find the first repeat
# Outputs the two numbers linked by the smallest number of iterations
def find_first_repeat(lst, target):
    min_div = max(lst)+1
    out = 0 # output

    # Iterate through the list twice
    for ind1 in range(len(lst)):
        for ind2 in range(len(lst)):
            diff = lst[ind2] - lst[ind1] # Difference

            # Check if the larger number is taken, and if diff is a
            # multiple of the end number.
            if diff%target == 0:
                div = diff//target
                # Require divisor is positive and past 1st iteration
                if div > 1 and div < min_div: 
                    min_div = div
                    out = (lst[ind1], lst[ind2])
                    
    if min_div <= max(lst):
        return out
    else:
        raise IndexError("No value found")


if __name__ == "__main__":
    num_list = [int(num) for num in open("input.txt").read().split("\n")]
    mem = check_by_memory(num_list)

    if mem[1]:
        print(mem[0])
    else:
        print(find_first_repeat(mem[2], mem[0]))
