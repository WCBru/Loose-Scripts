A = ord("A")
Z = ord("Z")
a = ord("a")
z = ord("z")

DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CROSSDELTAS = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

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

    def add_key(self, text, pos=None):
        letter = text[self.pos[0]][self.pos[1]] if pos is None else\
                 text[pos[0]][pos[1]]
        if ord(letter) >= a and ord(letter) <= z:
            self.keys[ord(letter) - a] = True

    def add_all_keys(self, text):
        for rob in range(4):
            self.add_key(text, pos=self.pos[2*rob:2*rob+2])

    def code(self):
        return sum([2**(k) if self.keys[k] else 0 for k in range(len(self.keys))])

    def get_adjacent(self, graph, text):
        output = []
        coords = [self.pos[2*x:(2*x+2)] for x in range(4)]
        for rob in range(4):
            tempCoord = coords[:]
            #print(tempCoord)
            for nodeLoc, nodeCost in graph[coords[rob]]:
                if self.can_reach(text[nodeLoc[0]][nodeLoc[1]]):
                    tempCoord[rob] = nodeLoc
                    newCoord = [None for x in range(8)]
                    for r in range(4):
                        newCoord[2*r] = tempCoord[r][0]
                        newCoord[2*r+1] = tempCoord[r][1]
                    #print(node)
                    output.append((tuple(newCoord), nodeCost))

        return output

def find_features(textmap):
    nodeList = set()
    start = None
    keyLoc = []#[None for x in range(26)]
    doorLoc = []#[None for x in range(26)]

    # Find all intersections 
    for row in range(1, len(textmap) - 1):
        for col in range(1, len(textmap[row]) - 1):
            tile = textmap[row][col]
            tileord = ord(tile)
            # note tile if not wall and
            if tile == "@":
                start = (row, col)
            elif (tileord >= A and tileord <= Z):
                doorLoc.append((row, col))
            elif (tileord >= a and tileord <= z):
                keyLoc.append((row, col))                
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

def splitPoint(node):
    return [node[2*x:(2*x+2)] for x in range(len(node)//2)]
    
if __name__ == "__main__":
    # Read in map
    textmap = open("input2.txt").read().strip().split('\n')
    for row in range(len(textmap)):
        textmap[row] = [c for c in textmap[row]]
    
    nodeList, start, keyLoc, doorLoc = find_features(textmap)
    nodeList.remove(start)
    textmap[start[0]][start[1]] = "#"
    newStarts = []
    for d in range(4):
        toRemove = (start[0] + DELTAS[d][0], start[1] + DELTAS[d][1])
        textmap[toRemove[0]][toRemove[1]] = "#"
        nodeList.remove(toRemove)
        newStarts.append((start[0] + CROSSDELTAS[d][0],
                          start[1] + CROSSDELTAS[d][1]))
        nodeList.add(newStarts[d])
        textmap[newStarts[d][0]][newStarts[d][1]] = "@"

    #for row in textmap:
    #    print(''.join(row))
    
    graph = generate_graph(nodeList, textmap)
    #print(newStarts[0] in graph)
    graph = refine_graph(graph, list(newStarts) + keyLoc + doorLoc)

    firstState = []
    for s in newStarts:
        firstState.append(s[0])
        firstState.append(s[1])

    toVisit = [State(tuple(firstState), keys=[False for x in range(len(keyLoc))])]
    visited = {}
    while len(toVisit) > 0:
        current = toVisit.pop()
        current.add_all_keys(textmap)
        code = current.code()

        if all(current.keys): # Exit condition: all keys found
            print(current.cost)
            break
        
        # Check if state has already been noted for this code
        pts = splitPoint(current.pos)
        if code in visited:
            if all([pts[p] in visited[code][p] for p in range(4)]):
                continue
        else:
            visited[code] = [set() for x in range(4)]

        # Note this state as visited
        for r in range(4):
            visited[code][r].add(pts[r])

        #print(sum(current.keys))
        for adjNode, adjCost in current.get_adjacent(graph, textmap):
            adjPts = splitPoint(adjNode)
            if any([adjPts[p] not in visited[code][p] for p in range(4)]):
                #print(adjNode)
                newState = State(adjNode,
                                 cost=current.cost + adjCost,
                                 keys=current.keys)
                toVisit.append(newState)

        toVisit.sort(reverse=True, key=lambda x: x.cost)
    else:
        raise Exception("No solution found")
