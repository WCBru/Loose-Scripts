# Generate walls for problem
def get_walls(doc_name):
    walls = []

    # Read in each tuple and create a number of walls
    doc = open(doc_name)
    line = doc.readline()
    while line != "":
        # Initially, always treat the second entry (the range) as y values
        x, y = line.strip().split(', ')
        y_1, y_2 = y[2:].split('..')

        # Add the range of "y" values
        addList = [(int(x[2:]), yval) for yval in range(int(y_1), int(y_2)+1)]

        # Reverse if y was given first
        if x[0] == 'y': 
            addList = [(wall[1], wall[0]) for wall in addList]

        # Add line walls to overall wall list and read in next line
        walls += addList
        line = doc.readline()
    # END while
    return walls

# Get all tiles bound by walls at this y, containing x (up to limit of map)
# Takes walls nested list, x, y point and x bounds of map (as tuple)
def get_layer(walls, x, y, x_lims):
    output = [x] # Initally, start with the point given

    # Use offset to search left then right
    offset = -1 # I.e. starts negative, then goes positive
    while True:
        # If a wall hasn't been hit, and extend no further than 2 blocks
        # beyond bounds (in case water goes past the furthest wall)
        if x + offset not in walls[y] and (
            x + offset >= x_lims[0] -2 and x + offset <= x_lims[1] + 2):
            
            # Then add this wall to output and increment offset
            output.append(x+offset)
            offset += 1 if offset > 0 else -1

        # Wall hit to the left, start searching right
        elif offset < 0:
            offset = 1
        else: # Wall hit on right, return
            return output

if __name__ == "__main__":  
    walls = get_walls("input.txt")

    # x and y limits
    y_vals = sorted([wall[1] for wall in walls])
    min_y = y_vals[0]
    max_y = y_vals[-1]
    x_vals = sorted([wall[0] for wall in walls])
    min_x = x_vals[0]
    max_x = x_vals[-1]

    # Convert list of walls into a nested list
    # To speed up wall collision checks
    layers = []
    # For each y-value
    for y in range(max_y + 1):
        # Add the wall's x value if y-value matches
        toAdd = []
        for wall in walls:
            if wall[1] == y:
                toAdd.append(wall[0])
                
        layers.append(toAdd)
    # END FOR

    toExpand = [(500,0)] # Expand downward list
    spread_list = [] # Expand across list

    # List of water tiles. Visited contains both running and supported
    supported = [[] for y in range(len(layers))]
    running = [[] for y in range(len(layers))]
    visited = [[] for y in range(len(layers))]

    # Go until nothing left to expand
    while len(toExpand) > 0 or len(spread_list) > 0:
        # Spread outward first, as this determines what can fall downwards
        if len(spread_list) == 0: # No spreading
            x,y = toExpand.pop()
        else:
            x,y = spread_list.pop()

        # Add water tile if not visited and leq max y-value
        # Added water starts as running water
        if y <= max_y and x not in visited[y]:
            running[y].append(x)
            visited[y].append(x)

        # Continue of y-limit reached. There can't be walls below this
        if y == max_y:
            continue

        # First case: below empty, add to nodes to visit
        if x not in layers[y+1] and x not in visited[y+1]:
            toExpand.append((x,y+1))
            
        # Second Case: Supported water or wall below, spread out
        elif x in layers[y+1] or x in supported[y+1]:
            # Add left and right nodes
            if x+1 not in visited[y] and x+1 not in layers[y]:
                spread_list.append((x+1, y))
            if x-1 not in visited[y] and x-1 not in layers[y]:
                spread_list.append((x-1, y))

            # Scan layer and check if filled - layer full AND can't fall
            this_layer = get_layer(layers,x,y, (min_x, max_x))
            if all([tile in visited[y] for tile in this_layer]):
                
                # Check that the water can't fall
                if all([tile in supported[y+1] + layers[y+1]
                        for tile in this_layer]):

                    # Can't fall: water in this layer becomes supported
                    # Running sources from above should be expanded again
                    # So they can spread out
                    for x_prev in this_layer:
                        # Move running to supported
                        running[y].remove(x_prev)
                        supported[y].append(x_prev)

                        # Find sources
                        if x_prev in running[y-1]:
                            toExpand.append((x_prev, y-1))
                    # END FOR
            # END check for running -> supported conversion
    # END MAIN WHILE LOOP

    print(sum([len(row) for row in supported[min_y:]]))
