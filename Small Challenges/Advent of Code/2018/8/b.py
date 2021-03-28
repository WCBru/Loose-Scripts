# Part B strategy - add new property for value
# Examine the last node added to the list - this should be the root node
# (Assuming it's all under one common root)

# Class for node
class Node:
    def __init__(self):
        self.child_values = []
        self.metadata = []
        self.value = 0

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

    # Recursively go through children
    for child in range(num_child):
        new_index, val = expand_node(new_index, inp, out)
        new_node.child_values.append(val)

    # Add on metadata at the end
    for meta in range(num_meta):
        new_node.metadata.append(inp[new_index + meta])

    # Parse Value of node
    if num_child == 0:
        new_node.value = sum(new_node.metadata)
    else: # Go through meta list
        for meta_val in inp[new_index:new_index+num_meta]:
            # Skip 0, numbers too large
            if meta_val > 0 and meta_val <= num_child:
                # Get relevant child using negative indicies
                # Note for nth child, meta_val = n => -1
                # For 1st child, meta_val = 1 => -num_child
                new_node.value += new_node.child_values[meta_val - 1]
    
    out.append(new_node) # Add node to node list
    new_index += num_meta # Index after header, children, metadata
    return (new_index, new_node.value)

# Strategy: Recursively find the nodes and add them to the main list
# Then do the checksum at the end
if __name__ == "__main__":
    node_list = [] # Nodes processed
    index = 0 # Index during input processing
    in_list = parse_input("input.txt") # Input

    # Expand all nodes (index == length of input)
    while index < len(in_list):
        index, val = expand_node(index, in_list, node_list)

    # This shouldn't be possible - process beyond the end of input
    if index > len(in_list):
        raise ValueError("Index overshot list length")

    # Print sum of all metadata
    print(node_list[-1].value)
