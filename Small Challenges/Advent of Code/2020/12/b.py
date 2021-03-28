DELTAS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
ROTS = [1, 0, -1, 0]

def parse(line):
    return (line[0], int(line[1:]))

def add(p1, p2, mult):
    return tuple([p1[i] + mult * p2[i] for i in range(len(p1))])

def rotate(position, angle, direction):
    cos = (angle // 90) % 4
    sin = (((direction * angle // 90) - 1) % 4)

    return (ROTS[cos] * position[0] + ROTS[sin - 2] * position[1],
            ROTS[sin] * position[0] + ROTS[cos] * position[1])

if __name__ == "__main__":
    pos = (0, 0)
    waypoint = (10, 1)
    head = 0

    lines = open("input.txt").read().split("\n")
    for line in lines:
        d, e = parse(line)
        if d == "N":
            waypoint = add(waypoint, DELTAS[3], e)
        elif d == "E":
            waypoint = add(waypoint, DELTAS[0], e)
        elif d == "S":
            waypoint = add(waypoint, DELTAS[1], e)
        elif d == "W":
            waypoint = add(waypoint, DELTAS[2], e)
        elif d == "F":
            pos = add(pos, waypoint, e)
        elif d == "L":
           waypoint = rotate(waypoint, e, 1)
        elif d == "R":
            waypoint = rotate(waypoint, e, -1)

    print(abs(pos[0]) + abs(pos[1]))
