'''####################b.py
DELTAS = [tuple([sgn if inner == ind else 0 for inner in range(3)])
          for sgn in [-1, 1]
          for ind in range(3)]

# Read input into a dict {pos: radius}
def gen_bot_lst(doc_name):
    output = {}
    doc = open(doc_name)
    line = doc.readline()

    # For each line
    while line != "":
        parts = line.split(", ") # Split line into parts

        # Extract position and radius
        pos = tuple([int(val) for val in parts[0][5:-1].split(",")])
        radius = int(parts[1].split("=")[1])

        # Add to output and get next line
        output[pos] = radius
        line = doc.readline()

    return output

# Function for getting Manhattan distance
def dist(pos1, pos2): # Hard coding size here
    return sum(abs(pos1[i]-pos2[i]) for i in range(3))

# 
def get_visible_bots(lst, pos, rad):
    return sum([int(dist(bot, pos) <= max(lst[bot], rad)) for bot in lst.keys()])

def get_best_coverage(bot_list, bot_pos, rad=None):
    radius = bot_list[bot_pos] if rad == None else rad
    corner_score = {}
    
    corners = [ tuple([delta[i]*radius+bot_pos[i] for i in range(3)])
                           for delta in DELTAS ]
    
    for corner in corners:
        corner_score[corner] = get_visible_bots(bot_list, corner, 0)
        #print(coverage)

    sorted_corners = sorted(corner_score, key=lambda corn:corner_score[corn])
    best_score = corner_score[sorted_corners[-1]]
    ind = -1
    while corner_score[sorted_corners[ind]] == best_score:
        ind -= 1
        
    return (best_score, sorted_corners[ind+1:])

# Remove all points from stack under val
def remove_under(val, lst):
    output = lst
    for i in range(len(lst)-1, -1, -1):
        if output[i][1] < val:
            output.pop(i)

    return output
        
# Since the best spots must at least contain a corner, just need to test
# corners and then search to find the best point
if __name__ == "__main__":
    bot_list = gen_bot_lst("input.txt")

    # Get the bot with the largest radius
    best_bot = sorted(bot_list.keys(), key=lambda bot:bot_list[bot])[-1]
    best_bot_rad = bot_list[best_bot]

    #print(get_visible_bots(bot_list, best_bot,best_bot_rad))

    # Test for time complexity for 1 bot
    best_cover = 0
    best_corners = []
    for bot in bot_list:
        cover, points = get_best_coverage(bot_list, bot)
        
        if cover > best_cover:
            best_cover = cover
            best_corners = points
        elif cover == best_cover:
            best_corners += points

        print("Done")

    print(best_cover,best_corners)

    best_cover_changed = True
    best_dist = dist(best_corners[0], (0,0,0)) # Dummy value: first in list
    while len(best_corners) > 0: # Gradually remove all corners
        stack = [(best_corners[0], best_cover)]
        expanded = []

        

        while len(stack) > 0:
            current_pos, current_cover = stack.pop(0)
            current_dist = sum([abs(val) for val in current_pos])

            if current_cover < best_cover:
                continue
            #print(current_dist)
            #print(len(expanded))

            if current_dist < best_dist or best_cover_changed:
                best_cover_changed = False
                best_dist = current_dist

            if current_pos in best_corners:
                best_corners.remove(current_pos)

            adj_points = [ tuple([delta[i]+current_pos[i] for i in range(3)])
                           for delta in DELTAS ]
            for adj in adj_points:
                adj_visible_bots = get_visible_bots(bot_list, adj, 0)
                adj_dist = sum([abs(val) for val in adj])
                if adj_visible_bots >= best_cover and adj not in expanded:
                    stack.append((adj, adj_visible_bots))
                    expanded.append(adj)
                    if adj_visible_bots > best_cover:
                        best_cover_changed = True
                        best_cover = adj_visible_bots
                        stack = remove_under(best_cover, stack)
                        print(best_cover)

    print(best_dist)

####################b2.py
import numpy as np

class Volume:
    def __init__(self, points):
        self.points = points
        
    def pointIntersects(self, x, y, z):
        pass

def read_rects(fileName):
    output = []
    file = open(fileName)
    line = file.readline()
    while line != "":
        parts = line.split("pos=<")[1].split(">, r=")
        parts = [int(i) for i in parts[0].split(",") + [parts[-1]]]
        output.append(Rect(parts[0], parts[1], parts[2], parts[3]))
        line = file.readline()

    return output

if __name__ == "__main__":
    rectList = read_rects("input_test.txt")

    print(rectList)

####################b3.py
DELTAS = [tuple([sgn if inner == ind else 0 for inner in range(3)])
          for sgn in [-1, 1]
          for ind in range(3)]

# Read input into a dict {pos: radius}
def gen_bot_lst(doc_name):
    output = {}
    doc = open(doc_name)
    line = doc.readline()

    # For each line
    while line != "":
        parts = line.split(", ") # Split line into parts

        # Extract position and radius
        pos = tuple([int(val) for val in parts[0][5:-1].split(",")])
        radius = int(parts[1].split("=")[1])

        # Add to output and get next line
        output[pos] = radius
        line = doc.readline()

    return output

def dist(coord1, coord2=(0,0,0)):
    return sum(abs(coord1[i] - coord2[i]) for i in range(len(coord1)))

def bots_intersect(bot1, bot2, rad1, rad2):
    return dist(bot1, bot2) < rad1 + rad2

def get_deltas(pt):
    output = []
    for delt in DELTAS:
        output.append(tuple([pt[i] + delt[i] for i in range(len(pt))]))
    return output

def fill_intersects(bots, bot1, bot2, pts, highest, lst):
    if not bots_intersect(bot1, bot2, bots[rect1], bots[rect2]):
        return highest

    highestInt = highest
    visited = {}
    toExpand = [tuple([(bot1[i] + bot2[i])//2 for i in range(len(bot1))])]

    while len(toExpand) > 0:
        #print("Expaniding...")
        newPt = toExpand.pop()
        if newPt not in visited:
            visited[newPt] = None
            for adj in get_deltas(newPt):
                if dist(bot1, adj) <= bots[bot1] and dist(bot2, adj) <= bots[bot2] and adj not in visited:
                    toExpand.append(adj)

    for pt in visited.keys():
        #print("Checking visited")
        if pt not in pts:
            pts[pt] = 1
        else:
            pts[pt] += 1
            if highestInt < pts[pt]:
                highestInt = pts[pt]
                lst = [pt]
            elif highestInt == pts[pt]:
                lst.append(pt)

    return highestInt

if __name__ == "__main__":
    bot_list = gen_bot_lst("input.txt")

    intersects = { pt : sum([int(bots_intersect(pt, pt2, bot_list[pt], bot_list[pt2])) for pt2 in bot_list.keys()]) for pt in bot_list}
    sList = sorted(bot_list.keys(), key = intersects.get)
    print("Intersects calculated for " + str(len(bot_list)) + " bots")
    
    currentMax = 0
    intersections = {}
    i = 0
    highList = []
    bots_as_lst = sList
    while i < len(bot_list):
        if i % 10 == 0:
            print("Done " + str(i) + " bots")
        rect1 = bots_as_lst[i]
        if intersects[rect1] < currentMax:
            break
        for rect2 in bots_as_lst[i:]:
            currentMax = fill_intersects(bot_list, rect1, rect2, intersections, currentMax, highList)
        i += 1
            
    print(currentMax)
    print(sorted(highList, key=dist)[0])

####################b4.py
def dist(coord1, coord2 = (0,0,0)):
    return sum([abs(coord1[i] - coord2[i]) for i in range(len(coord1))])

def get_adjascent(pt):
    output = []
    for m in [-1, 1]:
        for i in range(len(pt)):
            output.append(tuple([pt[j] + (0 if j != i else m) for j in range(len(pos))]))

    #print(output)
    return output

class Bot:
    def __init__(self, pos, rad, corn):
        self.center = pos
        self.radius = rad
        self.corners = corn
        self.dim = len(pos)

    def intersects(self, pos):
        return dist(self.center, pos) <= self.radius

def gen_corners(corners):
    output = []
    for ind in range(len(corners)):
        start = corners[ind]
        for dInd in [-1, -2]:
            end = corners[ind + dInd]
            delta = tuple([end[i] - start[i] for i in range(len(start))])
            delta = tuple([delta[i]/abs(delta[i]) if delta[i] != 0 else 0 for i in range(len(delta))])

            pt = tuple([start[i] + delta[i] for i in range(len(start))])
            while pt != end:
                output.append(pt)
                pt = tuple([pt[i] + delta[i] for i in range(len(start))])

def get_bots(docName):
    output = []
    doc = open(docName)
    line = doc.readline()

    # For each line
    while line != "":
        parts = line.split(", ") # Split line into parts
        
        # Extract position and radius
        pos = tuple([int(val) for val in parts[0][5:-1].split(",")])
        radius = int(parts[1].split("=")[1])

        corners = []
        for m in [-1, 1]:
            for i in range(3):
                corners.append(tuple([pos[j] + (0 if j != i else m * radius) for j in range(len(pos))]))

        output.append(Bot(pos, radius, corners))
        line = doc.readline()

    return output

def count_intersects(pos, bots):
    return sum([int(bot.intersects(pos)) for bot in bots])

if __name__ == "__main__":
    botList = get_bots("input.txt")
    corners = []

    print("Bots generated")

    maxIntersectCount = 0
    maxIntersectPos = [(0, 0, 0)]
    counter = 0

    for bot in botList:
        print(counter)
        for ind in range(len(bot.corners)):
            start = bot.corners[ind]
            for dInd in [-1, -2]:
                end = bot.corners[ind + dInd]
                delta = tuple([end[i] - start[i] for i in range(len(start))])
                delta = tuple([delta[i]//abs(delta[i]) if delta[i] != 0 else 0 for i in range(len(delta))])

                pt = tuple([start[i] + delta[i] for i in range(len(start))])
                print(start)
                while pt != end:
                    print(pt)
                    ints = count_intersects(pt, botList)
                    if ints > maxIntersectCount:
                        maxIntersectCount = ints
                        maxIntersectPos = [pt]
                    elif ints == maxIntersectCount:
                        maxIntersectPos.append(pt)

                    pt = tuple([pt[i] + delta[i] for i in range(len(start))])
        counter += 1

    print(min([dist(p) for p in maxIntersectPos]))

    '''
    for bot in botList:
        corners += bot.corners

    for corn in corners:
        intersects = count_intersects(corn, botList)
        if intersects > maxIntersectCount:
            #print(intersects)
            maxIntersectCount = intersects
            maxIntersectPos = [corn]
        elif intersects == maxIntersectCount:
            maxIntersectPos.append(corn)

            

    minDist = dist(maxIntersectPos[0])
    if len(maxIntersectPos) > 0:
        visited = []
        while len(maxIntersectPos) > 0:
            pos = maxIntersectPos.pop()
            minDist = min(minDist, dist(pos))
            
            if pos in visited:
                continue

            visited.append(pos)
            for adj in get_adjascent(pos):
                #print(count_intersects(adj, botList))
                interCount = count_intersects(adj, botList)
                if count_intersects(adj, botList) >= maxIntersectCount:
                    maxIntersectCount = max(maxIntersectCount, interCount)
                    maxIntersectPos.append(adj)

        print(minDist)
'''

####################b5.py
EPS = 0.001

def dist(coord1, coord2 = (0,0,0)):
    return sum([abs(coord1[i] - coord2[i]) for i in range(len(coord1))])

def gen_deltas(pt, dist = 1):
    output = []
    for m in [-1, 1]:
        for i in range(len(pt)):
            output.append(tuple([pt[j] + (0 if j != i else (m * dist))
                           for j in range(len(pt))]))
    return output

# Based on the AOC's creator's approach of octotrees
class Octo:
    def __init__(self, center, radius, intersectMod = -1):
        self.center = tuple([coord for coord in center])
        self.radius = radius
        self.interMod = intersectMod

    def subdivide(self):
        if self.radius == 0:
            return [self]
        
        # Radius = 1: return center + indiv points
        if self.radius == 1:
            return [Octo(pt, 0)
                    for pt in gen_deltas(self.center, 1) + [self.center]]

        # If even, divide by 2 and delta by the halved radius
        # If odd, round up for radius, round down for delta
        halvedRad = (self.radius + 1) * 3 // 4
        return [Octo(cent, halvedRad)
                for cent in gen_deltas(self.center, self.radius // 4)]

    def intersect(self, octo2):
        return dist(self.center, octo2.center) <= (
            self.radius + octo2.radius)

    def count_intersects(self, bots):
        return sum([int(self.intersect(bot2)) for bot2 in bots]) + self.interMod

def get_bot_largest(bot, bots):
    bestPt = bot.center
    bestCoverage = 0
    if bot.count_intersects(bots) == 0:
        return (bestPt, bestCoverage)

    if bot.radius == 0:
        return (bot.center, bot.count_intersects(bots))

    # Subdivide
    rad = bot.radius
    regions = [bot]
    while regions[0].radius > 0:
        newRegions = []
        for reg in regions:
            if reg.count_intersects(bots) > 0:
                newRegions += reg.subdivide()
        
        
        regions = newRegions
        print([(reg.center, reg.radius) for reg in regions])
    
    # Get the best coverage, closest to the origin
    coverage = [reg.count_intersects(bots) for reg in regions]
    bestCoverage = max(coverage)
    bestPt = regions[0].center
    #print([(regions[i].center, coverage[i]) for i in range(len(regions))])

    #print([reg.center for reg in regions])
    for reg in regions:
        if dist(reg.center) < dist(bestPt):
            bestPt = reg.center

    return (bestPt, bestCoverage)

def get_bots(docName):
    output = []
    doc = open(docName)
    line = doc.readline()

    # For each line
    while line != "":
        parts = line.split(", ") # Split line into parts
        
        # Extract position and radius
        pos = tuple([int(val) for val in parts[0][5:-1].split(",")])
        radius = int(parts[1].split("=")[1])

        output.append(Octo(pos, radius, -1))
        line = doc.readline()

    return output

if __name__ == "__main__":
    bots = get_bots("input_test.txt")
    maxCover = 0
    maxPt = (0, 0, 0)
    
    for bot in bots:
        pt, cover = get_bot_largest(bot, bots)
        print(pt, cover)
        if cover > maxCover:
            maxCover = cover
            maxPt = pt
        elif cover == maxCover:
            maxPt = maxPt if dist(maxPt) <= dist(pt) else pt

    print(maxPt, maxCover)

'''