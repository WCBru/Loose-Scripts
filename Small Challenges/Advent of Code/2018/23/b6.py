def dist(pos1, pos2 = None):
    pos2a = pos2 if pos2 != None else tuple([0 for i in pos1])
    return sum([abs(pos1[i] - pos2a[i]) for i in range(len(pos1))])

class Bot:
    def __init__(self, center, radius):
        self.center = tuple([coord for coord in center])
        self.radius = radius

    def intersect(self, box2):
        return dist(self.center, box2.center) <= (
            self.radius + box2.radius)

class Box:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.limits = ((x1, x2), (y1, y2), (z1, z2))

    def bot_intersect(self, center, radius):
        radRequired = 0
        for i in range(len(self.limits)):
            # If out of limits, add to the radius required
            if center[i] < self.limits[i][0] or center[i] > self.limits[i][1]:
                radRequired += min([abs(coord - center[i])
                                    for coord in self.limits[i]])

        return radRequired <= radius

    def count_intersects(self, bot_list):
        return sum([int(self.bot_intersect(bot.center, bot.radius))
                    for bot in bot_list])

    def subdivide(self):
        subCoords = []
        for dim in self.limits:
            subCoords.append([dim[0], (dim[0] + dim[1]) // 2,
                              ((dim[0] + dim[1]) // 2) + int((dim[1] - dim[0]) % 2 == 1),
                              dim[1]])


        return [Box(subCoords[0][x], subCoords[0][x+1],
                    subCoords[1][y], subCoords[1][y+1],
                    subCoords[2][z], subCoords[2][z+1])
                    for x in range(0, 3, 2)
                    for y in range(0, 3, 2)
                    for z in range(0, 3, 2)]

    def longest_length(self):
        return max([coord[1] - coord[0] + 1 for coord in self.limits])

    def min_pt(self):
        return tuple([lim[0] for lim in self.limits])

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

        output.append(Bot(pos, radius))
        line = doc.readline()

    return output

def create_center_bounds(bot_list):
    minX = bot_list[0].center[0]
    maxX = minX
    minY = bot_list[0].center[1]
    maxY = minY
    minZ = bot_list[0].center[2]
    maxZ = minZ
    for bot in bot_list:
        minX = min(minX, bot.center[0])
        maxX = max(maxX, bot.center[0])
        minY = min(minY, bot.center[1])
        maxY = max(maxY, bot.center[1])
        minZ = min(minZ, bot.center[2])
        maxZ = max(maxZ, bot.center[2])

    return Box(minX, maxX, minY, maxY, minZ, maxZ)

if __name__ == "__main__":
    bots = get_bots("input.txt")
    boundBox = create_center_bounds(bots)
    maxIntersects = max([sum([bot.intersect(b2) for b2 in bots]) for bot in bots])

    finished = False
    while not finished:
        boxes = [boundBox]
        sideLength = boundBox.longest_length()
        while sideLength > 1:
            #print(sideLength)
            newBoxes = []
            for box in boxes:
                if box.count_intersects(bots) >= maxIntersects:
                    newBoxes += box.subdivide()
            boxes = newBoxes
            sideLength = (sideLength + 1) // 2
        finished = len(boxes) > 0
        maxIntersects -= 1

    bestCoverage = 0
    bestPt = (0, 0, 0)
    for box in boxes:
        cover = box.count_intersects(bots)
        if cover > bestCoverage:
            bestCoverage = cover
            bestPt = box.min_pt()
        elif cover == bestCoverage:
            bestPt = bestPt if dist(bestPt) < dist(box.min_pt()) else box.min_pt()

    print(bestPt)
    print(dist(bestPt))
