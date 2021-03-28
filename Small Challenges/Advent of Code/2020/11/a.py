def iterate(nested):
    changed = False
    prev = [None for x in nested[0]]

    for row in range(1, len(nested) - 1):
        newRow = [x for x in nested[row]]
        for col in range(1, len(nested[row]) - 1):
            if nested[row][col] == None:
                continue
            
            tCount = 0
            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    if d1 == 0 and d2 == 0:
                        continue
                    elif nested[row + d1][col + d2]:
                        tCount += 1
            
            if nested[row][col] and tCount >= 4:
                changed = True
                newRow[col] = False
            elif not nested[row][col] and tCount == 0:
                changed = True
                newRow[col] = True
                
        nested[row - 1] = prev
        prev = newRow[:]

    nested[-2] = prev

    return changed

if __name__ == "__main__":
    seats = [([None] + [True if x == "#" else
                       (False if x == "L" else None) for x in row] + [None])
             for row in open("input.txt").read().strip().split("\n")]

    seats.insert(0, [None for x in seats[0]])
    seats.append([None for x in seats[0]])

    cont = True
    while cont:
        cont = iterate(seats)


    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seats[row][col] = 0 if seats[row][col] == None else seats[row][col]
    print(sum([sum(row) for row in seats]))

    
