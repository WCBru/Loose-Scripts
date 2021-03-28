A = ord("A")
Z = ord("Z")
a = ord("a")
z = ord("z")

DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class State:
    def __init__(self, pos, cost=0, keys=None):
        self.cost = cost
        self.pos = pos
        if keys is not None:
            self.keys = keys[:]
        else:
            self.keys = [False for k in range(26)]

    def can_reach(self, letter):
        if ord(letter) >= A and ord(letter) <= Z and \
           not self.keys[ord(letter) - A]:
            return False

        return True

    def add_key(self, text):
        letter = text[self.pos[0]][self.pos[1]]
        if ord(letter) >= a and ord(letter) <= z:
            self.keys[ord(letter) - a] = True

    def code(self):
        return sum([2**(k) if self.keys[k] else 0 for k in range(len(self.keys))])

def find_features(textmap):
    nodeList = set()
    start = None
    keyLoc = [None for x in range(26)]
    doorLoc = [None for x in range(26)]

    # Find all intersections 
    for row in range(1, len(textmap) - 1):
        for col in range(1, len(textmap[row]) - 1):
            tile = textmap[row][col]
            tileord = ord(tile)
            # note tile if not wall and
            if tile == "@":
                start = (row, col)
            elif (tileord >= A and tileord <= Z):
                doorLoc[tileord - A] = (row, col)
            elif (tileord >= a and tileord <= z):
                keyLoc[tileord - a] = (row, col)                
            elif not (tile == "." and # Not an intersection
                      sum([textmap[row - 1][col] != "#",
                           textmap[row + 1][col] != "#",
                           textmap[row][col - 1] != "#",
                           textmap[row][col + 1] != "#"]) != 2):
                continue # don't add tile

            nodeList.add((row, col))

    return (nodeList, start, keyLoc, doorLoc)

def generate_graph(nodes, textmap):
    graph = {node: [] for node in nodes}

    for node in nodes:
        for delta in DELTAS: # check each tile adj to node
            if textmap[node[0] + delta[0]][node[1] + delta[1]] == "#":
                continue

            cost = 1
            currPos = (node[0] + delta[0], node[1] + delta[1])
            prev = node

            while currPos not in nodes: # find the next tile to move to
                for delta in DELTAS:
                    nextPos = (currPos[0] + delta[0], currPos[1] + delta[1])
                    if textmap[nextPos[0]][nextPos[1]] != "#" and nextPos != prev:
                        prev = currPos
                        currPos = nextPos
                        cost += 1
                        break
                else:
                    raise Exception("No continuation found at " + str(currPos))
            else:
                if (currPos, cost) not in graph[node]:
                    graph[node].append((currPos, cost))
                    graph[currPos].append((node, cost))
                    
    return graph

def refine_graph(graphin, landmarks):
    graphout = {node: [] for node in landmarks}
    for node in landmarks:
        visited = set()
        toVisit = [(node, 0)]

        while len(toVisit) > 0:
            nextNode, oldCost = toVisit.pop()
            visited.add(nextNode)
            for adj in graphin[nextNode]:
                adjNode, adjCost = adj
                if adjNode not in visited:
                    if adjNode in landmarks:
                        graphout[node].append((adjNode, oldCost + adjCost))
                        visited.add(adjNode)
                    else: 
                        toVisit.append((adjNode, oldCost + adjCost))
            
            toVisit.sort(reverse=True, key=lambda x: x[1])
    return graphout           

if __name__ == "__main__":
    # Read in map
    textmap = open("input.txt").read().strip().split('\n')
    for row in range(len(textmap)):
        textmap[row] = [c for c in textmap[row]]
    
    nodeList, start, keyLoc, doorLoc = find_features(textmap)
    graph = generate_graph(nodeList, textmap)
    graph = refine_graph(graph, [start] + keyLoc + doorLoc)
    
    toVisit = [State(start)]
    visited = {}
    while True:
        
        current = toVisit.pop()
        current.add_key(textmap)
        code = current.code()
        if code in visited:
            if current.pos in visited[code]:
                continue
            visited[code].add(current.pos)
        else:
            visited[code] = set()

        if all(current.keys): # Exit condition: all keys found
            print(current.cost)
            break

        for adjNode, adjCost in graph[current.pos]:
            if current.can_reach(textmap[adjNode[0]][adjNode[1]]) and \
               adjNode != start and adjNode not in visited[code]:
                newState = State(adjNode,
                                 cost=current.cost + adjCost,
                                 keys=current.keys)
                toVisit.append(newState)

        toVisit.sort(reverse=True, key=lambda x: x.cost)
    else:
        raise Exception("No solution found")
