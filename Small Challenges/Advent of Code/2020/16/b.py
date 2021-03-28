def parse_range(line):
    parts = line.split(": ")
    ranges = parts[1].split(" or ")
    lims = set()
    for r in ranges:
        mini, maxi = r.split("-", 2)

        # Assuming all ranges are mutally exclusive
        lims.add((int(mini), int(maxi)))

    return (parts[0], lims)

def match_ranges(ranges, values):
    output = []
    for ran in ranges:
        valid = [False for x in values]
        for val in range(len(values)):
            for lims in ranges[ran]:
                valid[val] |= values[val] >= lims[0] and values[val] <= lims[1]

        if all(valid):
            output.append(ran)

    return output

if __name__ == "__main__":
    sections = open("input.txt").read().strip().split("\n\n")

    ranges = set()
    fields = {}
    names = []
    for line in sections[0].split("\n"):
        name, limits = parse_range(line)
        names.append(name)
        fields[name] = limits
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
    validLines = []
    for line in sections[2].split("\n")[1:]:
        valid = True
        for s in line.split(","):
            num = int(s)
            for ran in ranges:
                if num >= ran[0] and num <= ran[1]:
                    break
            else:
                valid = False
                break
                
        if valid:
            validLines.append([int(s) for s in line.split(",")])

    # Reshape list to test all values in a field
    allValues = [[0 for line in validLines] for x in validLines[0]]
    for char in range(len(validLines[0])):
        for line in range(len(validLines)):
            allValues[char][line] = validLines[line][char]

    # Find the order
    order = [None for x in fields]
    allocated = [False for x in fields]
    while len(fields) > 0:
        changed = False

        for f in range(len(allValues)):

            # Skip of field is already allocated
            if allocated[f]:
                continue

            # Match based on the remaining field names
            matches = match_ranges(fields, allValues[f])
            if len(matches) == 0:
                raise IndexError("No matches found")
            elif len(matches) == 1:
                order[f] = matches[0]
                print(matches[0])
                del fields[matches[0]]
                changed = True
                allocated[f] = True
                break                

        if not changed:
            raise IndexError("No allocations possible")

    # Calculate final value
    ticket = [int(num) for num in
              sections[1][sections[1].index("\n"):].split(",")]
    total = 1
    for word in range(len(order)):
        if order[word].split()[0] == "departure":
            total *= ticket[word]

    print(total)
