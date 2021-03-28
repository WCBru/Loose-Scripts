DELTAS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def parse(line):
    return (line[0], int(line[1:]))

def add(p1, p2, mult):
    return tuple([p1[i] + mult * p2[i] for i in range(len(p1))])

if __name__ == "__main__":
    pos = (0, 0)
    head = 0

    lines = open("input.txt").read().split("\n")
    for line in lines:
        d, e = parse(line)
        if d == "N":
            pos = add(pos, DELTAS[3], e)
        elif d == "E":
            pos = add(pos, DELTAS[0], e)
        elif d == "S":
            pos = add(pos, DELTAS[1], e)
        elif d == "W":
            pos = add(pos, DELTAS[2], e)
        elif d == "F":
            pos = add(pos, DELTAS[head], e)
        elif d == "L":
            head = (head - (e // 90)) % 4
        elif d == "R":
            head = (head + (e // 90)) % 4

    print(abs(pos[0]) + abs(pos[1]))
