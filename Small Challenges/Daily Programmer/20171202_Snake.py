# Currently solves 4 dimensions quite handily
# However, even reducing the depths iterated over,
# The real problem is how long it takes for each depth to be completed
# Future improvements should find a way to cut down how thoroughly
# a level needs to be checked

# Determines if two nodes are adjascent
# Adjascent nodes only have 1 different co-ordinate
def is_neighbour(node_a, node_b):
    diff_flag = False # flag to track if 1 difference found

    for coord in range(len(node_a)):
        if node_a[coord] != node_b[coord]:
            if diff_flag:
                return False
            else:
                diff_flag = True
    else:
        return True

# Check if a node is usable based on the visited nodes
def is_usable(past_nodes, current_node):
    for node in past_nodes:
        if is_neighbour(node, current_node):
            return False
    else:
        return True

def toggle(node, nth):
    out_str = ""
    for char in range(len(node)):
        if char != nth:
            out_str += node[char]
        else:
            out_str += str((int(node[nth])+1)%2)
    return out_str

def get_possible_moves(node, path):
    out_lst = []
    for digit in range(len(node)):
            toggled = toggle(node, digit)
            if is_usable(path, toggled):
                out_lst.append(toggled)
    return out_lst

# Find the longest valid path based on dimensionality and depth
def determine_longest_path(dim, depth):
    print("Depth: " + str(depth))
    visited = []
    best = []
    stack = []
    level_lst = [0]

    current_node = "" # Contruct first node
    for i in range(dim):
        current_node += "0"
    stack.append(current_node)

    while len(stack): # Iterate til stack empty
        current_node = stack.pop()
        level_lst.pop()
        possible_moves = []

        # If the limit has been reached, backtrack
        if len(visited) >= depth:
            visited.append(current_node) # Add current node to list of visited
            best = visited[:]
            if len(level_lst):
                target = level_lst[-1]
                while len(visited) != target:
                    visited.pop()
                continue
            else:
                break

        # Find all usable nodes from this point
        possible_moves = get_possible_moves(current_node, visited)
        visited.append(current_node) # Add current node to list of visited

        # Save and start backtracking if possible moves empty
        if not len(possible_moves) and len(level_lst):
            if len(visited) > len(best):
                best = visited[:]

            target = level_lst[-1]
            while len(visited) != target:
                visited.pop()
            continue # Start search from new node

        # If advancement possible, add all children to the stack
        stack.extend(possible_moves)
        
        for node in possible_moves:
            level_lst.append(len(visited))
    
    return best

def find_highest_level(dimensions, start_level, last = False):
    best = []
    current_level = start_level
    while True:
        new_path = determine_longest_path(dimensions, current_level)
        if len(new_path) <= len(best):
            if last:
                return best
            else:
                return current_level - 1
        else:
            best = new_path[:]
            current_level += 1

if __name__ == "__main__":
    in_str = "NaN"
    while not in_str.strip().isdigit():
        in_str = input("Please enter the number of dimensions: ") 
    dim = int(in_str) # dimensionality
    best_path = []
    level = 1

    for x in range(1,dim+1):
        print(str(x) + " Dimension(s)")
        if x == dim:
            best_path = find_highest_level(x, level, True)
        else:
            if x < 5:
                level = int(find_highest_level(x, level) * 1.7) + 1
            else:
                level = int(find_highest_level(x, level) * 1.9) + 1

    #print results
    print("No. of edges: " + str(len(best_path)-1))
    print(best_path[0], end = "")
    for node in best_path[1:]:
        print(" -> " + node, end="")