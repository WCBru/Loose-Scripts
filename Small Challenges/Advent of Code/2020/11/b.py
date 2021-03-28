def iterate(nested):
    changed = False
    copy = [row[:] for row in nested]

    for row in range(len(nested)):
        for col in range(len(nested[row])):
            if nested[row][col] == None:
                continue
            
            tCount = 0
            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    if d1 == 0 and d2 == 0:
                        continue

                    curr = (row + d1, col + d2)
                    while curr[0] >= 0 and curr[0] < len(nested) and \
                          curr[1] >= 0 and curr[1] < len(nested[row]):
                        if nested[curr[0]][curr[1]] != None:
                            break
                        curr = (curr[0] + d1, curr[1] + d2)
                    else:
                        continue
                        
                    if nested[curr[0]][curr[1]]:
                        tCount += 1

            if nested[row][col] and tCount >= 5:
                changed = True
                copy[row][col] = False
            elif not nested[row][col] and tCount == 0:
                changed = True
                copy[row][col] = True

    return (changed, copy)

if __name__ == "__main__":
    seats = [[True if x == "#" else (False if x == "L" else None) for x in row]
             for row in open("input.txt").read().strip().split("\n")]

    cont = True
    while cont:
        cont, seats = iterate(seats)

    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seats[row][col] = 0 if seats[row][col] == None else seats[row][col]
    print(sum([sum(row) for row in seats]))

    
