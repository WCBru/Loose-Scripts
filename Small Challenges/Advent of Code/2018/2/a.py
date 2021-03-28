if __name__ == "__main__":
    id_list = open("input.txt").read().split("\n")
    counts = [0,0]
    
    # For each ID
    for id_str in id_list:
        char = ''
        count = 0
        counted = [False, False]

        #Iterate through letters in ID
        for letter in sorted(id_str):
            if char != letter:
                # Add 
                char = letter
                counted[0] |= count == 2
                counted[1] |= count == 3
                count = 1
            else:
                count += 1
        else: # Run check once at the end
            counted[0] |= count == 2
            counted[1] |= count == 3
            counts = [counts[i] + (1 if counted[i] else 0) for i in range(len(counts))]

    print(counts[0]*counts[1])
