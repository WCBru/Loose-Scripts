DEPTH = 9465
TARGET = (13, 704)
Y_MULT = 48271
X_MULT = 16807
E_MOD = 20183
TYPES = {0:"Rocky", 1:"Narrow", 2:"Wet"}

if __name__ == "__main__":
    # Generate board of -1s
    board = [[-1 for x in range(TARGET[0]+1)] for y in range(TARGET[1]+1)]

    # Fill in the board in diagonals: start with 0 of on axis and
    # Make way to the other
    for diag in range(sum(TARGET)+1):
        # Tiles go from x axis to y axis
        for tile in range(diag + 1):
            x = tile
            y = diag - tile

            # If outside limits, continue
            if x > TARGET[0] or y > TARGET[1]:
                continue

            # Cases, as per problem description
            if y == 0 and x == 0:
                tile_type = 0
            elif x == TARGET[0] and y == TARGET[1]:
                tile_type = 0
            elif x == 0:
                tile_type = (y * Y_MULT + DEPTH)%E_MOD
            elif y == 0:
                tile_type = (x * X_MULT + DEPTH)%E_MOD
            else:
                tile_type = (board[y-1][x] * board[y][x-1] + DEPTH)%E_MOD

            board[y][x] = tile_type # Set type on board
        # END INNER FOR
    # END MAIN FOR LOOP
    
    print(sum([sum([col%3 for col in row]) for row in board]))
