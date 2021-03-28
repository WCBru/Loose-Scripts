DIRECTIONS = ["S", "N", "E", "W"]
DELTAS = {"N": (0, 1), "S": (0, -1), "E": (1,0), "W": (-1, 0)}
OPPOSITES = {"S":"N", "N":"S", "E":"W", "W":"E"}

# Function which traverses an entire string w/o brackets
# This way, the whole string can be treated as a "branch"
# Thus, this is recursive
def traverse_branch(dirstr, nodes, origin):
    current_pos = origin # Current position
    output = nodes # copies the nodes so they can be added to

    # Loop covering all chars
    ind = 0 # current index
    while ind < len(dirstr):
        char = dirstr[ind] # Get next char
        
        # If a branch is detected
        if char == "(":

            # Inner loop for starting branches
            inner_ind = ind + 1 # Start on first char
            start_ind = inner_ind # Start of the branch. inner_ind used for end
            bracket_level = 0 # Used to ensure only parse correct ")"

            # End on ")" matching beginning "("
            while dirstr[inner_ind] != ")" or bracket_level != 0:
                inner_char = dirstr[inner_ind]

                # Moving bracket levels
                if inner_char == "(":
                    bracket_level += 1
                elif inner_char == ")":
                    bracket_level -= 1

                # At bottom bracket level: process |, )
                if bracket_level == 0:    
                    if inner_char == "|": # End of a branch reached
                        branch_str = dirstr[start_ind:inner_ind] # branch str
                        if start_ind != inner_ind: # If branch not empty
                            # Recursive traverse
                            output = traverse_branch(branch_str,
                                                     output, current_pos)
                        start_ind = inner_ind + 1 # Start of next branch
                # END if bracket_level == 0
                inner_ind += 1 # Always increment inner_ind
            # END INNER WHILE
            else: # At the end, parse final branch
                if start_ind != inner_ind:
                    output = traverse_branch(dirstr[start_ind:inner_ind],
                                             output, current_pos)
            
            ind = inner_ind # Set outer index once branching is complete
            # This will incremented at the end
        # END char == "("
        
        # char in DIRECTIONS: Move in that direction
        elif char in DIRECTIONS:
            delta = DELTAS[char] # Get where to move

            # Get next position, and add if not already in list
            next_pos = (current_pos[0] + delta[0], current_pos[1] + delta[1])
            if next_pos not in output.keys():
                output[next_pos] = []

            # Add door to current and next tile
            if char not in output[current_pos]:
                output[current_pos].append(char)
            if OPPOSITES[char] not in output[next_pos]:
                output[next_pos].append(OPPOSITES[char])

            # Set next tile
            current_pos = next_pos
        # END char in DIRECITONS
        
        # Errors for invalid char
        elif char == "|" or char == ")":
            raise ValueError("{0} encountered outside brach".format(char))
        else:
            raise ValueError("{0} not recognised".format(char))
    
        ind += 1
    # END main while loop
            
    return output

if __name__ == "__main__":\
    # Generate room positons and doors
    dir_str = open("input.txt").read().strip()[1:-1]
    node_list = {(0,0): []}
    rooms = traverse_branch(dir_str, node_list, (0,0))

    checked_by_x = {0:[0]} # store checked rooms in a dict by x-coordinate
    visited_sizes = {(0,0): 0} # shortest length to a room based on its position

    # List and indicies for storing nodes to expand
    # Pre-declaring it all first uses memory to save time
    room_buffer = [(0,0, "") for room in range(len(rooms))]
    add_ind = 1 # where to add next node to queue
    take_ind = 0 # where to take next node to expand
    
    while len(visited_sizes.keys()) < len(rooms):
        # Get pos, door to prev tile
        pos = tuple(room_buffer[take_ind][:2])
        prev = room_buffer[take_ind][2]
        take_ind += 1 # Next time, take from next index

        # For each door available
        for door in rooms[pos]:
            if door != prev: # If not previous door
                # Get next room
                delta = DELTAS[door]
                next_pos = (pos[0]+delta[0], pos[1]+delta[1])

                # Init list in checked dict if not already there
                if next_pos[0] not in checked_by_x.keys():
                    checked_by_x[next_pos[0]] = []

                # If not already expanded
                # Mark expanded, add to buffer, add dist to get there
                if next_pos[1] not in checked_by_x[next_pos[0]]:
                    checked_by_x[next_pos[0]].append(next_pos[1])
                    
                    room_buffer[add_ind] = (next_pos[0], next_pos[1],
                                            OPPOSITES[door])
                    add_ind += 1 # Increment where to place next room
                    
                    visited_sizes[next_pos] = visited_sizes[pos] + 1
    # END WHILE
    
    print("A:", max([visited_sizes[key] for key in visited_sizes.keys()]))
    print("B:", sum([int(visited_sizes[key] >= 1000)
                     for key in visited_sizes.keys()]))
