# Strategy: Rather than keep 1 master list, traverse nodes which only
# know adjascent nodes. Was spoiled for this solution

# Node class. Keeps only 3 values: itself, the previous and next numbers
# Next in this case is cw
class Node:
    def __init__(self, value, back, forward):
        self.value = value
        self.prev = back
        self.next = forward

if __name__ == "__main__":
    num_players, num_marbles = [int(num) for num in
                                open("input.txt").read().split()[0::6]]
    num_marbles *= 100 # New goal

    # Scores, current marble index, amd board
    scores = [0 for x in range(num_players)]
    current = 0
    board = {0: Node(0,0,0)}

    # 1 -> num_marbles
    for marble in range(1, num_marbles+1):
        if marble % 23 == 0:
            current_player = (marble-1) % num_players # As marble starts at 1

            # Move 6 paces back. This will become the next current marble
            for move in range(6):
                current = board[board[current].prev].value
            pop = board[board[current].prev].value # Marble to pop
            pop_ccw = board[board[pop].prev].value # Marble ccw of to pop

            # Change current and pop_ccw so they cut out the marble to remove
            board[current].prev = pop_ccw
            board[pop_ccw].next = current
            
            scores[current_player] += marble + pop # Add score
            board.pop(pop) # Remove marble to be removed. Throws error if miss
        else:
            # Get marble values 1 and 2 cw of current
            cw1 = board[board[current].next].value
            cw2 = board[board[cw1].next].value

            # Edit endpoints of above marbles
            board[cw1].next = marble
            board[cw2].prev = marble
            
            board[marble] = Node(marble, cw1, cw2) # Add new marble
            current = marble # Update current

    print(max(scores))
