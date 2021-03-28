if __name__ == "__main__":
    num_players, num_marbles = [int(num) for num in
                                open("input.txt").read().split()[0::6]]

    # Scores, current marble index, amd board
    scores = [0 for x in range(num_players)]
    current = 0
    board = [0]

    # 1 -> num_marbles
    for marble in range(1, num_marbles+1):
        if marble % 23 == 0:
            current_player = (marble-1) % num_players # Marble starts at 1
            current -= 7 # Move 7 spaces ccw
            # Note pop removes the target marble as well
            scores[current_player] += marble + board.pop(current)
            # If current is negative, this correction is needed
            # If positive the marble cw falls into the current index
            # But if negative, current moves ccw as well, so need to correct
            current += 1 if current < 0 else 0
        else:
            # This check is needed in case the new marble would be added to
            # the edge. The modulo nature of this would bring it to the start
            if current != ((len(board) - 2) % len(board)):
                current = (current + 2) % len(board)
            else: # New marble at the edge
                current = len(board)

            board.insert(current, marble)

    print(max(scores))
