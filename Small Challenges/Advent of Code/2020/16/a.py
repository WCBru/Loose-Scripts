def parse_range(line):
    parts = line.split(": ")
    ranges = parts[1].split(" or ")
    lims = set()
    for r in ranges:
        mini, maxi = r.split("-", 2)

        # Assuming all ranges are mutally exclusive
        lims.add((int(mini), int(maxi)))

    return (parts[0], lims)

if __name__ == "__main__":
    sections = open("input.txt").read().strip().split("\n\n")

    ranges = set()
    for line in sections[0].split("\n"):
        _, limits = parse_range(line)
        for L in limits:
            for mini, maxi in list(ranges):
                if (L[0] >= mini and L[0] <= maxi) or \
                   (L[1] >= mini and L[1] <= maxi):
                    
                    allNums = [L[0], L[1], mini, maxi]
                    ranges.remove((mini, maxi))
                    ranges.add((min(allNums), max(allNums)))
                    break
            else:
                    ranges.add(L)

    # Check each line
    total = 0
    for line in sections[2].split("\n")[1:]:
        for s in line.split(","):
            num = int(s)
            for ran in ranges:
                if num >= ran[0] and num <= ran[1]:
                    break
            else:
                total += num

    print(total)
