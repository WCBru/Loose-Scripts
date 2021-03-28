DEPTH = 9465#11820#9465 #9465 #510
START = (0, 0)
TARGET = (13,704)#(7,782)#(13,704) #(13,704)#(10, 10)
Y_MULT = 48271
X_MULT = 16807
E_MOD = 20183
TYPES = {0: "Rocky", 1: "Wet", 2: "Narrow"}
TOOLS = {"None": 0, "Torch": 1, "Gear": 2}
DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Fill a diagonal with the diag parameter being the sum of coords
# E.g. the first tile (0,0) is diag = 0, since 0 + 0 = 0
def fill_diag(board, diag):
    # Note since this is the only time the board is written to,
    # There should be no need to worry about copying the elements precisely
    output = board

    # Add the new diagonal
    for row in output:
        row.append(-1)
    output.append([-1])
    
    # Tiles go from x axis to y axis
    for tile in range(len(output)):
        x = tile
        y = (len(output) - 1) - tile

        # Cases, as per problem description
        if x == TARGET[0] and y == TARGET[1]:
            tile_type = DEPTH % E_MOD
        elif x == START[0] and y == START[1]:
            tile_type = DEPTH % E_MOD
        elif x == 0:
            tile_type = (y * Y_MULT + DEPTH)%E_MOD
        elif y == 0:
            tile_type = (x * X_MULT + DEPTH)%E_MOD
        else:
            tile_type = (output[y-1][x] * output[y][x-1] + DEPTH)%E_MOD

        output[y][x] = tile_type # Set type on board
    # END FOR

    return output

# Get adjascent co-ordinates (up/down/left/right)
def get_adjascent(coord):
    output = []

    # Iterate through each delta and check if both coord non-negative
    for delta in DELTAS:
        nextpos = (coord[0]+delta[0], coord[1]+delta[1])
        
        if nextpos[0] >= 0 and nextpos[1] >= 0:
            output.append(nextpos)

    return output

# Determine the cost for changing tools, and return which tools to use
def process_tools(curr_r, tool, next_r):
    #print("Have", tool, "in", curr_r, "going to", next_r)
    # Change gear if unsuitable
    if any([i > 2 or i < 0 for i in [curr_r, tool, next_r]]):
        raise IndexError("Process Tools Error", [curr_r, tool, next_r])
    
    if TYPES[next_r] == "Rocky" and tool == TOOLS["None"]:
        return (7, TOOLS["Torch"] if TYPES[curr_r] == "Narrow" else TOOLS["Gear"])
    elif TYPES[next_r] == "Narrow" and tool == TOOLS["Gear"]:
        return (7, TOOLS["Torch"] if TYPES[curr_r] == "Rocky" else TOOLS["None"])
    elif TYPES[next_r] == "Wet" and tool == TOOLS["Torch"]:
        return (7, TOOLS["Gear"] if TYPES[curr_r] == "Rocky" else TOOLS["None"])
    else: # Current tool is fine - just stick with it
        return (0, tool)

# Get distance between 2 co-ords
def dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def get_least_cost(starting_tool):
    # Generate board of -1s
    board = []

    # Initially fill to board to include the target
    # Fill in the board in diagonals: start with 0 of on axis and
    # Make way to the other
    for diag in range(sum(TARGET)+1):
        board = fill_diag(board, diag)
    # END GENERATION FOR LOOP

    # Test for if this generation method is valid
    #print(sum([sum([col%3 for col in row[:TARGET[0]+1]])
    #           for row in board[:TARGET[1]+1]]))

    toExpand = [(START[0] , START[1], starting_tool)] #(x, y, equipment)
    costs = [dist(START, TARGET)]
    dur = [0]
    visited = {} # Hashmap for visited tiles and their cost
    #prevs = [START]

    while True:
        # Get this tile location gear and cost
        min_ind = costs.index(min(costs))
        x, y, tool = toExpand.pop(min_ind)
        cost = costs.pop(min_ind)
        current_dur = dur.pop(min_ind)
        current_region = board[y][x] % 3
        #prev = prevs.pop(min_ind)

        #print("########\n", (x,y), ": ", current_dur, cost, TYPES[current_region], tool)

        #print("Expanded", (x,y), "with", tool, "on", TYPES[current_region])
        #print("Cost:", current_dur, "With Heu:", cost)

        # Overwrite cost if new optimal found
        if (x, y, tool) in visited.keys():
            if visited[(x,y, tool)] > current_dur:
                raise ValueError("Suboptimal Expansion")            
            continue

        #print("Expanding", (x,y), "with", current_dur)

        visited[(x,y,tool)] = current_dur

        if (x,y) == TARGET:
            '''
            print(board)
            for row in board:
                for i in range(len(row)):
                    if row[i] % 3 == 0:
                        row[i] = '.'
                    elif row[i] % 3 == 1:
                        row[i] = '='
                    else:
                        row[i] = '|'

                print(''.join(row))
            '''
            #for x in visited:
            #    print(x, visited[x])
            break
            

        # For each adjascent tile, add to board if not big enough
        for adj in get_adjascent((x,y)):
            # Add diag if necessary
            if sum(adj) >= len(board):
                board = fill_diag(board, sum(adj))

            
                
            # Generate the costings and tool required
            next_region = board[adj[1]][adj[0]] % 3
            change_cost, next_tool = process_tools(current_region, tool,
                                                   next_region)

            #if (change_cost > 0):
            #    print(str((x,y)) + " -> " + str(adj) + " " + str(tool) + " -> " + str(next_tool))
                
            travel_cost = current_dur + 1
            heu_cost = dist(adj , TARGET)

            #if change_cost == 7:
            #    print("Change at", adj)
            
            #print("Picked", next_tool)
            if adj == TARGET and next_tool != TOOLS["Torch"]:
                change_cost += 7
                next_tool = TOOLS["Torch"]

            next_dur = travel_cost + change_cost
            queue_cost = next_dur + heu_cost

            #print("##\n", adj, ":", next_dur, queue_cost, TYPES[next_region], next_tool)

            adj_entry = (adj[0], adj[1], next_tool)
            if adj_entry in visited and visited[adj_entry] > next_dur:
                raise ValueError("Better adj found", visited[adj_entry], next_dur, adj_entry)

            # Add to the queue
            if adj_entry not in visited:
                #print("Adding", adj, "with travel", travel_cost, "Heuristic", heu_cost, "Change", change_cost)
                costs.append(queue_cost)
                dur.append(next_dur)
                toExpand.append(adj_entry)
                #prevs.append((x,y))
                #print(dur)
                #print(costs)
        

    #current = TARGET
    #while current != START:
    #    current = visited[current][1]
    return visited[(TARGET[0], TARGET[1], TOOLS["Torch"])]

if __name__ == "__main__":
    torch_score = get_least_cost(TOOLS["Torch"])
    print(torch_score)
