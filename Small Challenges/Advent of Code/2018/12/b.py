import numpy as np

DEBUG = False
EPS = 1e-15 # Epsilon - small float value
TAIL = [-1,-1,-1,-1] # Ends with empty pots

# Gets the correlated mask between the target and the kernel given
# Uses Frequency methods
def get_correlated(target, kernel):
    # Pad the kernel to be the same length as the target state
    padded_kernel = np.concatenate((
        kernel, np.array([0 for x in range(len(target) - kernel.size)])))

    # FT of state and padded kernel
    state_fft = np.fft.dct(target)
    kernel_fft = np.fft.dct(padded_kernel)

    # Correlate: multiply FT and conj of FT
    correlated = np.fft.idctt(np.multiply(state_fft, np.conj(kernel_fft)))

    # Round off FT to whole numbers
    correlated = np.round(np.real_if_close(correlated))

    # Matches iff the correlated score is the length of the kernel
    # This indiciates all elements match
    # Could also be implemented using XNORs for bools
    # Note also, use index 2 behind, since the focus is on the center element
    ker_sum = len(kernel)
    output = [2 if correlated[pot-2] >= ker_sum else 0
            for pot in range(len(correlated))]
    
    # Debug messages
    if DEBUG:
        print("State ", target)
        print("Kernel ", kernel)
        print("Output ", output)
    
    return output

# Returns the list with end -1 truncated
def get_shortened(state):
    start = 0
    end = len(state)-1
    while state[start] < 0:
        start += 1
    while state[end] < 0:
        end -= 1

    # Return start and shortened list
    return (start, state[start:end+1])

# Go through one generation
def iterate_generation(state, kern_list):
    new_state = [-1 for x in range(len(state))] # Blank state
    state_array = np.array(state) # current state to array

    for kernel in kern_list: # Correlate each kernel
        new_plants = get_correlated(state_array, kernel)
        
        # Similar to bool OR
        new_state = [1 if new_state[pot] + new_plants[pot] > 0 else -1
                     for pot in range(len(new_state))]

        if DEBUG:
            print("New State ", new_state)

    return new_state


if __name__ == "__main__":
    # Parse input
    doc = open("input.txt")

    # Board
    initial = doc.readline().split()[-1]
    origin = 0
    state = [1 if char == "#" else -1 for char in initial]
    state = TAIL + state + TAIL
    origin -= 4

    doc.readline() # Blank line
    
    # Kernels which provide a plant
    kernels = []
    line = doc.readline()
    while line != "":
        parts = line.split()

        # Add kernel to list of valid kernels if it generates a plant
        if parts[-1] == "#":
            kernels.append(np.array([1 if char == "#" else -1
                                     for char in parts[0]]))    
        line = doc.readline()
    # End Kernel Read

    # Track states already encountered to find a cycle
    # (Generation, origin) : shortened list
    # origin + oshift: start of non-empty pots
    oshift, shortened = get_shortened(state)
    past_states = {(0,origin + oshift): shortened}
    repeat_start = -1 # Start of cycle
    repeat_end = -1 # End of cycle
    origin_start = 0 # Origin at the start of cycle
    origin_shift = 0 # How much the origin shifts in a cycle

    # Loop for the generations
    for gen in range(1, 50000000000 + 1):
        state = iterate_generation(state, kernels) # New state
        oshift, shortened = get_shortened(state)

        # Compare to past states
        for key in past_states.keys():
            # If there's a match
            if past_states[key] == shortened:
                repeat_start = key[0] # Generation start
                repeat_end = gen # Generation end
                origin_start = key[1] # Pre-cycle origin shift
                origin_shift = (origin + oshift) - key[1] # Cycle shift
                break
        else: # No match: add to past_states
            past_states[(gen, origin + oshift)] = shortened

        # Break if a match was found
        if repeat_start != -1 and repeat_end != -1:
            break
        
        # Pad state if edges have been converted
        if sum(state[0:len(TAIL)]) > sum(TAIL):
            state = TAIL + state
            origin -= 4 # Shift origin
        if sum(state[-len(TAIL):]) > sum(TAIL):
            state = state + TAIL

        if DEBUG:
            print(state)
            print("#########################")

    # If a repeat was found
    if repeat_start != -1 and repeat_end != -1:
        gens = 50000000000 - repeat_start # gens before cycle

        # Shift: shift to start of cycle + no. of cycles * shift + remainder
        cyclic_shift = (gens//(repeat_end - repeat_start))*origin_shift
        shift = origin_start + cyclic_shift + gens%(repeat_end - repeat_start)
        short_state = past_states[(repeat_start, origin_start)]
        print(sum([pot + shift if short_state[pot] > 0 else 0 for pot in
                   range(len(short_state))]))
    else: # If the end was reached
        print(sum([pot + origin if state[pot] > 0 else 0
                   for pot in range(len(state))]))
