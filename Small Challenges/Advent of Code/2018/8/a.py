# Class for node
class Node:
    def __init__(self):
        self.children = 0
        self.metadata = []

# Parse input into list
def parse_input(doc_name):
    return [int(num) for num in open(doc_name).read().split()]

# Recursive function to categorise nodes
def expand_node(ind, inp, out):
    # Info from input
    num_child = inp[ind]
    num_meta = inp[ind+1]

    # Index start of children (or metadata if no children)
    new_index = ind + 2

    # Make a new node
    new_node = Node()
    new_node.children = num_child

    # Recursively go through children
    for child in range(num_child):
        new_index = expand_node(new_index, inp, out)

    # Add on metadata at the end
    for meta in range(num_meta):
        new_node.metadata.append(inp[new_index + meta])
    
    out.append(new_node) # Add node to node list
    return new_index + num_meta # Return index after header, children, metadata

# Strategy: Recursively find the nodes and add them to the main list
# Then do the checksum at the end
if __name__ == "__main__":
    node_list = [] # Nodes processed
    index = 0 # Index during input processing
    in_list = parse_input("input.txt") # Input

    # Expand all nodes (index == length of input)
    while index < len(in_list):
        index = expand_node(index, in_list, node_list)

    # This shouldn't be possible - process beyond the end of input
    if index > len(in_list):
        raise ValueError("Index overshot list length")

    # Print sum of all metadata
    print(sum([sum(node.metadata) for node in node_list]))
