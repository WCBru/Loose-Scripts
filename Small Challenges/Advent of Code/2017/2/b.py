def findDivisor(row):
    for big in row:
        multiplier = findIfFactor(row, big)
        if multiplier != -1:
            return multiplier

    print("No Factor Found!")
    return 0

def findIfFactor(row, target):
    for cell in row:
        multi = 2
        while cell* multi <= target:
            if cell*multi == target:
                return multi
            else:
                multi+= 1
                
    return -1

if __name__ == "__main__":
    data = open("data2.txt", "r")
    total = 0
    currentRow = data.readline().strip()
    while currentRow != "":
        rowData = currentRow.split()
        rowInts = [int(cell) for cell in rowData]
        rowInts.sort()
        #Since division isn't perfect, a multiplication method is used
        total += findDivisor(rowInts)
        

        currentRow = data.readline().strip()

    print(total)

