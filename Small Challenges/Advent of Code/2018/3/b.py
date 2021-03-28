# This is the same as part A except with a final step
# Since only 1 claim is unqiue, we need only find the first element
# Which is one, return that starting co-ord, and find the ID

# Return a tuple for claim info
# (ID, start_x, start_y, size_x, size_y)
def process_claim(claim_string):
    parts = claim_string.split()
    start = [int(num) for num in parts[2][:-1].split(',')]
    size = [int(num) for num in parts[3].split('x')]
    return (int(parts[0][1:]), start[0], start[1], size[0], size[1])

# Generate Claim List (tuples)
def generate_claim_list(doc_string):
    doc = open(doc_string)
    claim = doc.readline()
    out_list = []

    # For each claim
    while claim != "":
        # Get all details
        out_list.append(process_claim(claim))
        claim = doc.readline()

    doc.close()
    return out_list

def check_claim(board, claim):
    ID, startx, starty, sizex, sizey = claim

    # Check all squares are == 1
    for row in range(startx, startx + sizex):
        for col in range(starty, starty+sizey):
            if board[row][col] != 1:
                return False

    return True

# Brute force method
if __name__ == "__main__":
    # Brute force board of claims
    board = [[0 for i in range(1000)] for j in range(1000)]
    claim_list = generate_claim_list("input.txt")

    for claim in claim_list:
        ID, startx, starty, sizex, sizey = claim
        
        # Increment each square in the claim
        for row in range(startx, startx + sizex):
            for col in range(starty, starty+sizey):
                board[row][col] += 1
    # End For

    # Print the first claim with zero overlap
    for claim in claim_list:
        if check_claim(board, claim):
            print(claim[0])
            break
    else:
        print("No match found")
