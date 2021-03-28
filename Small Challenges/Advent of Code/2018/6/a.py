class POI:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = []
        self.inf = False

if __name__ == "__main__":
    # Test case from instructions
    #seeds = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]

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
    max_dist = maxx - minx + maxy - miny

    # For all squares
    for x in range(minx, maxx+1):
        for y in range(miny, maxy + 1):
            closest_dist = max_dist
            closest_indicies = []
            
            # Find closest POI
            for poi in range(len(lst_poi)):
                # Manhattan distance
                poi_dist = abs(lst_poi[poi].x - x) + abs(lst_poi[poi].y - y)

                if poi_dist == 0: # Shortcut: if on square itself
                    closest_indicies = [poi]
                    break

                # If leq min
                if poi_dist <= closest_dist:
                    # If new min, reset tracking
                    if poi_dist < closest_dist:
                        closest_dist = poi_dist
                        closest_indicies = []

                    # Add current POI to closest
                    closest_indicies.append(poi)

            # Process after checks
            if len(closest_indicies) > 1: # Equal spacing
                continue
            elif len(closest_indicies) == 0: # This shouldn't happen
                raise IndexError("Tile is missing closest POI")
            else: # Only 1 closest
                # Add tile to closest POI and set inf flag if tile is at edge
                lst_poi[closest_indicies[0]].tiles.append(closest_indicies[0])
                lst_poi[closest_indicies[0]].inf |= (x == maxx or x == minx
                                                     or y == miny or y == maxy)

    # if inf, int(not poi.inf) evaluates to 0
    print(max([len(poi.tiles) * int(not poi.inf) for poi in lst_poi]))
        
