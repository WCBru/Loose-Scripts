INPUT = 7347
SQ_SIZE = 3 # Kernel length (square side length)

# Generate board: individually for each square
def generate_board(seed):
    board = [[0 for x in range(300)] for y in range(300)]
    for x in range(300):
        for y in range(300):
            raw_val = ((x+1)+10)*(seed + (y+1)*((x+1)+10))
            board[y][x] = ((raw_val // 100) % 10) - 5
    return board

# Convolve in original space
if __name__ == "__main__":
    board = generate_board(INPUT)

    # Max Properties
    max_val = 0
    max_position = (-1,-1)

    # Origin in top left, so stops short based on SQ_SIZE
    for x in range(300-SQ_SIZE+1):
        for y in range(300-SQ_SIZE+1):
            # Current value: sum over rows and cols
            current = sum([ sum(board[y][x:x+SQ_SIZE])
                            for y in range(y,y+SQ_SIZE) ])

            # Replace max if new mxa found
            if current > max_val:
                max_val = current
                max_position = (x+1,y+1)

    print(max_position)
    

    
