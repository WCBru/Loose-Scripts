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
    state_fft = np.fft.fft(target)
    kernel_fft = np.fft.fft(padded_kernel)

    # Correlate: multiply FT and conj of FT
    correlated = np.fft.ifft(np.multiply(state_fft, np.conj(kernel_fft)))

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

    # For each generation
    for gen in range(20):
        new_state = [-1 for x in range(len(state))] # Blank state
        state_array = np.array(state) # current state to array

        for kernel in kernels: # Correlate each kernel
            new_plants = get_correlated(state_array, kernel)
            
            # Similar to bool OR
            new_state = [1 if new_state[pot] + new_plants[pot] > 0 else -1
                         for pot in range(len(new_state))]

            if DEBUG:
                print("New State ", new_state)

        # Pad state if edges have been converted
        if sum(new_state[0:len(TAIL)]) > sum(TAIL):
            new_state = TAIL + new_state
            origin -= 4 # Shift origin
        if sum(new_state[-len(TAIL):]) > sum(TAIL):
            new_state = new_state + TAIL

        if DEBUG:
            print(new_state)
            print("#########################")
        state = new_state[:] # Array copy - avoids reference problems

    print(sum([pot + origin if state[pot] > 0 else 0 for pot in range(len(state))]))
