def load_pts(fileName):
    doc = open(fileName)
    output = []
    line = doc.readline()

    while line.strip() != "":
        output.append(tuple([int(coord) for coord in line.strip().split(",")]))
        line = doc.readline()
    
    doc.close()
    return output

def dist(coord1, coord2):
    return sum([abs(coord1[i] - coord2[i]) for i in range(len(coord1))])

def get_coords_in_range(src, targets, radius):
    output = []
    for target in targets:
        if dist(src, target) <= radius and target != src:
            output.append(target)

    return output

def remove_constellation(pts, conn_list):
    toExpand = [pts[0]]
    while len(toExpand) > 0:
        pt = toExpand.pop(0)
        if pt in pts:
            pts.remove(pt)
            toExpand += conn_list[pt]

if __name__ == "__main__":
    coords = load_pts("input.txt")
    # Reduce list size with each iteration to create a tree
    connections = {coords[i]: get_coords_in_range(coords[i], coords, 3) \
                   for i in range(len(coords))}
    constCount = 0
    while len(coords) > 0:
        remove_constellation(coords, connections)
        constCount += 1

    print(constCount)
    
