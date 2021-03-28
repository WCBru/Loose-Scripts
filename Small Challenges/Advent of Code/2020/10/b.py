def count_combos(sl):
    if len(sl) < 2:
        return 1

    sset = set(sl)
    start = sl[0]
    end = sl[-1]
    toExpand = [start]
    count = 0

    while len(toExpand) > 0:
        curr = toExpand.pop()
        for delta in range(1, 4):
            if curr + delta in sset:
                if curr + delta == end:
                    count += 1
                else: # if too slow, construct from higher end to lower end
                    toExpand.append(curr + delta)

    return count
        

if __name__ == "__main__":
    jolts = [0] + [int(x) for x in open("input.txt").read().strip().split("\n")]
    jolts.sort()
    jolts.append(jolts[-1] + 3)

    slices = []
    lower = 0
    upper = 1
    for j in range(1, len(jolts)):
        if jolts[j] - jolts[j - 1] == 3:
            slices.append(jolts[lower:j])
            lower = j

    total = 1
    for sl in slices:
        total *= count_combos(sl)

    print(total)
            
