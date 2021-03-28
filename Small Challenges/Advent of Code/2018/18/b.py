import numpy as np

LIMIT = 1000000000

# Strategy:
# For each minute:
# Pad +2 to each side (Using a 3x3 kernel)
# Mask the scene for each type of tile and correlate the kernel
# Initially set to prev.
# If mask matches conditions, edit entry in tiles

# Generate board from input text file name
def gen_board(doc_name):
    output = []
    doc = open(doc_name)
    line = doc.readline().strip()

    # Read in ecah line and convert the string into a list
    while line != "":
        output.append(list(line))
        line = doc.readline().strip()
        
    return output
# End gen_board

# Mask the board: 1 if it matches the target, 0 otherwise
def generate_mask(tiles, target):
    return np.array([[1 if char == target else 0 for char in row]
                     for row in tiles])

# Count the number of tiles which match the target
def char_count(tiles, target):
    return sum([sum([int(char == target) for char in row]) for row in tiles])

if __name__ == "__main__":
    tiles = np.array(gen_board("input.txt"))
    # Pad tiles with junk value
    tiles = np.pad(tiles, 2, 'constant', constant_values='-')
    encountered = [np.copy(tiles)] # Encountered scenarios
    
    # Generate Kernel
    row_len = len(tiles[0])
    # Kernel: 3 x 3 of 1s, 0 otherwise
    kernel = [[int(row < 3 and col < 3) for col in range(row_len)]
              for row in range(len(tiles))]
    k_ft = np.conj(np.fft.fft2(kernel)) # conj. for correlation not convolve
    
    for minute in range(1, LIMIT + 1): # 10 minute range
        # Generate mask, do fft and multiply with kernel
        tree_mask = generate_mask(tiles, '|')
        t_ft = np.fft.fft2(tree_mask)
        tree_sums = np.fft.ifft2(np.multiply(t_ft, k_ft))
        tree_sums = np.round(np.real_if_close(tree_sums))

        # Same for lumber yards
        yard_mask = generate_mask(tiles, "#")
        y_ft = np.fft.fft2(yard_mask)
        yard_sums = np.fft.ifft2(np.multiply(y_ft, k_ft))
        yard_sums = np.round(np.real_if_close(yard_sums))

        # Create a new copy of the board
        new_board = np.array([row[:] for row in tiles])

        # Account for padding: 2 to length-2
        # When checking sums (row-1, col-1) as the origin for the correlation
        # is in the top-left corner, rather than the center
        for row in range(2, len(tiles)-2):
            for col in range(2, row_len-2):
                # Open tile - check tree coverage
                if tiles[row,col] == '.':
                    if tree_sums[row-1, col-1] >= 3:
                        new_board[row][col] = '|'
                # Tree tile - check yard coverage
                elif tiles[row,col] == '|':
                    if yard_sums[row-1,col-1] >= 3:
                        new_board[row][col] = '#'
                # Yard tile - check yard and tree coverage
                elif tiles[row,col] == '#':
                    if yard_sums[row-1,col-1] < 2 or tree_sums[row-1,col-1]< 1:
                        new_board[row][col] = '.'
                else: # Unrecognised tile
                    print("Wrong tile ", tiles[row,col])

        # Check for a repeating pattern
        for board in range(len(encountered)):
            # If a match from a previous board is found
            if (encountered[board] == new_board).all():
                start_min = board # Start of cycle
                cycle_length = minute - board # Cycle length
                tail = (LIMIT - start_min) % cycle_length # cycle leftover
                encountered.append(np.copy(new_board)) # add last board
                tiles = encountered[start_min + tail] # select ending board
                break
        else: # If none match, append copy of new board, and iterate
            encountered.append(np.copy(new_board))
            tiles = new_board
            continue

        break # This will be reached if broken in for loop
            

    # Print product of tile counts of trees and yards
    print(char_count(tiles, '|')*char_count(tiles, '#'))
