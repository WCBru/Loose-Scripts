ATTACK = 3
FULL_HP = 200
DELTAS = [(0, -1), (-1, 0), (1, 0), (0, 1)] # In reading order
LOOPS = 9

SEARCH_DEBUG = False
MAP_DEBUG = False
GAME_DEBUG = False
RESULT_DEBUG = True

# Note combatants are identical
# ID can come from list of combantants
class Combatant:
    def __init__(self, x, y, att = ATTACK):
        self.attack = att
        self.hp = FULL_HP
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    def attack_to(self, target):
        target.take_damage(self.attack)

    def take_damage(self, amount):
        self.hp -= amount

# Generate valid targets from the combatant list given
# Valid here means not obstructed
# Removes duplicates automatically
# Returns a list of the enemy position if already adjascent to an enemy
def gen_targets(combatant_list, board, initial):
    target_list = []

    # For each combatant
    for combatant in combatant_list:
        # Get the adjascent sqaures
        adj_squares = [(combatant.x + move[0], combatant.y + move[1])
                       for move in DELTAS]

        # For each adjascent square
        for pos in adj_squares:
            if pos == initial: # If already adjascent
                return [initial] # Return the current position alone

            # Add square if open and not already accounted for
            if board[pos[1]][pos[0]] == "." and pos not in target_list:
                target_list.append(pos)

    return target_list

# Return the absolute distance between 2 n-tuples (based on the min size)
def abs_dist(pos1, pos2):
    return sum([abs(pos1[i]-pos2[i]) for i in range(min(len(pos2),len(pos1)))])

# Get the best move possible
# Target list is known to have elements
# Do a BFS to favour reading order
def get_best_move(board, targets, pos, dim):
    # Note pre-allocated list sizes to reduce time cost
    # Tiles to expand
    toExpand = [(-1,-1) for i in range(dim[1]*dim[0])]
    toExpand[0] = pos
    # Parents of tiles to be expanded
    parents = [(-1,-1) for i in range(dim[1]*dim[0])]    
    parents[0] = pos

    take_ind = 0 # Index for next node to expand
    add_ind = 1 # Index for where to add next child node

    visited = {} # visited node : parent

    # Masks for node already visited and for if a square is a possible goal
    visited_mask = [[True for col in range(dim[0])] for row in range(dim[1])]
    goal_mask = [[(col, row) in targets for col in range(dim[0])]
                 for row in range(dim[1])]

    # Go until nothing left to expand
    while add_ind > take_ind:
        # Get next node and set parent node for next node
        current = toExpand[take_ind]
        visited[current] = parents[take_ind]
        take_ind += 1 # Increment where to take nodes from

        
        if SEARCH_DEBUG:
            print("##########\n", current.pos, "\n", [v.pos for v in visited])
        
        # Target found: backtrace to first move
        if goal_mask[current[1]][current[0]]:
            # DEBUG
            if SEARCH_DEBUG:
                print("Target found, backtracing from ", current.pos)

            # Loop: Keep going back if distance to origin > 1
            # I.e. not next to origin
            current_tile = current
            while abs_dist(current_tile, pos) > 1:
                # DEBUG
                if SEARCH_DEBUG:
                    print("Trace: ", current_tile)
                    
                current_tile = visited[current_tile]
            else: # Return move found
                # DEBUG
                if SEARCH_DEBUG:
                    print("Returning ",
                          (current_tile[0]-pos[0], current_tile[1]-pos[1]))
                    
                return (current_tile[0]-pos[0], current_tile[1]-pos[1])
            # END WHILE

        # Find and add children
        for delta in DELTAS:
            newpos = (current[0] + delta[0], current[1] + delta[1])
            
            if SEARCH_DEBUG:
                print("New position: ", newpos)
                
            # If not visited and child node is empty
            if (visited_mask[newpos[1]][newpos[0]]
                and board[newpos[1]][newpos[0]] == "."):

                # DEBUG
                if SEARCH_DEBUG:
                    print("Adding position to search")

                # Add node and its parent (the current node)
                toExpand[add_ind] = newpos
                parents[add_ind] = current

                # Set visited mask (since this is the optimal way
                # to reach newpos, and increment adding index
                visited_mask[newpos[1]][newpos[0]] = False
                add_ind += 1
    else: # Ran out of nodes: not possible, so don't move
        return (0,0)

# Find a target if adjascent, otherwise return None
def find_target(group, pos, mult):
    # Formulate adjascent tiles
    adj_moves = [(pos[0] + move[0], pos[1] + move[1]) for move in DELTAS]
    target = None

    # If an enemy is in an adjascent tile, mark them as the target
    # Enemies are sorted in reading order
    for enemy in sorted(group, key=lambda elm: mult*elm.y+elm.x):
        # Mark target if adjascent and a target is not already marked
        # or the new target has less HP
        if (enemy.x, enemy.y) in adj_moves:
            if target == None:
                target = enemy
            elif enemy.hp < target.hp:
                target = enemy

    return target

if __name__ == "__main__":
    ini_board = []

    # Read in input
    doc = open("input.txt")
    line = doc.readline()
    while line != "":
        ini_board.append(list(line.strip()))
        line = doc.readline()
    doc.close()

    # Board dimensions
    rows = len(ini_board)
    cols = max([len(row) for row in ini_board])

    # Iterate up from 4 - 200
    for d in range(4,201):
        # Populate Elf and Goblin lists
        board = [row[:] for row in ini_board]
        elves = []
        goblins = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "E":
                    elves.append(Combatant(col,row, att = d))
                elif board[row][col] == "G":
                    goblins.append(Combatant(col,row))

        elves_initial = len(elves) # Elf numbers for counting losses
        turn = 0 # Turn number. Incremented at turn completion

        # While numbers from both sides are still alive
        while len(elves)*len(goblins) > 0:
            # Print Map debug
            if MAP_DEBUG:
                print("Turn ", turn)
                for row in board:
                    print("".join(row))

            # Combined list of elves and goblins, in reading order
            full_list = sorted(elves + goblins, key=lambda c: cols*c.y+c.x)

            # Iterate through elves and goblins, as sorted above
            for npc in full_list:
                # If already dead, continue
                if npc not in goblins and npc not in elves:
                    continue
                
                # Stop if fighting is over
                if len(elves)*len(goblins) <= 0:
                    break

                # Get the hostile group
                target_group = elves if npc in goblins else goblins

                # A check to ensure the co-ords are valid
                if board[npc.y][npc.x] != ("G" if npc in goblins else "E"):
                    raise IndexError("Wrong tile pos ", (npc.y, npc.x))

                # Print what kind side this combatant is
                if GAME_DEBUG:
                    print("\nTurn for", ("goblin" if npc in goblins else "elf"))
                    
                # Generate list of target tiles to move to
                target_list = gen_targets(target_group, board, (npc.x, npc.y))
                if GAME_DEBUG:
                    print("Valid Targets:\n", target_list)

                # Determine move to be made, if moves can be made
                if len(target_list) > 0:
                    # Get best move
                    move = get_best_move(board, target_list,
                                         npc.get_pos(), (cols, rows))
                    if GAME_DEBUG:
                        print("Best move: ", move)

                    # Move current npc in list and on the board
                    board[npc.y][npc.x] = "."
                    npc.y += move[1]
                    npc.x += move[0]
                    board[npc.y][npc.x] = "G" if npc in goblins else "E"
                    
                    # Determine if can attack enemy
                    target = find_target(target_group, npc.get_pos(), cols)
                    if target != None: # If target found
                        # DEBUG
                        if GAME_DEBUG:
                            print("Target acquired: ", (target.x, target.y))
                            print("Target has ", target.hp, " hp")

                        # Remove if target killed
                        npc.attack_to(target)
                        if target.hp <= 0:
                            if GAME_DEBUG:
                                print("Target eliminated")

                            # Remove target from board and lists
                            board[target.y][target.x] = "."
                            target_group.remove(target)
            else: # Turn complete: increment turn counter
                turn += 1            

        # Evaluate this loop
        score = sum([c.hp for c in elves + goblins])*turn
        if RESULT_DEBUG:
            print("\nSummary for", d)
            print(("Goblins" if len(goblins) > 0 else "Elves"), "win")
            print("Elves lost", elves_initial - len(elves))
            print("Score:", score)

        # If the elves didn't suffer any losses, print score
        if len(elves) == elves_initial:
            print(score)
            break
