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

def consolidate_portals(graph, portals, text):
    inner = set()
    outer = set()
    for label in portals:
        for port in portals[label]:
            if port[0] <= 3 or port[0] >= len(text) - 3 or \
               port[1] <= 3 or port[1] >= len(text[2]) - 3:
                outer.add(port)
            else:
                inner.add(port)

    rise = set()
    for label in portals:
        ends = portals[label]
        if len(ends) != 2:
            raise IndexError(label + " does not have 2 endpoints")

        end1, end2 = list(ends)
        for conn1 in graph[end1]:
            node1, cost1 = conn1
            end1Rise = end1 in outer
            for conn2 in graph[end2]:
                node2, cost2 = conn2
                if end1Rise:
                    rise.add((node1, node2))
                else:
                    rise.add((node2, node1))
                
                graph[node1].add((node2, cost2 + cost1 + 1))
                graph[node2].add((node1, cost2 + cost1 + 1))

                if node1 in graph:
                    graph[node1].remove((end1, cost1))
                    
                if node2 in graph:
                    graph[node2].remove((end2, cost2))

        del graph[end1]
        del graph[end2]

    return (graph, rise)

if __name__ == "__main__":
    textmap = [[c for c in row]
               for row in open("input.txt").read().strip("\n").split('\n')]

    start, end, portals, nodes = parse_map(textmap)
    graph = create_graph(textmap, nodes)
    graph, rise = consolidate_portals(graph, portals, textmap)
    
    end = (end[0], end[1], 0)

    # Search
    visited = set()
    toVisit = [((start[0], start[1], 0), 0)]
    while True:
        pos, cost= toVisit.pop()
        if pos == end:
            print(cost)
            break
        elif pos in visited:
            continue
        else:
            visited.add(pos)
            level = pos[2]
            gridpos = pos[0:2]
            for node, nodeCost in graph[gridpos]:
                if node not in visited:
                    newLevel = level
                    if (gridpos, node) in rise:
                        newLevel += 1
                    elif (node, gridpos) in rise:
                        newLevel -= 1

                    if newLevel > 0:
                        continue
                    
                    toVisit.append(((node[0], node[1], newLevel), cost + nodeCost))

            toVisit.sort(reverse=True, key=lambda x:x[1])
