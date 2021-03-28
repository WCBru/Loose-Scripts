# Assming all tiles in the region are connected
class POI:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = []
        self.inf = False

if __name__ == "__main__":
    seeds = []
    
    # Read in each line
    doc = open("input.txt")
    line = doc.readline()
    while line != "":
        seg = line.split(", ")
        seeds.append((int(seg[0]), int(seg[1])))
        line = doc.readline()
    doc.close()
    
    # Mins and Max
    minx = min([seg[0] for seg in seeds])
    miny = min([seg[1] for seg in seeds])
    maxx = max([seg[0] for seg in seeds])
    maxy = max([seg[1] for seg in seeds])
    lst_poi = [POI(seg[0], seg[1]) for seg in seeds]
    region_size = 0
    
    # For all squares
    for x in range(minx, maxx+1):
        for y in range(miny, maxy + 1):            
            tile_total_dist = 0 # Distance for tile

            # Go through each POI
            for poi in lst_poi:
                # Manhattan distance
                tile_total_dist += abs(poi.x - x) + abs(poi.y - y)

            # Increment Region size if tile total < 10,000    
            region_size += 1 if tile_total_dist < 10000 else 0

            # End nested for
            
    # if inf, int(not poi.inf) evaluates to 0
    print(region_size)
        
