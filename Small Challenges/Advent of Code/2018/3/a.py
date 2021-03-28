# Return a tuple for claim info
# (ID, start_x, start_y, size_x, size_y)
def process_claim(claim_string):
    parts = claim_string.split()
    start = [int(num) for num in parts[2][:-1].split(',')]
    size = [int(num) for num in parts[3].split('x')]
    return (int(parts[0][1:]), start[0], start[1], size[0], size[1])

# Brute force method
if __name__ == "__main__":
    # Brute force board of claims
    board = [[0 for i in range(1000)] for j in range(1000)]
    doc = open("input.txt")
    claim = doc.readline()

    # For each claim
    while claim != "":
        # Get all details
        ID, startx, starty, sizex, sizey = process_claim(claim)

        # Increment each square in the claim
        for row in range(startx, startx + sizex):
            for col in range(starty, starty+sizey):
                board[row][col] += 1

        claim = doc.readline() # Next claim
    # End while
    
    # Print the sum of rows, which are a sum of all elements which are >= 2
    print(sum([ sum([num > 1 for num in row]) for row in board ]))
        
    doc.close()
