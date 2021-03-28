A = ord("A")
Z = ord("Z")

DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # order is important

def add(p1, p2):
    return tuple([p1[i] + p2[i] for i in range(len(p1))])

def parse_map(text):
    start = None
    end = None
    portals = {}
    nodes = set()

    for row in range(1, len(text) - 1):
        for col in range(1, len(text[row]) - 1):

            # only parse empty spaces
            if text[row][col] == '.':
                connections = 0
                for d in range(len(DELTAS)):
                    pt = (row + DELTAS[d][0], col + DELTAS[d][1])
                    char = text[pt[0]][pt[1]]

                    # Adjacent to letter: check what kind it is
                    if ord(char) >= A and ord(char) <= Z:
                        nodes.add((row, col)) # Add this point as a node
                        pt2 = add(pt, DELTAS[d])
                        char2 = text[pt2[0]][pt2[1]]
                        label = (char + char2) if d < 2 else (char2 + char)

                        if label == "AA":
                            start = (row, col)
                        elif label == "ZZ":
                            end = (row, col)
                        else: # Portal
                            if label in portals:
                                portals[label].append((row, col))
                            else:
                                portals[label] = [(row, col)]
                                
                    elif char == ".":
                        connections += 1

                    if connections != 2 and connections != 0:
                        nodes.add((row, col)) # set should preclude dupes

    return (start, end, portals, nodes)

def create_graph(text, nodes):
    output = {node:set() for node in nodes}
    for node in nodes:
        for d in DELTAS:
            prev = node
            current = add(node, d)
            cost = 1
            if text[current[0]][current[1]] != ".":
                continue
            
            while current not in nodes:
                for d in DELTAS:
                    newPt = add(current, d)
                    if text[newPt[0]][newPt[1]] == "." and newPt != prev:
                        prev = current
                        current = newPt
                        cost += 1
                        break
                else:
                    print(text[current[0]][current[1]])
                    
                    raise Exception("Next stop not found")

            output[node].add((current, cost))

    return output

def consolidate_portals(graph, portals):
    for label in portals:
        ends = portals[label]
        if len(ends) != 2:
            raise IndexError(label + " does not have 2 endpoints")

        end1, end2 = list(ends)
        for conn1 in graph[end1]:
            node1, cost1 = conn1
            for conn2 in graph[end2]:
                node2, cost2 = conn2
                graph[node1].add((node2, cost2 + cost1 + 1))
                graph[node2].add((node1, cost2 + cost1 + 1))

                if node1 in graph:
                    graph[node1].remove((end1, cost1))
                    
                if node2 in graph:
                    graph[node2].remove((end2, cost2))

        del graph[end1]
        del graph[end2]

    return graph

if __name__ == "__main__":
    textmap = [[c for c in row]
               for row in open("input.txt").read().strip("\n").split('\n')]

    start, end, portals, nodes = parse_map(textmap)
    graph = create_graph(textmap, nodes)
    graph = consolidate_portals(graph, portals)

    # Search
    visited = set()
    toVisit = [(start, 0)]
    while True:
        pos, cost = toVisit.pop()
        if pos == end:
            print(cost)
            break
        elif pos in visited:
            continue
        else:
            visited.add(pos)
            for node, nodeCost in graph[pos]:
                if node not in visited:
                    toVisit.append((node, cost + nodeCost))

            toVisit.sort(reverse=True, key=lambda x:x[1])
